from enum import Enum


class EStatusPolity(Enum):
    LOCKED = 1
    UNLOCKED_BUT_NOT_AVAILABLE = 2
    UNLOCKED_AND_AVAILABLE = 4
    ACTIVE = 5
