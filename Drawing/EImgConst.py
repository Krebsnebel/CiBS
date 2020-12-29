from enum import Enum


class EImgConst(Enum):

    def __init__(self, x, y, dx, dy, shiftX, shiftY, stackDx, stackDy, resize):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.stackDx = stackDx
        self.stackDy = stackDy
        self.shiftX = shiftX
        self.shiftY = shiftY
        self.resize = resize

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDx(self):
        return self.dx

    def getDy(self):
        return self.dy

    def getStackDx(self):
        return self.stackDx

    def getStackDy(self):
        return self.stackDy

    def getResize(self):
        return self.resize

    #                          x,      y,     dx,     dy, shiftX, shiftY,stackDx,stackDy,   resize
    MMAP_MILITARY_UNIT = (1045.0,   38.0,  248.0,  218.0,    0.0,    0.0,    1.0,   -1.0, 132.0 / 1125.0)
