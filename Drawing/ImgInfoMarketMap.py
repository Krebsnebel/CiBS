import pygame

from CivEnums.EBuilding import EBuilding
from CivEnums.EConstants import EConstants
from CivEnums.ERefPoint import ERefPoint
from CivEnums.EResource import EResource
from CivEnums.EUnitType import EUnitType
from CivObjects.Position import Position
from Drawing.EImageObject import EImageObject
from Drawing.ImgInfo import ImgInfo


"""
this class is an image information of market map
* set mouse position, while mouse pressed and for highlighting
* getter for resize and image position of image object
"""


class ImgInfoMarketMap(ImgInfo):

    def __init__(self):
        self.marketMap = None
        self.pickMarket = False
        self.pickTemple = False
        self.pickGranary = False
        self.pickLibrary = False
        self.pickBarrack = False
        self.pickBlacksmith = False
        self.pickTradingPost = False
        self.pickMarina = False
        self.pickWonderCardStack = True
        self.pickWonderCard1 = False
        self.pickWonderCard2 = False
        self.pickWonderCard3 = False
        self.pickWonderCard4 = False
        self.pickWonderMarker1 = False
        self.pickWonderMarker2 = False
        self.pickWonderMarker3 = False
        self.pickWonderMarker4 = False
        self.pickInfantry = False
        self.pickArtillery = False
        self.pickCavalry = False
        self.pickAirForce = False
        self.pickCultureCardI = False
        self.pickCultureCardII = False
        self.pickCultureCardIII = False
        self.pickIron = True
        self.pickIncense = True
        self.pickWheat = True
        self.pickSilk = True
        self.pickCoin = True
        self.pickCulture = True
        self.pickCottage = True
        self.pickBarbarian = True

        self.cultureStepArray = [False for i in range(EConstants.CULTURE_LEVELS.value)]

        super().__init__(1843, 651, Position(90, -611), ERefPoint.TOP_LEFT)

    def setMarketMap(self, marketMap):
        self.marketMap = marketMap

    def setMousePositionForHighlighting(self, mousePosition):
        pass

    def leftMouseButtonPressed(self, mousePosition):
        pass

    def getResize(self, imgObj):
        return imgObj.getResize() * self.scale

    def getImgPosOf(self, imgObj):
        pos = self.getPosOf(ERefPoint.TOP_LEFT, True)
        return Position(pos.getX() + imgObj.getX(), pos.getY() + imgObj.getY())

    def draw(self, window):
        b = self.marketMap.getBusinessObjectCollection()
        delta = EConstants.DELTA_MARKER_BUILDINGS_STACK.value
        t = b.getStackLengthOfBuilding(EBuilding.MARKET) - 1
        self.drawFrame(window, EImageObject.BUILDING_STACK_1L, self.pickMarket, t*delta, -t*delta)
        t = b.getStackLengthOfBuilding(EBuilding.TEMPLE) - 1
        self.drawFrame(window, EImageObject.BUILDING_STACK_1R, self.pickTemple, t*delta, -t*delta)
        t = b.getStackLengthOfBuilding(EBuilding.GRANARY) - 1
        self.drawFrame(window, EImageObject.BUILDING_STACK_2L, self.pickGranary, t*delta, -t*delta)
        t = b.getStackLengthOfBuilding(EBuilding.LIBRARY) - 1
        self.drawFrame(window, EImageObject.BUILDING_STACK_2R, self.pickLibrary, t*delta, -t*delta)
        t = b.getStackLengthOfBuilding(EBuilding.BARRACK) - 1
        self.drawFrame(window, EImageObject.BUILDING_STACK_3L, self.pickBarrack, t*delta, -t*delta)
        t = b.getStackLengthOfBuilding(EBuilding.BLACKSMITH) - 1
        self.drawFrame(window, EImageObject.BUILDING_STACK_3R, self.pickBlacksmith, t*delta, -t*delta)
        t = b.getStackLengthOfBuilding(EBuilding.TRADING_POST) - 1
        self.drawFrame(window, EImageObject.BUILDING_STACK_4L, self.pickTradingPost, t*delta, -t*delta)
        t = b.getStackLengthOfBuilding(EBuilding.MARINA) - 1
        self.drawFrame(window, EImageObject.BUILDING_STACK_4R, self.pickMarina, t*delta, -t*delta)

        delta = EConstants.DELTA_WONDER_CARDS_STACK.value
        t = b.getStackLengthOfWonder() - 1
        self.drawFrame(window, EImageObject.WONDER_STACK, self.pickWonderCardStack, t*delta, -t*delta)
        self.drawFrame(window, EImageObject.WONDER_CARD_POS_1, self.pickWonderCard1, 0, 0)
        self.drawFrame(window, EImageObject.WONDER_CARD_POS_2, self.pickWonderCard2, 0, 0)
        self.drawFrame(window, EImageObject.WONDER_CARD_POS_3, self.pickWonderCard3, 0, 0)
        self.drawFrame(window, EImageObject.WONDER_CARD_POS_4, self.pickWonderCard4, 0, 0)

        self.drawFrame(window, EImageObject.WONDER_MARKER_POS_1, self.pickWonderMarker1, 0, 0)
        self.drawFrame(window, EImageObject.WONDER_MARKER_POS_2, self.pickWonderMarker2, 0, 0)
        self.drawFrame(window, EImageObject.WONDER_MARKER_POS_3, self.pickWonderMarker3, 0, 0)
        self.drawFrame(window, EImageObject.WONDER_MARKER_POS_4, self.pickWonderMarker4, 0, 0)

        mi = self.marketMap.getMilitaryUnitCollection()
        delta = EConstants.DELTA_MILITARY_UNIT_STACK.value - 1
        t = mi.getStackLengthOfMilUnit(EUnitType.INFANTRY)
        self.drawFrame(window, EImageObject.INFANTRY_STACK, self.pickInfantry, t*delta, -t*delta)
        t = mi.getStackLengthOfMilUnit(EUnitType.INFANTRY) - 1
        self.drawFrame(window, EImageObject.ARTILLERY_STACK, self.pickArtillery, t*delta, -t*delta)
        t = mi.getStackLengthOfMilUnit(EUnitType.CAVALRY) - 1
        self.drawFrame(window, EImageObject.CAVALRY_STACK, self.pickCavalry, t*delta, -t*delta)
        t = mi.getStackLengthOfMilUnit(EUnitType.AIR_FORCE) - 1
        self.drawFrame(window, EImageObject.AIR_FORCE_STACK, self.pickAirForce, t*delta, -t*delta)

        c = self.marketMap.getCulturalEventCollection()
        delta = EConstants.DELTA_CULTURE_CARDS_STACK.value
        t = c.getStackLengthOfCultureCards(1) - 1
        self.drawFrame(window, EImageObject.CULTURE_EVENT_1, self.pickCultureCardI, t*delta, -t*delta)
        t = c.getStackLengthOfCultureCards(2) - 1
        self.drawFrame(window, EImageObject.CULTURE_EVENT_2, self.pickCultureCardII, t*delta, -t*delta)
        t = c.getStackLengthOfCultureCards(3) - 1
        self.drawFrame(window, EImageObject.CULTURE_EVENT_3, self.pickCultureCardIII, t*delta, -t*delta)

        m = self.marketMap.getMarkerCollection()
        delta = EConstants.DELTA_TOKENS_STACK.value
        t = m.getStackLengthOfResource(EResource.IRON) - 1
        self.drawFrame(window, EImageObject.IRON_MARKET_MAP, self.pickIron, t * delta, -t * delta)
        t = m.getStackLengthOfResource(EResource.INCENSE) - 1
        self.drawFrame(window, EImageObject.INCENSE_MARKET_MAP, self.pickIncense, t * delta, -t * delta)
        t = m.getStackLengthOfResource(EResource.WHEAT) - 1
        self.drawFrame(window, EImageObject.WHEAT_MARKET_MAP, self.pickWheat, t * delta, -t * delta)
        t = m.getStackLengthOfResource(EResource.SILK) - 1
        self.drawFrame(window, EImageObject.SILK_MARKET_MAP, self.pickSilk, t * delta, -t * delta)
        t = m.getStackLengthOfResource(EResource.COIN) - 1
        self.drawFrame(window, EImageObject.COIN_MARKET_MAP, self.pickCoin, t * delta, -t * delta)
        t = m.getStackLengthOfResource(EResource.CULTURE) - 1
        self.drawFrame(window, EImageObject.CULTURE_MARKET_MAP, self.pickCulture, t * delta, -t * delta)
        t = m.getStackLengthOfCottage() - 1
        self.drawFrame(window, EImageObject.COTTAGE_MARKET_MAP, self.pickCottage, t * delta, -t * delta)
        t = m.getStackLengthOfBarbarian() - 1
        self.drawFrame(window, EImageObject.BARBARIAN_MARKET_MAP, self.pickBarbarian, t * delta, -t * delta)

        imgObj = EImageObject.CULTURE_LEVEL_MARKER
        for i in range(EConstants.CULTURE_LEVELS.value):
            self.drawFrame(window, imgObj, self.cultureStepArray[i],  i*imgObj.getSizeX(), 0)

    def drawFrame(self, window, imgObj, condition, dx, dy):
        if condition:
            possible_img = pygame.Surface(imgObj.getRect(), pygame.SRCALPHA)
            pygame.draw.rect(possible_img, (255, 0, 0), possible_img.get_rect(), 3)
            window.blit(possible_img, (self.getImgPosOf(imgObj).getX() + dx, self.getImgPosOf(imgObj).getY() + dy))

    def getImgPosOf(self, imgObj):
        if imgObj is not None:
            refPos = self.getPosOf(ERefPoint.TOP_LEFT, True)
            return Position(imgObj.getX() + refPos.getX(), imgObj.getY() + refPos.getY())
        return None
