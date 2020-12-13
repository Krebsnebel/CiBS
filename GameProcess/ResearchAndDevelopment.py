from GameProcess.EGameStep import EGameStep


"""
this class handles the research and development process (phase 5)
"""


class ResearchAndDevelopment:

    def __init__(self, gameStep):
        self.gameStep = gameStep

    def execute(self):
        if self.isInStep(EGameStep.CHOOSE_RESEARCH):
            pass
        elif self.isInStep(EGameStep.SWIPE_RESEARCH):
            pass
        elif self.isInStep(EGameStep.CONFIRM_RESEARCH):
            pass
        elif self.isInStep(EGameStep.SWITCH_CIVILIZATION):
            pass

    def isInStep(self, step):
        return self.gameStep.get() == step
