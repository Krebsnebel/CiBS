from CivCollection.MapTileCollection import MapTileCollection
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
        self.polityOfCivilizations = PolityOfCivilizations()

        militaryUnitCollection = self.marketMap.getMilitaryUnitCollection()
        for i in range(self.numberOfPlayer):
            mt = self.mapTileCollection.popMapTileCiv()
#            civ = Civilization(imgInfoGame.getCivilization(i), i, mt, playerColor[i], self.gameMap, gameStep)
            civ = Civilization(imgInfoGame.getCivilization(i), i, mt, playerColor[i], self, gameStep)
            self.polityOfCivilizations.addCivPolity(civ.getCivPolity())
            civ.addMilitaryUnit(militaryUnitCollection.getArtillery())
            civ.addMilitaryUnit(militaryUnitCollection.getCavalry())
            civ.addMilitaryUnit(militaryUnitCollection.getInfantry())
            if civ.getCivilizationEnum() == ECivilization.GERMANY:
                civ.addMilitaryUnit(militaryUnitCollection.getInfantry())
                civ.addMilitaryUnit(militaryUnitCollection.getInfantry())
            self.civilizations.append(civ)

        self.setGame()

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
