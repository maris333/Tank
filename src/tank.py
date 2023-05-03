from src.tank_helper import TankHelper


class Tank:
    __create_key = object()

    @classmethod
    def create(cls, name: str, capacity: int, tank_helper: TankHelper):
        tank = Tank(cls.__create_key, name, capacity)
        tank_helper.list_of_tanks.append(tank)
        return tank

    def __init__(self, create_key, name, capacity):
        assert (create_key == Tank.__create_key)
        self._name: str = name
        self._capacity: int = capacity
        self._current_volume: int = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def current_volume(self) -> int:
        return self._current_volume

    @current_volume.setter
    def current_volume(self, value) -> None:
        self._current_volume = value

    @current_volume.getter
    def current_volume(self) -> int:
        return self._current_volume

    def pour_water(self, volume: int) -> bool:
        if self.current_volume + volume > self.capacity:
            print(f"{self.name.title()} capacity exceeded")
            return False
        self.current_volume += volume
        print(f"{self.name.title()} has {self.current_volume} water")
        return True

    def pour_out_water(self, volume: int) -> bool:
        if self.current_volume < volume:
            print(f"{self.name.title()} does not have enough water")
            return False
        self.current_volume -= volume
        print(f"{self.name.title()} has {self.current_volume} water")
        return True

    def transfer_water(
            self, to_tank: "Tank", volume: int
    ) -> bool:
        if self.current_volume < volume:
            print(f"{self.name.title()} does not have enough water")
            return False
        if to_tank.current_volume + volume > to_tank.capacity:
            print(f"{to_tank.name.title()} capacity exceeded")
            return False
        self.current_volume -= volume
        to_tank.current_volume += volume
        print(f"{volume} water poured from {self.name} to {to_tank.name}")
        return True
