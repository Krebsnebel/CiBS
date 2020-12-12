from enum import Enum


class EResource(Enum):

    def __init__(self, s):
        self.sign = s

    NONE = " "
    GOLD = "c"
    SILK = "s"
    IRON = "e"
    WHEAT = "w"
    INCENSE = "r"
    GREAT_PERSON = "g"
    SPY = "o"
    URANIUM = "u"

    def getSign(self):
        return self.sign
