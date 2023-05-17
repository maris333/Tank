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
                  f" {list(filter(lambda key: tanks.get(key) == max(tanks.values()), tanks))}")
            return list(filter(lambda key: tanks.get(key) == max(tanks.values()), tanks))
        return []

    def get_tanks_with_most_operations_of_type(self, operation_name: str) -> List:
        tanks: Dict[str, int] = {}
        tanks = {op.tank: tanks.get(op.tank, 0) + 1 for op in self.operations if op.name == operation_name}
        if tanks:
            print(f"List of tanks with most operations of type {operation_name}: "
                  f"{list(filter(lambda key: tanks.get(key) == max(tanks.values()), tanks))}")
            return list(filter(lambda key: tanks.get(key) == max(tanks.values()), tanks))
        return []

    def check_state(self, tank_name: str) -> int:
        operation = next(filter(lambda op: op.tank == tank_name or (hasattr(op, "to_tank") and op.to_tank == tank_name),
                                reversed(self.operations)), None)
        return operation.volume if operation is not None else 0
