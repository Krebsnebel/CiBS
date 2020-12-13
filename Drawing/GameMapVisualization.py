import pygame
from pygame.locals import *

from Game.GameProcessManager import GameProcessManager
from CivObjects.Position import Position
from Drawing.ImgInfoGame import ImgInfoGame


"""
In this class the visualization ist executed and events are requested
Due to events, decisions are made
"""


class GameMapVisualization:

    def __init__(self, playerColor):
        self.imgInfo = ImgInfoGame(len(playerColor))
        self.gameProcess = GameProcessManager(playerColor, self.imgInfo)

        pygame.init()

        # Variablen/KONSTANTEN setzen
        self.W = 1720
        self.H = 880
        self.FPS = 30
        self.SCHWARZ = (0, 0, 0)
        self.WEISS = (255, 255, 255)
        self.spielaktiv = True

        # Definieren und Öffnen eines neuen Fensters
        #self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.window = pygame.display.set_mode([self.W, self.H])
        pygame.display.set_caption("Civilization")
        self.clock = pygame.time.Clock()

    def startVisualization(self):
        spielaktiv = True
        gameStep = self.gameProcess.getGameStep()
        gameMap = self.gameProcess.getGameMap()
        # Schleife Hauptprogramm
        while spielaktiv:
            [x, y] = pygame.mouse.get_pos()
            gameStep.setMousePosition(x, y)

            self.imgInfo.shift(self.window, Position(x, y))

            # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
            for event in pygame.event.get():
                # Beenden bei [ESC] oder [X]
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    spielaktiv = False
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    gameStep.leftMouseButtonPressed()

            # Spiellogik
            self.gameProcess.execute()

            # Spielfeld löschen
            self.window.fill(self.WEISS)

            # Spielfeld/figuren zeichnen
            font = pygame.font.SysFont("comicsansms", 18)
            reqText = font.render(gameStep.getStrForExpectedEvent(), True, (0, 128, 0))
            self.gameProcess.draw(self.window)
            self.window.blit(reqText, (800, 20))

            # Fenster aktualisieren
            pygame.display.flip()
            self.clock.tick(self.FPS)
