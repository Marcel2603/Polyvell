from dataclasses import dataclass


@dataclass
class Knight:
    name: str
    hit_probality: float
    wins: int = 0

    def increase_win(self):
        self.wins += 1
