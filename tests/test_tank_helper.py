import pytest
from src.tank import Tank
from src.tank_helper import TankHelper
from src.tank_operations import TankOperations


class TestTankHelper:
    @pytest.fixture
    def tank_operations(self):
        return TankOperations()

    @pytest.fixture
    def tank_helper(self):
        tank_helper = TankHelper()
        tank_helper.append_to_list([Tank("tank1", 100), Tank("tank2", 110)])
        return tank_helper

    def test_get_most_filled_tank(
        self,
        tank_helper: TankHelper,
        tank_operations: TankOperations,
    ):
        tank_helper.list_of_tanks[1].pour_water(110, tank_operations)
        assert tank_helper.get_most_filled_tank() == tank_helper.list_of_tanks[1]

    def test_get_empty_tanks(self, tank_helper: TankHelper):
        assert len(tank_helper.get_empty_tanks()) == 2
