import pygame

from CivCollection.Game import Game
from CivCollection.MapTileCollection import MapTileCollection
from CivCollection.MarketMap import MarketMap
from CivEnums.EGameSection import EGameSection
from CivObjects.CivPossibilities import CivPossibilities
from Game.CityAdministration import CityAdministration
from Game.GameStep import GameStep
from Game.Movement import Movement
from Game.PrepareGame import PrepareGame
from Game.ResearchAndDevelopment import ResearchAndDevelopment
from Game.StartOfRound import StartOfRound
from Game.Trade import Trade


"""
this class is the overall class of the whole game process
in this class all subclasses of game phases are defined
"""


class GameProcessManager:

    def __init__(self, playerColor, imgInfoGame):
        self.FPS = 6
        self.clock = pygame.time.Clock()
        self.numberOfPlayer = len(playerColor)
        self.gameImgInfo = imgInfoGame
        self.mapTileCollection = MapTileCollection(imgInfoGame.getGameMap())

        self.marketMap = MarketMap(imgInfoGame.getMarketMap(), self.numberOfPlayer)
        self.game = Game(imgInfoGame, self.marketMap, playerColor, self.mapTileCollection)
        self.game.setGame(self.mapTileCollection)

        self.civsPossibilities = []
        civs = self.game.getCivilizations()
        for i in range(self.numberOfPlayer):
            self.civsPossibilities.append(CivPossibilities(self.game.getGameMap(), civs[i]))
            self.civsPossibilities[i].setPointsForKapitol()

        self.businessObjectCollection = self.marketMap.getBusinessObjectCollection()

        self.gameStep = GameStep(imgInfoGame, self.game.getCivilizations(), self.civsPossibilities, self.numberOfPlayer)
        self.prepareGame = PrepareGame(self.gameStep, self.game, self.businessObjectCollection)
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
        return self.gameStep.getGameSection() == section

    def getNumberOfPlayer(self):
        return self.numberOfPlayer

    def getGameMap(self):
        return self.game.getGameMap()

    def getGameStep(self):
        return self.gameStep

    def draw(self, window):
        self.game.draw(window)
