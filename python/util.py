from random import random
from knight import Knight

def knight_hit(knight: Knight) -> bool:
    rand = random()

    return rand < knight.hit_probality