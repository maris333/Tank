from src.logger import Logger
from src.tank_operations import TankOperations


class Tank:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
        self._current_volume = 0

    @property
    def name(self):
        return self._name

    @property
    def capacity(self):
        return self._capacity

    @property
    def current_volume(self):
        return self._current_volume

    @current_volume.setter
    def current_volume(self, value):
        self._current_volume = value

    def pour_water(self, volume: int, tank_operations: TankOperations) -> bool:
        if self.current_volume + volume > self.capacity:
            print(f"{self.name.title()} capacity exceeded")
            Logger.pour_water(volume, self, False, tank_operations)
            return False
        self.current_volume += volume
        Logger.pour_water(volume, self, True, tank_operations)
        print(f"{self.name.title()} has {self.current_volume} water")
        return True

    def pour_out_water(self, volume: int, tank_operations: TankOperations) -> bool:
        if self.current_volume < volume:
            print(f"{self.name.title()} does not have enough water")
            Logger.pour_out_water(volume, self, False, tank_operations)
            return False
        self.current_volume -= volume
        Logger.pour_out_water(volume, self, True, tank_operations)
        print(f"{self.name.title()} has {self.current_volume} water")
        return True

    def transfer_water(
            self, from_tank: "Tank", volume: int, tank_operations: TankOperations
    ) -> bool:
        if from_tank.current_volume < volume:
            print(f"{from_tank.name.title()} does not have enough water")
            Logger.transfer_water(volume, self, False, tank_operations)
            return False
        if self.current_volume + volume > self.capacity:
            print(f"{self.name.title()} capacity exceeded")
            Logger.transfer_water(volume, self, False, tank_operations)
            return False
        from_tank.current_volume -= volume
        self.current_volume += volume
        Logger.transfer_water(volume, self, True, tank_operations)
        print(f"{volume} water poured from {from_tank.name} to {self.name}")
        return True
