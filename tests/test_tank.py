import pytest as pytest

from src.event_sourcer import EventSourcer
from src.tank import Tank
from src.tank_helper import TankHelper
from src.tank_manager import TankManager
from src.tank_operations import TankOperations


class TestTank:

    @pytest.fixture
    def tank_operations(self) -> TankOperations:
        return TankOperations()

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

    def test_pour_water(self, tank1: Tank, tank_manager: TankManager):
        tank_manager.pour_water(tank1.name, 10)
        assert tank1.current_volume == 10

    def test_pour_water_exceeds_capacity(
        self, tank1: Tank, tank_manager: TankManager
    ):
        assert not tank_manager.pour_water(tank1.name, 110)

    def test_pour_out_water(self, tank1: Tank, tank_manager: TankManager):
        tank_manager.pour_water(tank1.name, 10)
        tank_manager.pour_out_water(tank1.name, 10)
        assert tank1.current_volume == 0

    def test_pour_out_water_exceeds_current_volume(
        self, tank1: Tank, tank_manager: TankManager
    ):
        tank_manager.pour_water(tank1.name, 10)
        assert not tank1.pour_out_water(20)

    def test_transfer_water(
        self, tank1: Tank, tank2: Tank, tank_manager: TankManager
    ):
        tank_manager.pour_water(tank1.name, 10)
        tank_manager.transfer_water(tank1.name, tank2.name, 10)
        assert tank1.current_volume == 0
        assert tank2.current_volume == 10

    def test_transfer_water_tank_has_not_enough_water(
        self, tank1: Tank, tank2: Tank, tank_manager: TankManager
    ):
        assert not tank_manager.transfer_water(tank1.name, tank2.name, 20)

    def test_transfer_water_tank1_capacity_exceeded(
        self, tank1: Tank, tank2: Tank, tank_manager: TankManager
    ):
        assert not tank_manager.transfer_water(tank1.name, tank2.name, 105)
