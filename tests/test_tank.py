import pytest as pytest

from tank import Tank
from tank_helper import TankHelper


class TestTank:

    @pytest.fixture
    def tank1(self):
        return Tank.create_instance("tank1", 100)

    @pytest.fixture
    def tank2(self):
        return Tank.create_instance("tank2", 110)

    def test_create_instance_adds_tank_to_list(self, tank1):
        tank = tank1
        assert len(TankHelper.list_of_tanks) == 1

    def test_pour_water(self, tank1):
        tank1.pour_water(10)
        assert tank1.current_volume == 10

    def test_pour_water_exceeds_capacity(self, tank1):
        assert not tank1.pour_water(110)

    def test_pour_out_water(self, tank1):
        tank1.pour_water(10)
        tank1.pour_out_water(10)
        assert tank1.current_volume == 0

    def test_pour_out_water_exceeds_current_volume(self, tank1):
        tank1.pour_water(10)
        assert not tank1.pour_out_water(20)

    def test_transfer_water(self, tank1, tank2):
        tank2.pour_water(10)
        tank1.transfer_water(tank2, 10)
        assert tank1.current_volume == 10
        assert tank2.current_volume == 0

    def test_transfer_water_tank2_has_not_enough_water(self, tank1, tank2):
        tank2.pour_water(10)
        assert not tank1.transfer_water(tank2, 20)

    def test_transfer_water_tank1_capacity_exceeded(self, tank1, tank2):
        tank2.pour_water(110)
        assert not tank1.transfer_water(tank2, 110)

    def test_get_most_filled_tank(self, tank1, tank2):
        tank1.pour_water(10)
        tank2.pour_water(20)
        assert TankHelper.get_most_filled_tank() == tank2

    def test_get_most_filled_tank_returns_two_or_more(self, tank1, tank2):
        tank1.pour_water(10)
        tank2.pour_water(20)
        assert TankHelper.get_most_filled_tank() == [tank1, tank2]

    def test_get_empty_tanks(self, tank1, tank2):
        assert len(TankHelper.get_empty_tanks()) == 2

    def test_get_tank_with_most_failed_operations(self, tank1, tank2):
        tank1.pour_water(110)
        tank2.pour_water(100)
        tank1.pour_out_water(100)
        assert TankHelper.get_tank_with_most_failed_operations() == tank1.name

    def test_get_tank_with_most_failed_operations_returns_two_or_more(self, tank1, tank2):
        tank1.pour_water(110)
        tank2.pour_water(110)
        tank1.pour_out_water(110)
        tank2.pour_out_water(110)
        assert TankHelper.get_tank_with_most_failed_operations() == [tank1.name, tank2.name]

    def test_get_tank_with_most_operations_of_type(self, tank1, tank2):
        tank1.pour_water(110)
        tank2.pour_water(100)
        tank1.pour_out_water(100)
        assert TankHelper.get_tank_with_most_failed_operations() == tank1.name

    def test_get_tank_with_most_operations_of_type_returns_two_or_more(self, tank1, tank2):
        tank1.pour_water(110)
        tank2.pour_water(100)
        tank1.pour_out_water(100)
        tank2.pour_out_water(100)
        assert TankHelper.get_tank_with_most_failed_operations() == [tank1.name, tank2.name]
