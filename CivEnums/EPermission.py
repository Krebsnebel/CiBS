from enum import Enum


class EPermissionTerrain(Enum):
    ALL_EXCEPT_WATER = 0
    ALL_EXCEPT_WATER_AND_MOUNTAIN = 1
    ONLY_GRASSLAND = 2
    ONLY_MOUNTAIN = 3
    ONLY_WATER = 4
    ONLY_DESERT = 5
    ONLY_FOREST = 6
    MOVE_OVER_WATER = 7
    STOP_ON_WATER = 8
