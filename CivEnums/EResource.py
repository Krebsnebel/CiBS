from enum import Enum


class EResource(Enum):

    def __init__(self, s):
        self.sign = s

    NONE = " "
    COIN = "c"
    SILK = "s"
    IRON = "e"
    WHEAT = "w"
    INCENSE = "r"
    GREAT_PERSON = "g"
    SPY = "o"
    URANIUM = "u"
    CULTURE = "a"
    HIT = "h"

    def getSign(self):
        return self.sign
