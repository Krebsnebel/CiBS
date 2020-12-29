from enum import Enum


class EImageObject(Enum):

    def __init__(self, imgSizeX, imgSizeY, resize, posX, posY):
        self.imgSizeX = imgSizeX
        self.imgSizeY = imgSizeY
        self.resize = resize
        self.sizeX = self.imgSizeX * resize
        self.sizeY = self.imgSizeY * resize
        self.posX = posX
        self.posY = posY

    def getX(self):
        return self.posX

    def getY(self):
        return self.posY

    def getSizeX(self):
        return self.sizeX

    def getSizeY(self):
        return self.sizeY

    def getImgSizeX(self):
        return self.sizeX

    def getImgSizeY(self):
        return self.sizeY

    def getResize(self):
        return self.resize

    def getRect(self):
        return int(self.getSizeX()), int(self.getSizeY())

    NO_OBJECT = (0, 0, 0.0, 0.0, 0.0)
    BARBARIAN_MARKET_MAP = (100, 100, 60.0 / 100.0, 100.0, 10.0)
    COTTAGE_MARKET_MAP = (100, 100, 60.0 / 100.0, 200.0, 50.0)
    IRON_MARKET_MAP = (100, 100, 60.0 / 100.0, 100.0, 90.0)
    INCENSE_MARKET_MAP = (100, 100, 60.0 / 100.0, 200.0, 130.0)
    WHEAT_MARKET_MAP = (100, 100, 60.0 / 100.0, 100.0, 170.0)
    SILK_MARKET_MAP = (100, 100, 60.0 / 100.0, 200.0, 210.0)
    COIN_MARKET_MAP = (85, 85, 60.0 / 100.0, 0.0, 400.0)
    CULTURE_MARKET_MAP = (100, 80, 60.0 / 100.0, 100.0, 440.0)
    CULTURE_LEVEL_MARKER = (48.49, 60, 1.0, 386.0, 460.0)
    NEXT_BUTTON = (2400, 2400, 60.0 / 2400.0, 20.0, 20.0)
    CIVILIZATION_SHEET = (2000, 1333, 217.0 / 1333.0, 2000.0 * 217.0 / 1333.0, 217.0)
    MARKET_MAP = (2000, 997, 531.4 / 997.0, 390.0, 0.0)
    MAP_TILE = (1125, 1125, 240.0 / 1125.0, 0.0, 0.0)
    SQUARE = (1125, 1125, 60.0 / 1125.0, 0.0, 0.0)
    CIVILIZATION_RESEARCH = (1125, 1125, 240.0 / 1125.0, 0.0, 0.0)
    TRADE_DISK = (1125, 1125, 96.0 / 1125.0, 200.0, 31.0)
    GOLD_DISK = (1125, 1125, 46.0 / 1125.0, 225.0, 56.0)
    POLITY = (1333, 2000, 78.0 / 1333.0, 7.0, 98.0)
    POLITY_ZOOMED = (1333, 2000, 250.0 / 1333.0, 10.0, 10.0)
    BUILDING_STACK_1L = (1125, 1125, 60.0 / 1125.0, 619.0, 11.0)
    BUILDING_STACK_1R = (1125, 1125, 60.0 / 1125.0, 778.0, 11.0)
    BUILDING_STACK_2L = (1125, 1125, 60.0 / 1125.0, 619.0, 118.0)
    BUILDING_STACK_2R = (1125, 1125, 60.0 / 1125.0, 778.0, 118.0)
    BUILDING_STACK_3L = (1125, 1125, 60.0 / 1125.0, 619.0, 225.0)
    BUILDING_STACK_3R = (1125, 1125, 60.0 / 1125.0, 778.0, 225.0)
    BUILDING_STACK_4L = (1125, 1125, 60.0 / 1125.0, 654.0, 332.0)
    BUILDING_STACK_4R = (1125, 1125, 60.0 / 1125.0, 815.0, 332.0)
    WONDER_STACK = (1125, 750, 78.0 / 750.0, 397.0, 2.0)
    WONDER_CARD_POS_1 = (1125, 750, 78.0 / 750.0, 397.0, 90.0)
    WONDER_CARD_POS_2 = (1125, 750, 78.0 / 750.0, 397.0, 178.0)
    WONDER_CARD_POS_3 = (1125, 750, 78.0 / 750.0, 397.0, 266.0)
    WONDER_CARD_POS_4 = (1125, 750, 78.0 / 750.0, 397.0, 354.0)
    WONDER_MARKER_POS_1 = (1125, 1125, 60.0 / 1125.0, 522.0, 99.0)
    WONDER_MARKER_POS_2 = (1125, 1125, 60.0 / 1125.0, 522.0, 187.0)
    WONDER_MARKER_POS_3 = (1125, 1125, 60.0 / 1125.0, 522.0, 275.0)
    WONDER_MARKER_POS_4 = (1125, 1125, 60.0 / 1125.0, 522.0, 363.0)
    WONDER_CARD_CIV_POS_1 = (1125, 750, 78.0 / 750.0, 0.0, -85.0)
    WONDER_CARD_CIV_POS_2 = (1125, 750, 78.0 / 750.0, 0.0, -170.0)
    WONDER_CARD_CIV_POS_3 = (1125, 750, 78.0 / 750.0, 0.0, -255.0)
    ARTIST_MARKER_CIV = (1125, 1125, 60.0 / 1125.0, 125.0, -75.0)
    BUILDER_MARKER_CIV = (1125, 1125, 60.0 / 1125.0, 125.0, -150.0)
    GENERAL_MARKER_CIV = (1125, 1125, 60.0 / 1125.0, 125.0, -225.0)
    HUMANITARIAN_MARKER_CIV = (1125, 1125, 60.0 / 1125.0, 200.0, -75.0)
    INDUSTRIALIST_MARKER_CIV = (1125, 1125, 60.0 / 1125.0, 200.0, -150.0)
    SCIENTIST_MARKER_CIV = (1125, 1125, 60.0 / 1125.0, 200.0, -225.0)
    CULTURE_EVENT_1 = (1333, 2000, 78.0 / 1333.0, 567.0, 550.0)
    CULTURE_EVENT_2 = (1333, 2000, 78.0 / 1333.0, 905.0, 550.0)
    CULTURE_EVENT_3 = (1333, 2000, 78.0 / 1333.0, 1245.0, 550.0)
    SQUARE_OBJECT = (1125, 1125, 60.0 / 1125.0, 0.0, 0.0)
    WONDER_CARD = (1125, 750, 78.0 / 750.0, 0.0, 0.0)
    INFANTRY_STACK = (1125, 1125, 132.0 / 1125.0, 1045.0, 38.0)
    ARTILLERY_STACK = (1125, 1125, 132.0 / 1125.0, 1293.0, 38.0)
    CAVALRY_STACK = (1125, 1125, 132.0 / 1125.0, 1045.0, 256.0)
    AIR_FORCE_STACK = (1125, 1125, 132.0 / 1125.0, 1293.0, 256.0)
    UNIT_CARDS = (1125, 1125, 132.0 / 1125.0, 0.0, 0.0)
    CULTURE_CARDS_CIV = (1333, 2000, 78.0 / 1333.0, 10.0, 3.0)
    RESEARCH_CARDS = (376, 246, 120.0 / 376.0, 20.0, 20.0)
    UNRESEARCHED_CARDS_ZOOMED = (376, 246, 120.0 / 376.0, 20.0, 20.0)
    FIGURE = (1125, 1125, 60.0 / 1125.0, 120.0, 330.0)
    CITY = (1125, 1125, 60.0 / 1125.0, 60.0, 0.0)
    KAPITOL = (1125, 1125, 60.0 / 1125.0, 60.0, 427.0)
    CITY_1 = (1125, 1125, 60.0 / 1125.0, 60.0, 357.0)
    CITY_2 = (1125, 1125, 60.0 / 1125.0, 60.0, 287.0)
    TOWN = (1125, 1125, 60.0 / 1125.0, 0.0, 0.0)
    WONDER = (1125, 1125, 60.0 / 1125.0, 0.0, 0.0)
    GREAT_PERSON = (1125, 1125, 60.0 / 1125.0, 0.0, 0.0)
    UNIQUE_BUILDINGS = (1125, 1125, 60.0 / 1125.0, 0.0, 0.0)
    BUILDINGS_ON_GRASSLAND = (1125, 1125, 60.0 / 1125.0, 0.0, 0.0)
    BUILDINGS_IN_MOUNTAIN = (1125, 1125, 60.0 / 1125.0, 0.0, 0.0)
    BUILDINGS_ON_WATER = (1125, 1125, 60.0 / 1125.0, 0.0, 0.0)
    BUILDINGS_IN_DESERT = (1125, 1125, 60.0 / 1125.0, 0.0, 0.0)
    ARMY = (1125, 1125, 60.0 / 1125.0, [0, 10, -15, -20, 25, -35, 30], [-15, 25, -20, 0, -27, 10, 17])
    PIONEER = (1125, 1125, 60.0 / 1125.0, [-25, 18], [60, 60])

    INFANTRY = (0, 0, 0, 0, 0)
    ARTILLERY = (0, 0, 0, 0, 0)
    CAVALRY = (0, 0, 0, 0, 0)
    AIR_FORCE = (0, 0, 0, 0, 0)
