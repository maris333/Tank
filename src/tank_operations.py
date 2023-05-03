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
        for op in self.operations:
            self._get_tanks_with_most_failed_operations_checker(op, tanks)
        if tanks:
            max_value = max(tanks.values())
            print(f"List of tanks with most failed operations:"
                  f" {[key for key, value in tanks.items() if value == max_value]}")
            return [key for key, value in tanks.items() if value == max_value]
        return []

    @staticmethod
    def _get_tanks_with_most_failed_operations_checker(op: any, tanks: Dict) -> None:
        if not op.success:
            tank_name = op.tank
            if tank_name in tanks:
                tanks[tank_name] += 1
            else:
                tanks[tank_name] = 1

    def get_tanks_with_most_operations_of_type(self, operation_name: str) -> List:
        tanks: Dict[str, int] = {}
        for op in self.operations:
            self._get_tanks_with_most_operations_of_type_checker(op, operation_name, tanks)
        if tanks:
            max_value = max(tanks.values())
            print(f"List of tanks with most operations of type {operation_name}: "
                  f"{[key for key, value in tanks.items() if value == max_value]}")
            return [key for key, value in tanks.items() if value == max_value]
        return []

    @staticmethod
    def _get_tanks_with_most_operations_of_type_checker(op: any, operation_name: str, tanks: Dict) -> None:
        if op.name == operation_name:
            tank_name = op.tank
            if tank_name in tanks:
                tanks[tank_name] += 1
            else:
                tanks[tank_name] = 1

    def check_state(self, tank_name: str) -> int:
        result = 0
        for op in self.operations:
            if op.tank == tank_name:
                result = op.volume
            if hasattr(op, "to_tank"):
                if op.to_tank == tank_name:
                    result = op.to_tank_volume
        return result

