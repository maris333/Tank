from datetime import datetime

from tank_helper import TankHelper


class Tank:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.current_volume = 0

    @classmethod
    def create_instance(cls, name, capacity):
        tank = cls(name, capacity)
        TankHelper.list_of_tanks.append(tank)
        return tank

    def pour_water(self, volume):
        if self.current_volume + volume > self.capacity:
            print("{} capacity exceeded".format(self.name.title()))
            TankHelper.operations.append(
                {
                    "date": datetime.now(),
                    "name": "pour_water",
                    "tank": self.name,
                    "volume": volume,
                    "success": False
                }
            )
            return False
        self.current_volume += volume
        TankHelper.operations.append(
            {
                "date": datetime.now(),
                "name": "pour_water",
                "tank": self.name,
                "volume": volume,
                "success": True
            }
        )
        print("{} has {} water".format(self.name.title(), self.current_volume))
        return True

    def pour_out_water(self, volume):
        if self.current_volume < volume:
            print("{} does not have enough water".format(self.name.title()))
            TankHelper.operations.append(
                {
                    "date": datetime.now(),
                    "name": "pour_out_water",
                    "tank": self.name,
                    "volume": volume,
                    "success": False
                }
            )
            return False
        self.current_volume -= volume
        TankHelper.operations.append(
            {
                "date": datetime.now(),
                "name": "pour_out_water",
                "tank": self.name,
                "volume": volume,
                "success": True
            }
        )
        print("{} has {} water".format(self.name.title(), self.current_volume))
        return True

    def transfer_water(self, from_tank, volume):
        if from_tank.current_volume < volume:
            print("{} does not have enough water".format(from_tank.name.title()))
            TankHelper.operations.append(
                {
                    "date": datetime.now(),
                    "name": "transfer_water",
                    "tank": self.name,
                    "volume": volume,
                    "success": False,
                }
            )
            return False
        if self.current_volume + volume > self.capacity:
            print("{} capacity exceeded".format(self.name.title()))
            TankHelper.operations.append(
                {
                    "date": datetime.now(),
                    "name": "transfer_water",
                    "tank": self.name,
                    "volume": volume,
                    "success": False,
                }
            )
            return False
        from_tank.current_volume -= volume
        self.current_volume += volume
        TankHelper.operations.append(
            {
                "date": datetime.now(),
                "name": "transfer_water",
                "tank": self.name,
                "volume": volume,
                "success": True,
            }
        )
        print("{} water poured from {} to {}".format(volume, from_tank.name, self.name))
        return True
