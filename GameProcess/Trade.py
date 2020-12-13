from GameProcess.EGameStep import EGameStep


"""
this class handles the trade process (phase 2)
"""


class Trade:

    def __init__(self, gameStep):
        self.gameStep = gameStep

    def execute(self):
        if self.isInStep(EGameStep.COUNT_TRADING_POINTS):
            pass
        elif self.isInStep(EGameStep.SWITCH_CIVILIZATION):
            pass

    def isInStep(self, step):
        return self.gameStep.get() == step
