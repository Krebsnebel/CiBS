import pygame

from CivEnums.EBuilding import EBuilding
from CivEnums.EConstants import EConstants
from CivEnums.ERefPoint import ERefPoint
from CivEnums.EResource import EResource
from CivEnums.EUnitType import EUnitType
from CivObjects.Position import Position
from Drawing.EImageObject import EImageObject
from Drawing.ImgInfo import ImgInfo
from Options.EOptionType import EOptionType
from Options.Option import Option

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
        self.pickIron = False
        self.pickIncense = False
        self.pickWheat = False
        self.pickSilk = False
        self.pickCoin = False
        self.pickCulture = False
        self.pickCottage = False
        self.pickBarbarian = False

        self.cultureStepArray = [False for i in range(EConstants.CULTURE_LEVELS.value)]

        super().__init__(1843, 651, Position(90, -611), ERefPoint.TOP_LEFT)

    def setMarketMap(self, marketMap):
        self.marketMap = marketMap

    def setMousePositionForHighlighting(self, mousePosition):
        pass

    def leftMouseButtonPressed(self, mousePosition):
        pass

    def getImgPosOf(self, imgObj, shift, scale):
        pos = self.getPosOf(ERefPoint.TOP_LEFT, shift, scale)
        return Position(pos.getX() + imgObj.getX(), pos.getY() + imgObj.getY())

    def setMousePosition(self, x, y):
        ImgInfo.setMousePosition(self, x, y)
        self.mouseAtPossiblePosition = None
        for opt in self.options:
            mousePos = self.getMousePosition(False)
            insideX = opt.getX() < mousePos.getX()/self.scale - self.getShiftX() <= opt.getX() + opt.getWidth()
            insideY = opt.getY() < mousePos.getY()/self.scale - self.getShiftY() <= opt.getY() + opt.getHeight()
            if insideX and insideY:
                self.mouseAtPossiblePosition = Option(opt.getImgObj(), opt.getX(), opt.getY(),
                                                      opt.getOptionType(), opt.getEmphasize(), opt.getPositionOfMap())

    def setOptionsForBuildings(self, mk, te, gr, li, ba, bl, tr, mr):
        self.pickMarket = mk
        self.pickTemple = te
        self.pickGranary = gr
        self.pickLibrary = li
        self.pickBarrack = ba
        self.pickBlacksmith = bl
        self.pickTradingPost = tr
        self.pickMarina = mr

    def setOptionsForWonder(self, wcs, wc1, wc2, wc3, wc4, wk1, wk2, wk3, wk4):
        self.pickWonderCardStack = wcs
        self.pickWonderCard1 = wc1
        self.pickWonderCard2 = wc2
        self.pickWonderCard3 = wc3
        self.pickWonderCard4 = wc4
        self.pickWonderMarker1 = wk1
        self.pickWonderMarker2 = wk2
        self.pickWonderMarker3 = wk3
        self.pickWonderMarker4 = wk4

    def setOptionsForMilitaryAndCultureCards(self, inf, art, cav, af, cc1, cc2, cc3):
        self.pickInfantry = inf
        self.pickArtillery = art
        self.pickCavalry = cav
        self.pickAirForce = af
        self.pickCultureCardI = cc1
        self.pickCultureCardII = cc2
        self.pickCultureCardIII = cc3

    def setOptionsForMarker(self, ir, ic, wt, sk, cn, cu, co, ba):
        self.pickIron = ir
        self.pickIncense = ic
        self.pickWheat = wt
        self.pickSilk = sk
        self.pickCoin = cn
        self.pickCulture = cu
        self.pickCottage = co
        self.pickBarbarian = ba

    def setOptionsForCultureLevelMarker(self, cultureStepArray):
        self.cultureStepArray = cultureStepArray.copy()

    def setOptions(self):
        self.options = []
        b = self.marketMap.getBusinessObjectCollection()
        delta = EConstants.DELTA_MARKER_BUILDINGS_STACK.value
        t = b.getStackLengthOfBuilding(EBuilding.MARKET) - 1
        self.setOption(self.pickMarket, EImageObject.BUILDING_STACK_1L, t * delta, -t * delta)
        t = b.getStackLengthOfBuilding(EBuilding.TEMPLE) - 1
        self.setOption(self.pickTemple, EImageObject.BUILDING_STACK_1R, t * delta, -t * delta)
        t = b.getStackLengthOfBuilding(EBuilding.GRANARY) - 1
        self.setOption(self.pickGranary, EImageObject.BUILDING_STACK_2L, t * delta, -t * delta)
        t = b.getStackLengthOfBuilding(EBuilding.LIBRARY) - 1
        self.setOption(self.pickLibrary, EImageObject.BUILDING_STACK_2R, t * delta, -t * delta)
        t = b.getStackLengthOfBuilding(EBuilding.BARRACK) - 1
        self.setOption(self.pickBarrack, EImageObject.BUILDING_STACK_3L, t * delta, -t * delta)
        t = b.getStackLengthOfBuilding(EBuilding.BLACKSMITH) - 1
        self.setOption(self.pickBlacksmith, EImageObject.BUILDING_STACK_3R, t * delta, -t * delta)
        t = b.getStackLengthOfBuilding(EBuilding.TRADING_POST) - 1
        self.setOption(self.pickTradingPost, EImageObject.BUILDING_STACK_4L, t * delta, -t * delta)
        t = b.getStackLengthOfBuilding(EBuilding.MARINA) - 1
        self.setOption(self.pickMarina, EImageObject.BUILDING_STACK_4R, t * delta, -t * delta)

        delta = EConstants.DELTA_WONDER_CARDS_STACK.value
        t = b.getStackLengthOfWonder() - 1
        self.setOption(self.pickWonderCardStack, EImageObject.WONDER_STACK, t * delta, -t * delta)
        self.setOption(self.pickWonderCard1, EImageObject.WONDER_CARD_POS_1, 0, 0)
        self.setOption(self.pickWonderCard2, EImageObject.WONDER_CARD_POS_2, 0, 0)
        self.setOption(self.pickWonderCard3, EImageObject.WONDER_CARD_POS_3, 0, 0)
        self.setOption(self.pickWonderCard4, EImageObject.WONDER_CARD_POS_4, 0, 0)

        self.setOption(self.pickWonderMarker1, EImageObject.WONDER_MARKER_POS_1, 0, 0)
        self.setOption(self.pickWonderMarker2, EImageObject.WONDER_MARKER_POS_2, 0, 0)
        self.setOption(self.pickWonderMarker3, EImageObject.WONDER_MARKER_POS_3, 0, 0)
        self.setOption(self.pickWonderMarker4, EImageObject.WONDER_MARKER_POS_4, 0, 0)

        mi = self.marketMap.getMilitaryUnitCollection()
        delta = EConstants.DELTA_MILITARY_UNIT_STACK.value
        t = mi.getStackLengthOfMilUnit(EUnitType.INFANTRY) - 1
        self.setOption(self.pickInfantry, EImageObject.INFANTRY_STACK, t * delta, -t * delta)
        t = mi.getStackLengthOfMilUnit(EUnitType.INFANTRY) - 1
        self.setOption(self.pickArtillery, EImageObject.ARTILLERY_STACK, t * delta, -t * delta)
        t = mi.getStackLengthOfMilUnit(EUnitType.CAVALRY) - 1
        self.setOption(self.pickCavalry, EImageObject.CAVALRY_STACK, t * delta, -t * delta)
        t = mi.getStackLengthOfMilUnit(EUnitType.AIR_FORCE) - 1
        self.setOption(self.pickAirForce, EImageObject.AIR_FORCE_STACK, t * delta, -t * delta)

        c = self.marketMap.getCulturalEventCollection()
        delta = EConstants.DELTA_CULTURE_CARDS_STACK.value
        t = c.getStackLengthOfCultureCards(1) - 1
        self.setOption(self.pickCultureCardI, EImageObject.CULTURE_EVENT_1, t * delta, -t * delta)
        t = c.getStackLengthOfCultureCards(2) - 1
        self.setOption(self.pickCultureCardII, EImageObject.CULTURE_EVENT_2, t * delta, -t * delta)
        t = c.getStackLengthOfCultureCards(3) - 1
        self.setOption(self.pickCultureCardIII, EImageObject.CULTURE_EVENT_3, t * delta, -t * delta)

        m = self.marketMap.getMarkerCollection()
        delta = EConstants.DELTA_TOKENS_STACK.value
        t = m.getStackLengthOfResource(EResource.IRON) - 1
        self.setOption(self.pickIron, EImageObject.IRON_MARKET_MAP, t * delta, -t * delta)
        t = m.getStackLengthOfResource(EResource.INCENSE) - 1
        self.setOption(self.pickIncense, EImageObject.INCENSE_MARKET_MAP, t * delta, -t * delta)
        t = m.getStackLengthOfResource(EResource.WHEAT) - 1
        self.setOption(self.pickWheat, EImageObject.WHEAT_MARKET_MAP, t * delta, -t * delta)
        t = m.getStackLengthOfResource(EResource.SILK) - 1
        self.setOption(self.pickSilk, EImageObject.SILK_MARKET_MAP, t * delta, -t * delta)
        t = m.getStackLengthOfResource(EResource.COIN) - 1
        self.setOption(self.pickCoin, EImageObject.COIN_MARKET_MAP, t * delta, -t * delta)
        t = m.getStackLengthOfResource(EResource.CULTURE) - 1
        self.setOption(self.pickCulture, EImageObject.CULTURE_MARKET_MAP, t * delta, -t * delta)
        t = m.getStackLengthOfCottage() - 1
        self.setOption(self.pickCottage, EImageObject.COTTAGE_MARKET_MAP, t * delta, -t * delta)
        t = m.getStackLengthOfBarbarian() - 1
        self.setOption(self.pickBarbarian, EImageObject.BARBARIAN_MARKET_MAP, t * delta, -t * delta)

        imgObj = EImageObject.CULTURE_LEVEL_MARKER
        for i in range(EConstants.CULTURE_LEVELS.value):
            self.setOption(self.cultureStepArray[i], EImageObject.CULTURE_LEVEL_MARKER, i * imgObj.getSizeX(), 0)

    def setOption(self, cond, imgObj, dx, dy):
        if cond:
            imgPos = self.getImgPosOf(imgObj, False, False)
            self.options.append(Option(imgObj, imgPos.getX() + dx, imgPos.getY() + dy, EOptionType.SQUARE,
                                       self.emphasize, None))
