from enum import Enum


class ERotation(Enum):

    def __init__(self, rot):
        self.rotation = rot

    NO_ROTATION = 0
    CLOCKWISE_90 = 1
    CLOCKWISE_180 = 2
    CLOCKWISE_270 = 3

    def getRotation(self):
        return self.rotation
