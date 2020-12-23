import pygame

from CivEnums.ERotation import ERotation
from CivObjects.Position import Position


"""
with this class, it is possible to draw any 2D object image or figures
arguments of functions are
* image
* window
* position of image
* scale and resize factor of image
* rotation
* additional dx, dy
"""


class DrawCivObjects:

    @classmethod
    def drawSquareObject(cls, img, window, pos, resize, scale):
        cls.drawImage(img, window, ERotation.NO_ROTATION, pos, resize, scale)

    @classmethod
    def drawFigureOnSquare(cls, img, window, pos, resize, scale, dx, dy):
        x = pos.getX() + dx
        y = pos.getY() + dy
        imgPos = Position(x, y)
        cls.drawImage(img, window, ERotation.NO_ROTATION, imgPos, resize, scale)

    @classmethod
    def drawImage(cls, img, window, rotation, pos, resize, scale):
        w = int(img.get_width() * resize * scale)
        h = int(img.get_height() * resize * scale)
        manImg = pygame.transform.scale(img, (w, h))
        if isinstance(rotation, ERotation):
            if rotation is ERotation.CLOCKWISE_90:
                manImg = pygame.transform.rotate(manImg, 270)
            elif rotation is ERotation.CLOCKWISE_180:
                manImg = pygame.transform.rotate(manImg, 180)
            elif rotation is ERotation.CLOCKWISE_270:
                manImg = pygame.transform.rotate(manImg, 90)
            window.blit(manImg, (pos.getX() * scale, pos.getY() * scale))
        else:
            size_orig = manImg.get_rect()
            manImg = pygame.transform.rotate(manImg, rotation)
            size_rot = manImg.get_rect()
            window.blit(manImg, ((pos.getX() - size_rot.center[0] + size_orig.center[0]) * scale,
                                 (pos.getY() - size_rot.center[1] + size_orig.center[1]) * scale))
