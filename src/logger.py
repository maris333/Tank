from datetime import datetime

from src.tank_operations import TankOperations


class Logger:
    @staticmethod
    def pour_water(volume: int, tank, value: bool, tank_operations: TankOperations) -> None:
        tank_operations.operations.append(
            {
                "date": datetime.now(),
                "name": "pour_water",
                "tank": tank.name,
                "volume": volume,
                "success": value,
            }
        )

    @staticmethod
    def pour_out_water(volume: int, tank, value: bool, tank_operations: TankOperations) -> None:
        tank_operations.operations.append(
            {
                "date": datetime.now(),
                "name": "pour_out_water",
                "tank": tank.name,
                "volume": volume,
                "success": value,
            }
        )

    @staticmethod
    def transfer_water(volume: int, tank, value: bool, tank_operations: TankOperations) -> None:
        tank_operations.operations.append(
            {
                "date": datetime.now(),
                "name": "transfer_water",
                "tank": tank.name,
                "volume": volume,
                "success": value,
            }
        )
