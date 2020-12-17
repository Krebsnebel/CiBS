from Game.Game import Game
from CivEnums.EGameSection import EGameSection
from GameProcess.CityAdministration import CityAdministration
from GameProcess.GameStep import GameStep
from GameProcess.Movement import Movement
from GameProcess.PrepareGame import PrepareGame
from GameProcess.ResearchAndDevelopment import ResearchAndDevelopment
from GameProcess.StartOfRound import StartOfRound
from GameProcess.Trade import Trade


"""
this class is the overall class of the whole game process
in this class all subclasses of game phases are defined
"""


class GameProcessManager:

    def __init__(self, playerColor, gameImgInfo):
        self.numberOfPlayer = len(playerColor)

        self.gameImgInfo = gameImgInfo
        self.gameStep = GameStep(playerColor, gameImgInfo)
        self.game = Game(self.gameImgInfo, playerColor, self.gameStep)

        self.gameStep.setCivilizations(self.game.getCivilizations())
        self.prepareGame = PrepareGame(self.gameStep, self.game)
        self.startOfRound = StartOfRound(self.gameStep)
        self.trade = Trade(self.gameStep)
        self.cityAdministration = CityAdministration(self.gameStep)
        self.movement = Movement(self.gameStep)
        self.researchAndDevelopment = ResearchAndDevelopment(self.gameStep)

    def execute(self):
        if self.isInSection(EGameSection.PREPARE_GAME):
            self.prepareGame.execute()
        elif self.isInSection(EGameSection.START_ROUND):
            self.startOfRound.execute()
        elif self.isInSection(EGameSection.TRADE):
            self.trade.execute()
        elif self.isInSection(EGameSection.CITY_ADMINISTRATION):
            self.cityAdministration.execute()
        elif self.isInSection(EGameSection.MOVEMENT):
            self.movement.execute()
        elif self.isInSection(EGameSection.RESEARCH):
            self.researchAndDevelopment.execute()

    def isInSection(self, section):
        return self.gameStep.getSection() == section

    def getNumberOfPlayer(self):
        return self.numberOfPlayer

    def getGameMap(self):
        return self.game.getGameMap()

    def getGameStep(self):
        return self.gameStep

    def draw(self, window):
        self.game.draw(window)
