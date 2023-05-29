import pytest

from src.tank import Tank
from src.tank_helper import TankHelper


class TestTankHelper:

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
    def tank3(self, tank_helper: TankHelper) -> Tank:
        return Tank.create("tank3", 110, tank_helper)

    @pytest.fixture
    def water_operations(self, tank1: Tank, tank2: Tank, tank3: Tank) -> None:
        tank1.pour_water(100)
        tank2.pour_water(90)

    def test_get_most_filled_tank(
        self,
        tank_helper: TankHelper,
        water_operations: None
    ):
        for tank in tank_helper.get_most_filled_tanks():
            assert tank == tank_helper.list_of_tanks[0]

    def test_get_tank_with_most_water(
        self,
        tank_helper: TankHelper,
        water_operations
    ):
        for tank in tank_helper.get_tanks_with_most_water():
            assert tank == tank_helper.list_of_tanks[0]

    def test_get_empty_tanks(self, tank_helper: TankHelper, water_operations):
        assert len(tank_helper.get_empty_tanks()) == 1
