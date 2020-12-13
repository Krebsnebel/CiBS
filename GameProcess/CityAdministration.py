from GameProcess.EGameStep import EGameStep


"""
this class handles the city administration (phase 3)
"""


class CityAdministration:

    def __init__(self, gameStep):
        self.gameStep = gameStep

    def execute(self):
        if self.isInStep(EGameStep.SET_STRUCTURE):
            pass
        elif self.isInStep(EGameStep.SET_FIGURE):
            pass
        elif self.isInStep(EGameStep.ARM_MILITARY_UNIT):
            pass
        elif self.isInStep(EGameStep.MINING_RESOURCE):
            pass
        elif self.isInStep(EGameStep.SWITCH_CIVILIZATION):
            pass

    def isInStep(self, step):
        return self.gameStep.get() == step
