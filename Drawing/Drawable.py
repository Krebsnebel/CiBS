import pygame

from CivEnums.ERefPoint import ERefPoint
from CivObjects.Position import Position


class Drawable:

    def __init__(self, img, imgConst, imgDetail, cardNr, mapPos):
        self.img = img
        self.imgConst = imgConst
        self.imgDetail = imgDetail
        self.cardNr = cardNr
        self.mapPos = mapPos
        self.rotation = 0
        self.visible = False
        self.resize = imgConst.getResize()
        self.imgPos = Position(0, 0)
        self.changeCurrImgPos()

    def setCardNr(self, cardNr):
        self.cardNr = cardNr
        self.changeCurrImgPos()

    def changeCurrImgPos(self):
        imgDetPos = self.imgDetail.getPosOf(ERefPoint.TOP_LEFT, False, False)
        self.resize = self.imgConst.getResize()
        imgX = imgDetPos.getX() + self.imgConst.getX() + self.mapPos.getX() * self.imgConst.getDx()
        imgX = imgX + self.cardNr * self.imgConst.getStackDx()
        imgY = imgDetPos.getY() + self.imgConst.getY() + self.mapPos.getY() * self.imgConst.getDy()
        imgY = imgY + self.cardNr * self.imgConst.getStackDy()
        self.imgPos.setPosition(imgX, imgY)

    def setVisibility(self, visible):
        self.visible = visible

    def setImg(self, img):
        self.img = img

    def draw(self, window):
        scale = self.imgDetail.getScale()
        shiftX = self.imgDetail.getShiftX()
        shiftY = self.imgDetail.getShiftY()
        w = int(self.img.get_width() * self.resize * scale)
        h = int(self.img.get_height() * self.resize * scale)
        manImg = pygame.transform.scale(self.img, (w, h))
        size_orig = manImg.get_rect()
        manImg = pygame.transform.rotate(manImg, self.rotation)
        size_rot = manImg.get_rect()
        window.blit(manImg, ((self.imgPos.getX() + shiftX - size_rot.center[0] + size_orig.center[0]) * scale,
                             (self.imgPos.getY() + shiftY - size_rot.center[1] + size_orig.center[1]) * scale))


