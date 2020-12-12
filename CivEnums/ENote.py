from enum import Enum


class ENote(Enum):

    def __init__(self, s):
        self.sign = s

    NONE = " "
    KAPITOL_SUGGESTION = "k"
    COTTAGE = "c"
    BARBARIAN = "b"
    RESOURCE = "r"

    def getSign(self):
        return self.sign
