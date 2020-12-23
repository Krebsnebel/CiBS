from CivEnums.EConstants import EConstants
from CivEnums.ENote import ENote
from CivEnums.EResource import EResource
from CivEnums.ERotation import ERotation
from CivObjects.Marker import Marker
from CivObjects.Position import Position
from Drawing.EImageObject import EImageObject

"""
this class is a collection of different markers on market map
resource, cottage, barbarian, coin and culture markers collected and - if necessary - shuffled (ToDo) here
depending of move of each player markers can be taken from marker pile (ToDo)
there is a function to draw the marker piles on market place (ToDo)
"""


class MarkerCollection:

    def __init__(self, imgInfoMarketMap, num_player):
        self.imgInfo = imgInfoMarketMap
        self.wheat = []
        self.iron = []
        self.silk = []
        self.incense = []
        self.cottage = []
        self.barbarian = []
        self.coin = []
        self.culture = []

        for i in range(2):
            self.barbarian.append(Marker(ENote.BARBARIAN, EResource.GREAT_PERSON))
            self.barbarian.append(Marker(ENote.BARBARIAN, EResource.URANIUM))
            self.cottage.append(Marker(ENote.COTTAGE, EResource.IRON))

        for i in range(3):
            self.barbarian.append(Marker(ENote.BARBARIAN, EResource.SPY))
            self.barbarian.append(Marker(ENote.BARBARIAN, EResource.IRON))
            self.cottage.append(Marker(ENote.COTTAGE, EResource.SPY))

        for i in range(num_player):
            self.wheat.append(Marker(ENote.RESOURCE, EResource.WHEAT))
            self.iron.append(Marker(ENote.RESOURCE, EResource.IRON))
            self.silk.append(Marker(ENote.RESOURCE, EResource.SILK))
            self.incense.append(Marker(ENote.RESOURCE, EResource.INCENSE))

        for i in range(5):
            self.cottage.append(Marker(ENote.COTTAGE, EResource.WHEAT))
            self.cottage.append(Marker(ENote.COTTAGE, EResource.SILK))
            self.cottage.append(Marker(ENote.COTTAGE, EResource.INCENSE))

        for i in range(EConstants.NUMBER_COINS.value):
            self.coin.append(Marker(ENote.RESOURCE, EResource.COIN))

        for i in range(EConstants.NUMBER_CULTURE.value):
            self.culture.append(Marker(ENote.RESOURCE, EResource.CULTURE))

    def getStackLengthOfResource(self, resource):
        if resource is EResource.IRON:
            return len(self.iron)
        elif resource is EResource.INCENSE:
            return len(self.incense)
        elif resource is EResource.WHEAT:
            return len(self.wheat)
        elif resource is EResource.SILK:
            return len(self.silk)
        elif resource is EResource.COIN:
            return len(self.coin)
        elif resource is EResource.CULTURE:
            return len(self.culture)
        else:
            return -1

    def getStackLengthOfCottage(self):
        return len(self.cottage)

    def getStackLengthOfBarbarian(self):
        return len(self.barbarian)

    def draw(self, window):
        delta = EConstants.DELTA_TOKENS_STACK.value
        self.drawStack(window, self.barbarian, self.imgInfo, EImageObject.BARBARIAN_MARKET_MAP, delta)
        self.drawStack(window, self.cottage, self.imgInfo, EImageObject.COTTAGE_MARKET_MAP, delta)
        self.drawStack(window, self.iron, self.imgInfo, EImageObject.IRON_MARKET_MAP, delta)
        self.drawStack(window, self.incense, self.imgInfo, EImageObject.INCENSE_MARKET_MAP, delta)
        self.drawStack(window, self.wheat, self.imgInfo, EImageObject.WHEAT_MARKET_MAP, delta)
        self.drawStack(window, self.silk, self.imgInfo, EImageObject.SILK_MARKET_MAP, delta)

        self.drawStack(window, self.coin, self.imgInfo, EImageObject.COIN_MARKET_MAP, delta)
        self.drawStack(window, self.culture, self.imgInfo, EImageObject.CULTURE_MARKET_MAP, delta)

    def drawStack(self, window, stack, imgInfo, imgObj, s):
        scale = self.imgInfo.getScale()
        i = 0
        stackPos = imgInfo.getImgPosOf(imgObj, True, False)
        resize = imgObj.getResize()
        for obj in stack:
            pos = Position(stackPos.getX() + i, stackPos.getY() - i)
            obj.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
            i = i + s
