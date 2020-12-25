from CivEnums.EPolity import EPolity
from CivEnums.ERotation import ERotation
from CivObjects.Polity import Polity
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing.EImageObject import EImageObject
from Drawing.ImgInfoPolity import ImgInfoPolity
from Options.EOptionType import EOptionType
from Options.Option import Option

"""
this class handles the polity of civilizations
draw functions are implemented
"""


class PolityOfCivilizations:

    def __init__(self):
        self.imgInfo = ImgInfoPolity()
        self.drawPolityOfCiv = None
        self.drawIdx = 0
        self.options = []
        self.civPolityArr = []

        self.allPolitiesArr = []
        self.allPolitiesArr.append(EPolity.ANARCHY)
        self.allPolitiesArr.append(EPolity.COMMUNISM)
        self.allPolitiesArr.append(EPolity.DEMOCRACY)
        self.allPolitiesArr.append(EPolity.DESPOTISM)
        self.allPolitiesArr.append(EPolity.FEUDALISM)
        self.allPolitiesArr.append(EPolity.FUNDAMENTALISM)
        self.allPolitiesArr.append(EPolity.MONARCHY)
        self.allPolitiesArr.append(EPolity.REPUBLIC)

    def setOptions(self, pol, c1, c2):
        self.options = []
        self.setOption(pol, EImageObject.POLITY)
        self.setOption(c1, EImageObject.CITY_1)
        self.setOption(c2, EImageObject.CITY_2)

    def setOption(self, cond, imgObj):
        if cond:
            imgPos = self.getImgPosOf(imgObj, False, False)
            self.options.append(Option(imgObj, imgPos.getX(), imgPos.getY(), EOptionType.SQUARE, self.emphasize, None))

    def setOptions(self, civ):
        self.drawPolityOfCiv = civ
        self.options = []
        if civ is None:
            return
        for pc in self.civPolityArr:
            if pc.getCivilizationEnum() is self.drawPolityOfCiv:
                self.polityArr.append(Polity(pc.getPolity(), EStatusPolity.ACTIVE))
                if pc.getPolity() is not EPolity.ANARCHY:
                    polity = pc.getPreviouslyUnlockedPolity()
                    if polity is not None:
                        self.polityArr.append(Polity(polity, EStatusPolity.UNLOCKED_AND_AVAILABLE))
                    self.polityArr.append(Polity(EPolity.ANARCHY, EStatusPolity.UNLOCKED_AND_AVAILABLE))
                else:       # polity is ANARCHY
                    possiblePolities = pc.getPossiblePolities()
                    for polity in possiblePolities:
                        self.polityArr.append(Polity(polity, EStatusPolity.UNLOCKED_AND_AVAILABLE))
                for polity in self.allPolitiesArr:
                    polityIsInArray = False
                    for polObj in self.polityArr:
                        if polity is polObj.getPolity():
                            polityIsInArray = True
                    if not polityIsInArray:
                        self.polityArr.append(Polity(polity, EStatusPolity.UNLOCKED_BUT_NOT_AVAILABLE))

    def addCivPolity(self, civPolity):
        self.civPolityArr.append(civPolity)

    def draw(self, window):
        if self.drawPolityOfCiv is None:
            return False
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
