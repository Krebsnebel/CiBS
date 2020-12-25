from enum import Enum


class EOptionStatus(Enum):
    LOCKED = 1
    UNLOCKED_BUT_NOT_AVAILABLE = 2
    NOT_AVAILABLE = 3
    AVAILABLE = 4
    ACTIVE = 5
