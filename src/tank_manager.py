from src.event_sourcer import EventSourcer
from src.tank import Tank
from src.tank_helper import TankHelper
from src.tank_operations import TankOperations


class TankManager:
    def __init__(self, tank_helper: TankHelper, tank_operations: TankOperations, event_sourcer: EventSourcer):
        self.tank_helper = tank_helper
        self.tank_operations = tank_operations
        self.event_sourcer = event_sourcer

    def _get_tank(self, tank_name: str) -> Tank:
        return next(filter(lambda tank: tank.name == tank_name, self.tank_helper.list_of_tanks), None)

    def pour_water(self, tank_name: str, volume: int) -> None:
        if not self._get_tank(tank_name).pour_water(volume):
            self.event_sourcer.water_poured(volume, self._get_tank(tank_name), False)
        self.event_sourcer.water_poured(volume, self._get_tank(tank_name), True)

    def pour_out_water(self, tank_name: str, volume: int) -> None:
        if not self._get_tank(tank_name).pour_out_water(volume):
            self.event_sourcer.water_poured_out(volume, self._get_tank(tank_name), False)
        self.event_sourcer.water_poured_out(volume, self._get_tank(tank_name), True)

    def transfer_water(self, tank_name: str, to_tank: str, volume: int) -> None:
        if not (self._get_tank(tank_name).pour_out_water(volume) | self._get_tank(to_tank).pour_water(volume)):
            self.event_sourcer.water_transferred(volume, self._get_tank(to_tank), self._get_tank(tank_name), False)
        self.event_sourcer.water_transferred(volume, self._get_tank(to_tank), self._get_tank(tank_name), True)

