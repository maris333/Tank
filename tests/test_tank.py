import pytest as pytest
from src.tank import Tank
from src.tank_operations import TankOperations


class TestTank:
    @pytest.fixture
    def tank_operations(self):
        return TankOperations()

    @pytest.fixture
    def tank1(self):
        return Tank("tank1", 100)

    @pytest.fixture
    def tank2(self):
        return Tank("tank2", 110)

    def test_pour_water(self, tank1: Tank, tank_operations: TankOperations):
        tank1.pour_water(10, tank_operations)
        assert tank1.current_volume == 10

    def test_pour_water_exceeds_capacity(
        self, tank1: Tank, tank_operations: TankOperations
    ):
        assert not tank1.pour_water(110, tank_operations)

    def test_pour_out_water(self, tank1: Tank, tank_operations: TankOperations):
        tank1.pour_water(10, tank_operations)
        tank1.pour_out_water(10, tank_operations)
        assert tank1.current_volume == 0

    def test_pour_out_water_exceeds_current_volume(
        self, tank1: Tank, tank_operations: TankOperations
    ):
        tank1.pour_water(10, tank_operations)
        assert not tank1.pour_out_water(20, tank_operations)

    def test_transfer_water(
        self, tank1: Tank, tank2: Tank, tank_operations: TankOperations
    ):
        tank2.pour_water(10, tank_operations)
        tank1.transfer_water(tank2, 10, tank_operations)
        assert tank1.current_volume == 10
        assert tank2.current_volume == 0

    def test_transfer_water_tank2_has_not_enough_water(
        self, tank1: Tank, tank2: Tank, tank_operations: TankOperations
    ):
        tank2.pour_water(10, tank_operations)
        assert not tank1.transfer_water(tank2, 20, tank_operations)

    def test_transfer_water_tank1_capacity_exceeded(
        self, tank1: Tank, tank2: Tank, tank_operations: TankOperations
    ):
        tank2.pour_water(105, tank_operations)
        assert not tank1.transfer_water(tank2, 105, tank_operations)
