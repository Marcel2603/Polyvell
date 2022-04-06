from argparse import ArgumentError

import logging
from knight import Knight
from round import Round


class Tournament:
    def __init__(self) -> None:
        self.rounds = 0
        self.knights = []

    def start(self):
        self.knights = self._load_knights()
        self.rounds = self._get_rounds()

        for i in range(self.rounds):
            round = Round(self.knights)
            round.play_round()
        self.print_result(self.knights)
    
    def print_result(self, knights):
        logging.warn(" Result ")
        for knight in knights:
            logging.warn(f'Knight {knight.name}: {knight.wins} Wins')

    def _get_hit_probality(self, knight_number):
        hit_probality = float(
            input(f'Insert Hit Probality for Knight {knight_number}: '))
        if 0.0 <= hit_probality <= 1.0:
            return hit_probality
        else:
            raise ArgumentError

    def _load_knights(self) -> list:
        amount = int(input('How many Knights to create? '))
        knights = []
        for i in range(amount):
            hit_probality = self._get_hit_probality(i)
            knights.append(Knight(i, hit_probality))
        return sorted(knights, key=lambda knight: knight.hit_probality)

    def _get_rounds(self) -> int:
        return int(input("How many rounds (Enter for default) : ") or "1")
