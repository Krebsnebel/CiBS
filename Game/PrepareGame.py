from random import randrange

from CivEnums.ECivilization import ECivilization
from CivEnums.EGameSection import EGameSection
from Drawing.EImageObject import EImageObject
from Game.EGameStep import EGameStep


"""
this class handles the preparation of the game before round start
"""


class PrepareGame:

    def __init__(self, gameStep, game, businessObjectCollection):
        self.gameStep = gameStep
        self.game = game
        self.businessObjectCollection = businessObjectCollection

    def execute(self):
        civ = self.gameStep.getCivilization()
        civEnum = civ.getCivilizationEnum()
        if self.isInStep(EGameStep.MARK_SQUARES_FOR_HIGHLIGHTING_CITY):
            self.gameStep.setNextStep(None, EImageObject.KAPITOL, EGameStep.SET_CITY)
        elif self.isInStep(EGameStep.SET_CITY):
            kap = civ.getCity(0)
            p = self.gameStep.setSquareObject("Hauptstadt")
            if p is not None:
                self.getGameMap().setCity(kap, p.getX(), p.getY())
                self.gameStep.getCivPossibilities().refreshCityConstellation(0, True)
                if civEnum == ECivilization.AGYPT:
                    self.gameStep.setNextStep(self.businessObjectCollection.popWonder(randrange(4)),
                                              EImageObject.WONDER, EGameStep.SET_WONDER)
                elif civEnum == ECivilization.AMERICA:
                    self.gameStep.setNextStep(self.businessObjectCollection.popGreatPerson(), EImageObject.WONDER,
                                              EGameStep.SET_GREAT_PERSON)
                else:
                    self.gameStep.setNextStep(None, EImageObject.FIGURE, EGameStep.SET_PIONEER)
        elif self.isInStep(EGameStep.SET_WONDER):
            w = self.gameStep.getChosenSquareObject()
            p = self.gameStep.setSquareObject("Wunder")
            if p is not None:
                self.getGameMap().setBusinessObject(w, p.getX(), p.getY())
                self.gameStep.setNextStep(None, EImageObject.FIGURE, EGameStep.SET_PIONEER)
        elif self.isInStep(EGameStep.SET_GREAT_PERSON):
            g = self.gameStep.getChosenSquareObject()
            p = self.gameStep.setSquareObject("Große Persönlichkeit")
            if p is not None:
                self.getGameMap().setBusinessObject(g, p.getX(), p.getY())
                self.gameStep.setNextStep(None, EImageObject.FIGURE, EGameStep.SET_PIONEER)
        elif self.isInStep(EGameStep.SET_PIONEER):
            fig = [civ.getPioneer(0)]
            p = self.gameStep.setSquareObject("Pionier")
            if p is not None:
                self.getGameMap().setFigures(fig, p.getX(), p.getY())
                self.gameStep.setNextStep(None, EImageObject.FIGURE, EGameStep.SET_ARMY_NR1)
        elif self.isInStep(EGameStep.SET_ARMY_NR1):
            fig = [civ.getArmy(0)]
            p = self.gameStep.setSquareObject("Armee - 01")
            if p is not None:
                self.getGameMap().setFigures(fig, p.getX(), p.getY())
                if civEnum == ECivilization.RUSSIA:
                    self.gameStep.setNextStep(None, EImageObject.FIGURE, EGameStep.SET_ARMY_NR2)
                else:
                    self.gameStep.setNextStep(None, None, EGameStep.COUNT_TRADING_POINTS)
        elif self.isInStep(EGameStep.SET_ARMY_NR2):
            fig = [civ.getArmy(6)]
            p = self.gameStep.setSquareObject("Armee - 02")
            if p is not None:
                self.getGameMap().setFigures(fig, p.getX(), p.getY())
                self.gameStep.setNextStep(None, None, EGameStep.COUNT_TRADING_POINTS)
        elif self.isInStep(EGameStep.COUNT_TRADING_POINTS):
            civ.countTradingPoints()
            civ.isThirdCityPossible()
            self.gameStep.setNextCivilization(False)
            if self.gameStep.isRoundCompleted():
                self.refreshTownPositions()
                self.gameStep.setGameStep(None, None, EGameStep.GENERAL_SELECT, EGameSection.START_ROUND)
            else:
                self.gameStep.setGameStep(None, None, EGameStep.MARK_SQUARES_FOR_HIGHLIGHTING_CITY,
                                          EGameSection.PREPARE_GAME)

    def isInStep(self, step):
        return self.gameStep.get() == step

    def getGameMap(self):
        return self.game.getGameMap()

    def refreshTownPositions(self):
        self.getGameMap().refreshPotentiallyTownPositions()
        self.gameStep.refreshCurrentTownPositions()
