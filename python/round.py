from ast import And
import logging


from knight import Knight
from util import knight_hit

class Round:
    def __init__(self, knights: list):
        self.knights = knights.copy()

    def play_round(self):
        knight_pointer = 0
        logging.info(" Round start ")
        while len(self.knights) > 1:
            list_length = len(self.knights)
            next_knight = (knight_pointer + 1) % list_length
            self._fight_knights(self.knights[knight_pointer], self.knights[next_knight])
            knight_pointer = next_knight % len(self.knights)
        winner_knight = self.knights[0]
        winner_knight.increase_win()
        logging.info(f" Round end Knight {winner_knight.name} wins!! ")

    def _fight_knights(self, attacker: Knight, defender: Knight):
        if knight_hit(attacker):
            logging.debug(f'Knight {attacker.name} killed Knight {defender.name}')
            self.knights.remove(defender)
        else:
            logging.debug(f'Knight {attacker.name} missed!')
