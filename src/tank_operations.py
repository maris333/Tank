from datetime import datetime
from typing import Dict, List


class TankOperations:
    def __init__(self):
        self._operations: List[Dict[str, any]] = []

    @property
    def operations(self):
        return self._operations

    def get_tank_with_most_failed_operations(self):
        tanks: Dict[str, int] = {}
        for op in self.operations:
            if not op["success"]:
                tank_name = op["tank"]
                if tank_name in tanks:
                    tanks[tank_name] += 1
                else:
                    tanks[tank_name] = 1
        if tanks:
            return max(tanks, key=lambda x: x[1])
        return None

    def get_tank_with_most_operations_of_type(self, operation_name: str):
        tanks: Dict[str, int] = {}
        for op in self.operations:
            if op["name"] == operation_name:
                tank_name = op["tank"]
                if tank_name in tanks:
                    tanks[tank_name] += 1
                else:
                    tanks[tank_name] = 1
        if tanks:
            return max(tanks, key=lambda x: x[1])
        return None
