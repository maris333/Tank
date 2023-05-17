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
        return list(filter(lambda tank: tank.current_volume == max_value, self.list_of_tanks))

    def get_tanks_with_most_water(self) -> List:
        max_value = max(self.list_of_tanks, key=attrgetter("current_volume"))
        return list(filter(lambda tank: tank.current_volume == max_value, self.list_of_tanks))

    def get_empty_tanks(self) -> List:
        return list(filter(lambda tank: tank.current_volume == 0, self.list_of_tanks))
