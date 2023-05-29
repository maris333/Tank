from dataclasses import dataclass
from datetime import datetime

from src.event import Event


@dataclass
class WaterTransferred(Event):
    date = datetime.now()
    name = "transfer_water"
    tank: str
    volume: int
    to_tank: str
    to_tank_volume: int
    tank_capacity: int
    to_tank_capacity: int
    amount: int
    success: bool
