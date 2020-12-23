from CivEnums.ECivilization import ECivilization
from CivEnums.EPolity import EPolity
from CivEnums.ERotation import ERotation
from CivObjects.Position import Position
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing.EImageObject import EImageObject
from Drawing.ImgInfoPolity import ImgInfoPolity


"""
this class handles the polity of civilizations
draw functions are implemented
"""


class PolityOfCivilizations:

    def __init__(self):
        self.imgInfo = ImgInfoPolity()
        self.drawPolityOfCiv = None
        self.drawIdx = 0
        self.polityArr = []
        self.polityOfCivilizationsArr = []

        self.allPolitiesArr = []
        self.allPolitiesArr.append(EPolity.ANARCHY)
        self.allPolitiesArr.append(EPolity.COMMUNISM)
        self.allPolitiesArr.append(EPolity.DEMOCRACY)
        self.allPolitiesArr.append(EPolity.DESPOTISM)
        self.allPolitiesArr.append(EPolity.FEUDALISM)
        self.allPolitiesArr.append(EPolity.FUNDAMENTALISM)
        self.allPolitiesArr.append(EPolity.MONARCHY)
        self.allPolitiesArr.append(EPolity.REPUBLIC)

    def setCivForDrawing(self, civ):
        self.drawPolityOfCiv = civ

    def addCivPolity(self, civPolity):
        self.polityOfCivilizationsArr.append(civPolity)

    def draw(self, window):
        if self.drawPolityOfCiv is None:
            return False
        print("here2")
        self.drawIdx = 0
        self.polityArr = []
        for pc in self.polityOfCivilizationsArr:
            if pc.getCivilizationEnum() is self.drawPolityOfCiv:
                self.drawPolity(window, pc.getPolity())
                if pc.getPolity() is not EPolity.ANARCHY:
                    self.drawPolity(window, EPolity.ANARCHY)
                    polity = pc.getPreviouslyUnlockedPolity()
                    if polity is not None:
                        self.drawPolity(window, polity)
                else:
                    possiblePolities = pc.getPossiblePolities()
                    for polity in possiblePolities:
                        self.drawPolity(window, polity)
                for polity in self.allPolitiesArr:
                    polityIsDrawn = False
                    for drawnPol in self.polityArr:
                        if polity is drawnPol:
                            polityIsDrawn = True
                    if not polityIsDrawn:
                        self.drawPolity(window, polity)

    def drawPolity(self, window, polity):
        pos = self.imgInfo.getImgPosOf(EImageObject.POLITY_ZOOMED, self.drawIdx % 4, self.drawIdx // 4)
        resize = EImageObject.POLITY_ZOOMED.getResize()
        DrawCivObjects.drawImage(ImageHandler.getImageOfPolity(polity), window,
                                 ERotation.NO_ROTATION, pos, resize, 1)
        self.drawIdx = self.drawIdx + 1
        self.polityArr.append(polity)
