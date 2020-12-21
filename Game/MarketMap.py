import pygame

from CivCollection.BusinessObejctCollection import BusinessObjectCollection
from CivCollection.CulturalEventCollection import CulturalEventCollection
from CivCollection.MarkerCollection import MarkerCollection
from CivCollection.MilitaryUnitCollection import MilitaryUnitCollection
from CivEnums.ERotation import ERotation
from Drawing.DrawCivObjects import DrawCivObjects
from Drawing.EImageObject import EImageObject


"""
this class handles the complete market map of game
getters of collections and draw function are implemented
"""


class MarketMap:

    def __init__(self, imgInfoMarketMap, numberOfPlayer):
        self.numberOfPlayer = numberOfPlayer
        self.imgInfo = imgInfoMarketMap
        self.militaryUnitCollection = MilitaryUnitCollection(imgInfoMarketMap)
        self.businessObjectCollection = BusinessObjectCollection(imgInfoMarketMap)
        self.markerCollection = MarkerCollection(imgInfoMarketMap, numberOfPlayer)
        self.culturalEventCollection = CulturalEventCollection(imgInfoMarketMap)
        self.imgMarket = pygame.image.load("Material/MarketMap/MarketMap.jpg")

    def getMilitaryUnitCollection(self):
        return self.militaryUnitCollection

    def getBusinessObjectCollection(self):
        return self.businessObjectCollection

    def getMarkerCollection(self):
        return self.markerCollection

    def getCulturalEventCollection(self):
        return self.culturalEventCollection

    def draw(self, window):
        pos = self.imgInfo.getImgPosOf(EImageObject.MARKET_MAP)
        resize = self.imgInfo.getResize(EImageObject.MARKET_MAP)
        DrawCivObjects.drawImage(self.imgMarket, window, ERotation.NO_ROTATION, pos, resize, 1)
        self.businessObjectCollection.draw(window)
        self.culturalEventCollection.draw(window)
        self.militaryUnitCollection.draw(window)
        self.markerCollection.draw(window)

        self.imgInfo.draw(window)
