from operator import attrgetter
from typing import List

from src.tank import Tank


class TankHelper:
    def __init__(self):
        self._list_of_tanks: List[Tank] = []

    @property
    def list_of_tanks(self):
        return self._list_of_tanks

    def append_to_list(self, list_of_tanks: List[Tank]) -> None:
        for tank in list_of_tanks:
            self.list_of_tanks.append(tank)

    def get_most_filled_tank(self) -> Tank:
        return max(self.list_of_tanks, key=attrgetter("current_volume"))

    def get_empty_tanks(self) -> List:
        list_of_tanks = []
        for tank in self.list_of_tanks:
            if tank.current_volume == 0:
                list_of_tanks.append(tank)
        return list_of_tanks
