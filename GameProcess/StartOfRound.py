from Drawing.EImageObject import EImageObject
from GameProcess.EGameStep import EGameStep


"""
this class handles the start of round (phase 1)
"""


class StartOfRound:
    
    def __init__(self, gameStep, game):
        self.gameStep = gameStep
        self.game = game
        self.polityOfCivilizations = self.game.getPolityOfCivilizations()
        self.politySwitched = False

    def execute(self):
        civ = self.gameStep.getCivilization()
        civEnum = civ.getCivilizationEnum()
        if self.isInStep(EGameStep.GENERAL_SELECT):
            opt = civ.getValidChoiceWhileMousePressed()
            if opt is not None:
                if opt.getImgObj() == EImageObject.POLITY:
                    self.gameStep.setStep(EGameStep.SELECT_POLITY)
                    self.polityOfCivilizations.setPolitiesOfCiv(civEnum, self.politySwitched)
        elif self.isInStep(EGameStep.SELECT_POLITY):
            if self.polityOfCivilizations.isLeftMouseButtonPressed():
                opt = self.polityOfCivilizations.getValidChoiceWhileMousePressed()
                if opt is not None:
                    polPos = opt.getPositionOfMap()
                    self.polityOfCivilizations.setNewPolity(polPos)
                    self.politySwitched = True
                self.polityOfCivilizations.setPolitiesOfCiv(None, self.politySwitched)
                self.gameStep.setStep(EGameStep.GENERAL_SELECT)
        elif self.isInStep(EGameStep.WONDER_SKILL_SELECTED):
            pass
        elif self.isInStep(EGameStep.CULTURE_SKILL_SELECTED):
            pass
        elif self.isInStep(EGameStep.RESEARCH_SKILL_SELECTED):
            pass
        elif self.isInStep(EGameStep.SET_CITY):
            pass
        elif self.isInStep(EGameStep.SWITCH_CIVILIZATION):
            pass

    def isInStep(self, step):
        return self.gameStep.getStep() == step

