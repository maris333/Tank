from src.tank import Tank
from src.tank_operations import TankOperations
from src.water_poured import WaterPoured
from src.water_poured_out import WaterPouredOut
from src.water_transferred import WaterTransferred


class EventSourcer:

    def __init__(self, tank_operations: TankOperations):
        self.tank_operations = tank_operations

    def water_poured(self, amount: int, tank: Tank, value: bool) -> None:
        self.tank_operations.operations.append(WaterPoured(tank.name, amount, value, tank.current_volume))

    def water_poured_out(self, amount: int, tank: Tank, value: bool) -> None:
        self.tank_operations.operations.append(WaterPouredOut(tank.name, amount, value, tank.current_volume))

    def water_transferred(self, volume: int, to_tank: Tank, tank: Tank, value: bool) -> None:
        self.tank_operations.operations.append(WaterTransferred(tank.name, tank.current_volume, to_tank.name,
                                                                to_tank.current_volume, tank.capacity,
                                                                to_tank.capacity, volume, value))
