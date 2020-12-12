from enum import Enum


class EGameSection(Enum):
    IDLE = 0
    PREPARE_GAME = 1
    START_ROUND = 2
    TRADE = 3
    CITY_ADMINISTRATION = 4
    MOVEMENT = 5
    RESEARCH = 6
