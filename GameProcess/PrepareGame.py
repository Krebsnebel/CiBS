from random import randrange

from CivEnums.ECivilization import ECivilization
from CivEnums.EGameSection import EGameSection
from GameProcess.EGameStep import EGameStep


"""
this class handles the preparation of the game before round start
"""


class PrepareGame:

    def __init__(self, gameStep, game):
        self.gameStep = gameStep
        self.game = game
        self.businessObjectCollection = self.game.getBusinessObjectCollection()

    def execute(self):
        civ = self.gameStep.getCivilization()
        civEnum = civ.getCivilizationEnum()
        if self.isInStep(EGameStep.MARK_SQUARES_FOR_HIGHLIGHTING_CITY):
            self.gameStep.setChosenObj(civ.getCity(0))
            self.gameStep.setStep(EGameStep.SET_CITY)
        elif self.isInStep(EGameStep.SET_CITY):
            self.gameStep.expectGameMapPosition("Hauptstadt")
            p = civ.getMousePressedAtPossibleGameMapPosition()
            if p is not None:
                self.getGameMap().setCity(self.gameStep.getChosenObj(), p.getX(), p.getY())
                if civEnum == ECivilization.AGYPT:
                    self.gameStep.setChosenObj(self.businessObjectCollection.popWonder(randrange(4)))
                    self.gameStep.setStep(EGameStep.SET_WONDER)
                elif civEnum == ECivilization.AMERICA:
                    self.gameStep.setChosenObj(self.businessObjectCollection.popGreatPerson())
                    self.gameStep.setStep(EGameStep.SET_GREAT_PERSON)
                else:
                    self.gameStep.setChosenObj([civ.getPioneer(0)])
                    self.gameStep.setStep(EGameStep.SET_PIONEER)
        elif self.isInStep(EGameStep.SET_WONDER):
            self.gameStep.expectGameMapPosition("Wunder")
            p = civ.getMousePressedAtPossibleGameMapPosition()
            if p is not None:
                self.getGameMap().setBusinessObject(self.gameStep.getChosenObj(), p.getX(), p.getY())
                self.gameStep.setChosenObj([civ.getPioneer(0)])
                self.gameStep.setStep(EGameStep.SET_PIONEER)
        elif self.isInStep(EGameStep.SET_GREAT_PERSON):
            self.gameStep.expectGameMapPosition("Große Persönlichkeit")
            p = civ.getMousePressedAtPossibleGameMapPosition()
            if p is not None:
                self.getGameMap().setBusinessObject(self.gameStep.getChosenObj(), p.getX(), p.getY())
                self.gameStep.setChosenObj([civ.getPioneer(0)])
                self.gameStep.setStep(EGameStep.SET_PIONEER)
        elif self.isInStep(EGameStep.SET_PIONEER):
            self.gameStep.expectGameMapPosition("Pionier")
            p = civ.getMousePressedAtPossibleGameMapPosition()
            if p is not None:
                self.getGameMap().setFigures(self.gameStep.getChosenObj(), p.getX(), p.getY())
                self.gameStep.setChosenObj([civ.getArmy(0)])
                self.gameStep.setStep(EGameStep.SET_ARMY_NR1)
        elif self.isInStep(EGameStep.SET_ARMY_NR1):
            self.gameStep.expectGameMapPosition("Armee - 01")
            p = civ.getMousePressedAtPossibleGameMapPosition()
            if p is not None:
                self.getGameMap().setFigures(self.gameStep.getChosenObj(), p.getX(), p.getY())
                if civEnum == ECivilization.RUSSIA:
                    self.gameStep.setChosenObj([civ.getArmy(6)])
                    self.gameStep.setStep(EGameStep.SET_ARMY_NR2)
                else:
                    self.gameStep.setStep(EGameStep.COUNT_TRADING_POINTS)
        elif self.isInStep(EGameStep.SET_ARMY_NR2):
            self.gameStep.expectGameMapPosition("Armee - 02")
            p = civ.getMousePressedAtPossibleGameMapPosition()
            if p is not None:
                self.getGameMap().setFigures(self.gameStep.getChosenObj(), p.getX(), p.getY())
                self.gameStep.setStep(EGameStep.COUNT_TRADING_POINTS)
        elif self.isInStep(EGameStep.COUNT_TRADING_POINTS):
            civ.countTradingPoints()
            self.gameStep.setNextCivilization(False)
            if self.gameStep.isRoundCompleted():
                self.gameStep.setStepAndSection(EGameStep.GENERAL_SELECT, EGameSection.START_ROUND)
            else:
                self.gameStep.setStep(EGameStep.MARK_SQUARES_FOR_HIGHLIGHTING_CITY)

    def isInStep(self, step):
        return self.gameStep.getStep() == step

    def getGameMap(self):
        return self.game.getGameMap()
