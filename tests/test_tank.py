import pytest

from src.tank import Tank
from src.tank_helper import TankHelper



class TestTank:

    @pytest.fixture
    def tank_helper(self) -> TankHelper:
        return TankHelper()

    @pytest.fixture
    def tank1(self, tank_helper: TankHelper) -> Tank:
        return Tank.create("tank1", 100, tank_helper)

    @pytest.fixture
    def tank2(self, tank_helper: TankHelper) -> Tank:
        return Tank.create("tank2", 110, tank_helper)

    def test_pour_water(self, tank1: Tank):
        tank1.pour_water(10)
        assert tank1.current_volume == 10

    def test_pour_water_exceeds_capacity(
            self, tank1: Tank
    ):
        assert not tank1.pour_water(110)

    def test_pour_out_water(self, tank1: Tank):
        tank1.pour_water(10)
        tank1.pour_out_water(10)
        assert tank1.current_volume == 0

    def test_pour_out_water_exceeds_current_volume(
            self, tank1: Tank
    ):
        tank1.pour_water(10)
        assert not tank1.pour_out_water(20)