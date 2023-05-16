from operator import attrgetter
from typing import List


class TankHelper:

    def __init__(self):
        self._list_of_tanks: List[any] = []

    @property
    def list_of_tanks(self) -> List:
        return self._list_of_tanks

    def get_most_filled_tanks(self) -> List:
        max_value = max(self.list_of_tanks, key=lambda x: x.current_volume / x.capacity)
        return [value for value in self.list_of_tanks if value == max_value]

    def get_tanks_with_most_water(self) -> List:
        max_value = max(self.list_of_tanks, key=attrgetter("current_volume"))
        return [value for value in self.list_of_tanks if value == max_value]

    def get_empty_tanks(self) -> List:
        return [tank for tank in self.list_of_tanks if tank.current_volume == 0]
