import pytest

from src.event_sourcer import EventSourcer
from src.tank import Tank
from src.tank_helper import TankHelper
from src.tank_manager import TankManager
from src.tank_operations import TankOperations


class TestTankOperations:

    @pytest.fixture
    def tank_helper(self) -> TankHelper:
        return TankHelper()

    @pytest.fixture
    def tank1(self, tank_helper: TankHelper) -> Tank:
        return Tank.create("tank1", 100, tank_helper)

    @pytest.fixture
    def tank2(self, tank_helper: TankHelper) -> Tank:
        return Tank.create("tank2", 110, tank_helper)

    @pytest.fixture
    def event_sourcer(self, tank_operations: TankOperations) -> EventSourcer:
        return EventSourcer(tank_operations)

    @pytest.fixture
    def tank_manager(self, tank_helper: TankHelper, tank_operations: TankOperations,
                     event_sourcer: EventSourcer) -> TankManager:
        return TankManager(tank_helper, tank_operations, event_sourcer)

    @pytest.fixture
    def tank_operations(self) -> TankOperations:
        return TankOperations()

    @pytest.fixture
    def water_operations(self, tank1: Tank, tank2: Tank, tank_manager: TankManager) -> None:
        tank_manager.pour_water(tank1.name, 100)
        tank_manager.pour_water(tank2.name, 110)
        tank_manager.pour_out_water(tank1.name, 100)
        tank_manager.transfer_water(tank2.name, tank1.name, 55)

    @pytest.fixture
    def water_operations2(self, tank1: Tank, tank2: Tank, tank_manager: TankManager) -> None:
        tank_manager.pour_water(tank1.name, 110)
        tank_manager.pour_out_water(tank2.name, 110)

    @pytest.fixture
    def water_operations3(self, tank1: Tank, tank2: Tank, tank_manager: TankManager) -> None:
        tank_manager.pour_water(tank1.name, 110)
        tank_manager.pour_water(tank2.name, 110)

    def test_get_tanks_with_most_failed_operations_returns_one(
            self, tank1: Tank, tank_helper: TankHelper, tank_operations: TankOperations, water_operations3
    ):
        assert tank_operations.get_tanks_with_most_failed_operations()[0] == tank1.name

    def test_get_tanks_with_most_failed_operations_returns_empty_list(
            self, tank_helper: TankHelper, tank_operations: TankOperations, water_operations
    ):
        assert tank_operations.get_tanks_with_most_failed_operations() == []

    def test_get_tanks_with_most_failed_operations_returns_more_then_one(
            self, tank1: Tank, tank2: Tank, tank_helper: TankHelper, tank_operations: TankOperations, water_operations2
    ):
        assert tank_operations.get_tanks_with_most_failed_operations()[0] == tank1.name
        assert tank_operations.get_tanks_with_most_failed_operations()[1] == tank2.name

    def test_get_tanks_with_most_operations_of_type_returns_one(
            self, tank1: Tank, tank2: Tank, tank_helper: TankHelper, tank_operations: TankOperations, water_operations3
    ):
        assert tank_operations.get_tanks_with_most_operations_of_type("pour_water")[0] == tank1.name
        assert tank_operations.get_tanks_with_most_operations_of_type("pour_water")[1] == tank2.name

    def test_get_tanks_with_most_operations_of_type_returns_more_than_one(
            self, tank1: Tank, tank_helper: TankHelper, tank_operations: TankOperations, water_operations
    ):
        assert tank_operations.get_tanks_with_most_operations_of_type("pour_out_water")[0] == tank1.name

    def test_get_tanks_with_most_operations_of_type_returns_empty_list(
            self, tank1: Tank, tank_helper: TankHelper, tank_operations: TankOperations, water_operations2
    ):
        assert tank_operations.get_tanks_with_most_operations_of_type("transfer_water") == []

    def test_check_state(self, tank1: Tank, tank2: Tank, tank_operations: TankOperations,
                         tank_manager: TankManager, water_operations):
        assert (
                tank1.current_volume == tank_operations.check_state(tank1.name)
        )
        assert (
                tank2.current_volume == tank_operations.check_state(tank2.name)
        )
