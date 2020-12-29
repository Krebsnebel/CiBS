from CivCollection.MapTileCollection import MapTileCollection
from CivEnums.EUnitType import EUnitType
from CivilizationDir.Civilization import Civilization
from Game.GameMap import GameMap
from CivilizationDir.PolityOfCivilizations import PolityOfCivilizations
from CivEnums.ECivilization import ECivilization
from Game.MarketMap import MarketMap

"""
this class is the overall class of the whole game
in this class all subclasses are defined
"""


class Game:

    def __init__(self, imgInfoGame, playerColor, gameStep):
        self.playerColor = playerColor
        self.numberOfPlayer = len(self.playerColor)
        self.gameStep = gameStep
        self.marketMap = MarketMap(imgInfoGame.getMarketMap(), self.numberOfPlayer)
        imgInfoGame.getMarketMap().setMarketMap(self.marketMap)
        self.mapTileCollection = MapTileCollection(imgInfoGame.getGameMap())
        self.civilizations = []
        self.imgInfo = imgInfoGame
        self.gameMap = GameMap(imgInfoGame.getGameMap())
        self.polityOfCivilizations = PolityOfCivilizations(imgInfoGame.getPolity())

        militaryUnitCollection = self.marketMap.getMilitaryUnitCollection()
        for i in range(self.numberOfPlayer):
            mt = self.mapTileCollection.popMapTileCiv()
            civ = Civilization(imgInfoGame.getCivilization(i), i, mt, playerColor[i], self, gameStep)
            self.polityOfCivilizations.addCivPolity(civ.getCivPolity())
            civ.addMilitaryUnit(militaryUnitCollection.getCard(EUnitType.ARTILLERY))
            civ.addMilitaryUnit(militaryUnitCollection.getCard(EUnitType.CAVALRY))
            civ.addMilitaryUnit(militaryUnitCollection.getCard(EUnitType.INFANTRY))
            if civ.getCivilizationEnum() == ECivilization.GERMANY:
                civ.addMilitaryUnit(militaryUnitCollection.getCard(EUnitType.INFANTRY))
                civ.addMilitaryUnit(militaryUnitCollection.getCard(EUnitType.INFANTRY))
            self.civilizations.append(civ)

        self.setGame()

    def getPolityOfCivilizations(self):
        return self.polityOfCivilizations

    def getMarketMap(self):
        return self.marketMap

    def getBusinessObjectCollection(self):
        return self.marketMap.getBusinessObjectCollection()

    def setGame(self):
        self.gameMap.setGame(self.civilizations, self.mapTileCollection)

    def getGameMap(self):
        return self.gameMap

    def getCivilizations(self):
        return self.civilizations

    def draw(self, window):
        self.gameMap.draw(window)
        for c in self.civilizations:
            c.draw(window)
        self.marketMap.draw(window)
        self.polityOfCivilizations.draw(window)

        self.imgInfo.draw(window)
