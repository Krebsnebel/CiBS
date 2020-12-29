from enum import Enum


class ERotation(Enum):

    def __init__(self, rot):
        self.rotation = rot

    NO_ROTATION = 0
    CLOCKWISE_90 = 270
    CLOCKWISE_180 = 180
    CLOCKWISE_270 = 90

    def getRotation(self):
        return self.rotation
