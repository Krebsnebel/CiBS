from CivEnums.EGameSection import EGameSection
from CivObjects.Position import Position
from GameProcess.EGameStep import EGameStep


"""
this class handles the game step
"""


class GameStep:

    def __init__(self, playerColor, imgInfoGame):
        self.imgInfo = imgInfoGame
        self.playerColor = playerColor
        self.numberOfPlayer = len(playerColor)
        self.step = None
        self.gameSection = None
        self.chosenSquObj = None
        self.strForExpectedEvent = "aaa"

        self.startPlayer = 0
        self.nextPlayersTurn = 0
        self.civTurnIdx = 0
        self.civilizations = None
        self.civTurn = None
        self.roundCompleted = True

    def setCivilizations(self, civs):
        self.civilizations = civs
        self.setNextCivilization(False)
        self.setStepAndSection(EGameStep.MARK_SQUARES_FOR_HIGHLIGHTING_CITY, EGameSection.PREPARE_GAME)

    def setStepAndSection(self, step, section):
        self.gameSection = section
        self.setStep(step)

    def setStep(self, step):
        self.step = step
        self.civTurn.calculateOptions()

    def expectGameMapPosition(self, strObj):
        col = self.civTurn.getColor()
        civ = self.civTurn.getCivilizationEnum()
        self.strForExpectedEvent = "Spieler " + str(col) + ", civ " + str(civ) + " - setze " + strObj + " (x/y)"

    def isRoundCompleted(self):
        return self.roundCompleted

    def setNextCivilization(self, startPhase):
        if self.nextPlayersTurn == self.startPlayer:
            self.roundCompleted = True
        else:
            self.roundCompleted = False
        self.civTurnIdx = self.nextPlayersTurn
        self.civTurn = self.civilizations[self.civTurnIdx]
        self.nextPlayersTurn = (self.nextPlayersTurn + 1) % self.numberOfPlayer
        if startPhase and self.nextPlayersTurn == self.startPlayer:
            self.startPlayer = (self.startPlayer + 1) % self.numberOfPlayer
            self.nextPlayersTurn = self.startPlayer

    def getStrForExpectedEvent(self):
        return self.strForExpectedEvent

    def getSection(self):
        return self.gameSection

    def getStep(self):
        return self.step

    def getCivilization(self):
        return self.civTurn

    def setChosenObj(self, obj):
        self.chosenSquObj = obj

    def getChosenObj(self):
        return self.chosenSquObj
