from enum import Enum


class EColor(Enum):

    def __init__(self, lab):
        self.label = lab

    def __str__(self):
        return self.label

    WHITE = "White"
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    YELLOW = "Yellow"
    NO_COLOR = "NoColor"
