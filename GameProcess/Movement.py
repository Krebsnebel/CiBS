from GameProcess.EGameStep import EGameStep


"""
this class handles the movement process (phase 4)
"""


class Movement:

    def __init__(self, gameStep):
        self.gameStep = gameStep

    def execute(self):
        if self.isInStep(EGameStep.CHOOSE_SQUARE):
            pass
        elif self.isInStep(EGameStep.CHOOSE_FIGURE):
            pass
        elif self.isInStep(EGameStep.SET_DESTINATION_SQUARE):
            pass
        elif self.isInStep(EGameStep.SWITCH_CIVILIZATION):
            pass

    def isInStep(self, step):
        return self.gameStep.get() == step
