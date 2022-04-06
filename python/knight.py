from dataclasses import dataclass
from importlib_metadata import re


@dataclass
class Knight:
    name: str
    hit_probality: float
    wins: int = 0

    def increase_win(self):
        self.wins += 1
