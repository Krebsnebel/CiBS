from CivCollection.Civilization import Civilization
from CivCollection.GameMap import GameMap
from CivCollection.PolityOfCivilizations import PolityOfCivilizations
from CivEnums.ECivilization import ECivilization


"""
this class is the overall class of the whole game
in this class all subclasses are defined
"""


class Game:

    def __init__(self, imgInfoGame, marketMap, playerColor, mapTileCollection):
        self.civilizations = []
        self.imgInfo = imgInfoGame
        self.gameMap = GameMap(imgInfoGame.getGameMap())
        self.polityOfCivilizations = PolityOfCivilizations()
        self.marketMap = marketMap
        self.playerColor = playerColor
        self.numberOfPlayer = len(self.playerColor)

        militaryUnitCollection = self.marketMap.getMilitaryUnitCollection()
        for i in range(self.numberOfPlayer):
            mt = mapTileCollection.popMapTileCiv()
            civ = Civilization(imgInfoGame.getCivilization(i), i, mt.civilization, mt, playerColor[i], self.gameMap)
            self.polityOfCivilizations.addCivPolity(civ.getCivPolity())
#            self.polityOfCivilizations.setCivForDrawing(civ.getCivilizationEnum())
            civ.addMilitaryUnit(militaryUnitCollection.getArtillery())
            civ.addMilitaryUnit(militaryUnitCollection.getCavalry())
            civ.addMilitaryUnit(militaryUnitCollection.getInfantry())
            if civ.getCivilizationEnum() == ECivilization.GERMANY:
                civ.addMilitaryUnit(militaryUnitCollection.getInfantry())
                civ.addMilitaryUnit(militaryUnitCollection.getInfantry())
            self.civilizations.append(civ)

    def setGame(self, mapTileCollection):
        self.gameMap.setGame(self.civilizations, mapTileCollection)

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
