from typing import Dict, List

from src.event import Event


class TankOperations:
    def __init__(self):
        self._operations: List[Event] = []

    @property
    def operations(self) -> List:
        return self._operations

    @operations.setter
    def operations(self, value) -> None:
        self._operations = value

    @operations.getter
    def operations(self) -> List:
        return self._operations

    def get_tanks_with_most_failed_operations(self) -> List:
        tanks: Dict[str, int] = {}
        tanks = {op.tank: tanks.get(op.tank, 0) + 1 for op in self.operations if op.success is False}
        if tanks:
            print(f"List of tanks with most failed operations:"
                  f" {[key for key, value in tanks.items() if value == max(tanks.values())]}")
            return [key for key, value in tanks.items() if value == max(tanks.values())]
        return []

    def get_tanks_with_most_operations_of_type(self, operation_name: str) -> List:
        tanks: Dict[str, int] = {}
        tanks = {op.tank: tanks.get(op.tank, 0) + 1 for op in self.operations if op.name == operation_name}
        if tanks:
            print(f"List of tanks with most operations of type {operation_name}: "
                  f"{[key for key, value in tanks.items() if value == max(tanks.values())]}")
            return [key for key, value in tanks.items() if value == max(tanks.values())]
        return []

    def check_state(self, tank_name: str) -> int:
        return next((op.volume if op.tank == tank_name
                    else op.to_tank_volume if hasattr(op, "to_tank") and op.to_tank == tank_name
                    else 0
                    for op in reversed(self.operations)), 0)
