from operator import attrgetter


class TankHelper:
    list_of_tanks = []
    operations = []

    @staticmethod
    def get_most_filled_tank():
        return max(TankHelper.list_of_tanks, key=attrgetter('current_volume'))

    @staticmethod
    def get_empty_tanks():
        list_of_tanks = []
        for tank in TankHelper.list_of_tanks:
            if tank.current_volume == 0:
                list_of_tanks.append(tank)
        return list_of_tanks

    @staticmethod
    def get_tank_with_most_failed_operations():
        tanks = {}
        for op in TankHelper.operations:
            if not op['success']:
                tank_name = op['tank']
                if tank_name in tanks:
                    tanks[tank_name] += 1
                else:
                    tanks[tank_name] = 1
        if not tanks:
            return None
        return max(tanks, key=tanks.get)

    @staticmethod
    def get_tank_with_most_operations_of_type(operation_name):
        tanks = {}
        for op in TankHelper.operations:
            if op['name'] == operation_name:
                tank_name = op['tank']
                if tank_name in tanks:
                    tanks[tank_name] += 1
                else:
                    tanks[tank_name] = 1
        if not tanks:
            return None
        return max(tanks, key=tanks.get)
