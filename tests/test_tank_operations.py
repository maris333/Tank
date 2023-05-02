import pytest
from src.tank import Tank
from src.tank_helper import TankHelper
from src.tank_operations import TankOperations


class TestTankOperations:
    @pytest.fixture
    def tank_helper(self):
        tank_helper = TankHelper()
        tank_helper.append_to_list([Tank("tank1", 100), Tank("tank2", 110)])
        return tank_helper

    @pytest.fixture
    def tank_operations(self) -> TankOperations:
        return TankOperations()

    @pytest.fixture
    def water_operations(self, tank_operations, tank_helper) -> None:
        tank_helper.list_of_tanks[0].pour_water(110, tank_operations)
        tank_helper.list_of_tanks[1].pour_water(100, tank_operations)
        tank_helper.list_of_tanks[0].pour_out_water(100, tank_operations)

    def test_get_tank_with_most_failed_operations(
        self, tank_helper: TankHelper, tank_operations: TankOperations, water_operations
    ):
        assert (
            tank_operations.get_tank_with_most_failed_operations()
            == tank_helper.list_of_tanks[0].name
        )

    def test_get_tank_with_most_operations_of_type(
        self, tank_helper: TankHelper, tank_operations: TankOperations, water_operations
    ):
        assert (
            tank_operations.get_tank_with_most_failed_operations()
            == tank_helper.list_of_tanks[0].name
        )
