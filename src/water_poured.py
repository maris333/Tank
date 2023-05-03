from dataclasses import dataclass
from datetime import datetime

from src.event import Event


@dataclass
class WaterPoured(Event):
    date = datetime.now()
    name = "pour_water"
    tank: str
    amount: int
    success: bool
    volume: int
