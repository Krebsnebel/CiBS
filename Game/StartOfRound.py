from Game.EGameStep import EGameStep


"""
this class handles the start of round (phase 1)
"""


class StartOfRound:
    
    def __init__(self, gameStep):
        self.gameStep = gameStep

    def execute(self):
        if self.isInStep(EGameStep.GENERAL_SELECT):
            pass
        elif self.isInStep(EGameStep.SELECT_POLITY):
            pass
        elif self.isInStep(EGameStep.POLITY_SELECTED):
            pass
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
        return self.gameStep.get() == step

