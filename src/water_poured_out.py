from dataclasses import dataclass
from datetime import datetime

from src.event import Event


@dataclass
class WaterPouredOut(Event):
    date = datetime.now()
    name = "pour_out_water"
    tank: str
    amount: int
    success: bool
    volume: int
