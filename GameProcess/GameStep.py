from CivEnums.EGameSection import EGameSection
from CivObjects.Position import Position
from GameProcess.EGameStep import EGameStep

"""
this class handles the game step
"""

class GameStep:

    def __init__(self, gameImgInfo, civs, civsPoss, numPlayer):
        self.numberOfPlayer = numPlayer
        self.civilizations = civs
        self.civsPossibilities = civsPoss
        self.step = None
        self.gameSection = None
        self.mousePosition = Position(0, 0)
        self.chosenSquObj = None
        self.strForExpectedEvent = "aaa"
        self.gameImgInfo = gameImgInfo

        self.startPlayer = 0
        self.nextPlayersTurn = 0
        self.civTurn = None
        self.civPossibilitiesTurn = None
        self.roundCompleted = True
        self.setNextCivilization(False)
        self.setStepAndSection(EGameStep.MARK_SQUARES_FOR_HIGHLIGHTING_CITY, EGameSection.PREPARE_GAME)

    def setNextStep(self, obj, objType, nextStep):
        self.setGameStep(obj, objType, nextStep, self.getGameSection())

    def setGameStep(self, obj, objType, nextStep, nextSection):
        self.setChosenSquareObject(obj)
        if objType is None:
            self.clearSquaresForHighlighting()
        else:
            self.markSquaresForHighlighting(objType)
        self.setStepAndSection(nextStep, nextSection)

    def setSquareObject(self, strObj):
        self.expectGameMapPosition(strObj)
        p = self.getGameMapPosition()
        if p is not None:
            possible = self.gameImgInfo.getGameMap().isPuttingObjectOnSquarePossible(p)
            if possible:
                self.gameMapPositionUsed()
                return p
        return None

    def refreshCurrentTownPositions(self):
        for cp in self.civsPossibilities:
            cp.setCurrentPointsForTown()

    def clearSquaresForHighlighting(self):
        self.gameImgInfo.getGameMap().clearPossibilities()

    def markSquaresForHighlighting(self, objType):
        listPoints = self.civPossibilitiesTurn.getPointsOf(objType)
        self.gameImgInfo.getGameMap().markSquaresForHighlighting(listPoints)

    def markAreasInCivilizationForHighlighting(self):
        objImgList = self.civPossibilitiesTurn.getObjImgForHighlighting()
        self.civTurn.getImgInfo().markAreasInCivilizationForHighlighting(objImgList)

    def isRoundCompleted(self):
        return self.roundCompleted

    def setNextCivilization(self, startPhase):
        if self.nextPlayersTurn == self.startPlayer:
            self.roundCompleted = True
        else:
            self.roundCompleted = False
        self.civTurn = self.civilizations[self.nextPlayersTurn]
        self.civPossibilitiesTurn = self.civsPossibilities[self.nextPlayersTurn]
        self.nextPlayersTurn = (self.nextPlayersTurn + 1) % self.numberOfPlayer
        if startPhase and self.nextPlayersTurn == self.startPlayer:
            self.startPlayer = (self.startPlayer + 1) % self.numberOfPlayer
            self.nextPlayersTurn = self.startPlayer

    def setStepAndSection(self, step, section):
        self.step = step
        if self.gameSection is not section:
            self.gameSection = section
            for cp in self.civsPossibilities:
                cp.setGameSection(section)

    def getStrForExpectedEvent(self):
        return self.strForExpectedEvent

    def getGameSection(self):
        return self.gameSection

    def get(self):
        return self.step

    def getCivilization(self):
        return self.civTurn

    def getCivPossibilities(self):
        return self.civPossibilitiesTurn

    def getMousePosition(self):
        return self.mousePosition

    def setMousePosition(self, x, y):
        self.mousePosition.setPosition(x, y)
        self.gameImgInfo.setMousePositionForHighlighting(self.mousePosition)

    def expectGameMapPosition(self, strObj):
        col = self.civTurn.getColor()
        civ = self.civTurn.getCivilizationEnum()
        self.strForExpectedEvent = "Spieler " + str(col) + ", civ " + str(civ) + " - setze " + strObj + " (x/y)"
        self.gameImgInfo.getGameMap().expectGameMapPosition()

    def leftMouseButtonPressed(self):
        self.gameImgInfo.leftMouseButtonPressed(self.mousePosition)

    def setStep(self, step):
        self.step = step

    def setChosenSquareObject(self, obj):
        self.chosenSquObj = obj

    def getChosenSquareObject(self):
        return self.chosenSquObj

    def getGameMapPosition(self):
        return self.gameImgInfo.getGameMap().getGameMapPosition()

    def gameMapPositionUsed(self):
        return self.gameImgInfo.getGameMap().gameMapPositionUsed()
