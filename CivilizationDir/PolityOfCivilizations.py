from CivEnums.EPolity import EPolity
from CivEnums.ERotation import ERotation
from CivEnums.EStatusPolity import EStatusPolity
from CivObjects.Polity import Polity
from CivObjects.Position import Position
from Drawing import ImageHandler
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing.EImageObject import EImageObject


"""
this class handles the polity of civilizations
draw functions are implemented
"""


class PolityOfCivilizations:

    def __init__(self, imgInfoPolity):
        self.imgInfo = imgInfoPolity
        self.drawPolityOfCiv = None
        self.idx = 0
        self.polityArr = []
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

    def setPolitiesOfCiv(self, civ, politySwitched):
        self.drawPolityOfCiv = civ
        self.polityArr = []
        self.imgInfo.clearOptions()
        if civ is None:
            return
        self.idx = 0
        for pc in self.civPolityArr:
            if pc.getCivilizationEnum() is self.drawPolityOfCiv:
                pc.setPolitySwitched(politySwitched)
                self.polityArr.append(Polity(pc.getPolity(), EStatusPolity.ACTIVE))
                self.idx = self.idx + 1
                if pc.getPolity() is not EPolity.ANARCHY:
                    polity = pc.getPreviouslyUnlockedPolity()
                    if polity is not None:
                        self.polityArr.append(Polity(polity, EStatusPolity.UNLOCKED_AND_AVAILABLE))
                        if not pc.isPolitySwitched():
                            self.setOption()
                        self.idx = self.idx + 1
                    self.polityArr.append(Polity(EPolity.ANARCHY, EStatusPolity.UNLOCKED_AND_AVAILABLE))
                    if not pc.isPolitySwitched():
                        self.setOption()
                    self.idx = self.idx + 1
                else:       # polity is ANARCHY
                    possiblePolities = pc.getUnlockedPolities()
                    for polity in possiblePolities:
                        self.polityArr.append(Polity(polity, EStatusPolity.UNLOCKED_AND_AVAILABLE))
                        if not pc.isPolitySwitched():
                            self.setOption()
                        self.idx = self.idx + 1
                for polity in self.allPolitiesArr:
                    polityIsInArray = False
                    for polObj in self.polityArr:
                        if polity is polObj.getPolity():
                            polityIsInArray = True
                    if not polityIsInArray:
                        possiblePolities = pc.getUnlockedPolities()
                        status = EStatusPolity.LOCKED
                        for pol in possiblePolities:
                            if polity is pol:
                                status = EStatusPolity.UNLOCKED_BUT_NOT_AVAILABLE
                        self.polityArr.append(Polity(polity, status))

    def addCivPolity(self, civPolity):
        self.civPolityArr.append(civPolity)

    def draw(self, window):
        if self.drawPolityOfCiv is None:
            return
        self.idx = 0
        for polObj in self.polityArr:
            self.drawPolity(window, polObj)

        self.imgInfo.draw(window)

    def drawPolity(self, window, polObj):
        posPol = Position(self.idx % 4, self.idx // 4)
        pos = self.imgInfo.getImgPosOf(EImageObject.POLITY_ZOOMED, posPol)
        resize = EImageObject.POLITY_ZOOMED.getResize()
        DrawCivObjects.drawImage(ImageHandler.getImageOfPolity(polObj.getPolity()), window,
                                 ERotation.NO_ROTATION, pos, resize, 1)
        if polObj.getStatusOfPolity() is EStatusPolity.LOCKED:
            DrawCivObjects.drawImage(ImageHandler.getImageOfPolity(EPolity.LOCKED), window,
                                     ERotation.NO_ROTATION, pos, resize, 1)
        self.idx = self.idx + 1

    def setOption(self):
        self.imgInfo.setOption(EImageObject.POLITY_ZOOMED, self.idx)

    def getValidChoiceWhileMousePressed(self):
        return self.imgInfo.getValidChoiceWhileMousePressed()

    def isLeftMouseButtonPressed(self):
        return self.imgInfo.isLeftMouseButtonPressed()

    def setNewPolity(self, posPol):
        polity = self.polityArr[posPol.getX() + posPol.getY() * 4].getPolity()
        for pc in self.civPolityArr:
            if pc.getCivilizationEnum() is self.drawPolityOfCiv:
                pc.setPolity(polity)
                pc.setPolitySwitched(True)
