from CivEnums.EColor import EColor
from Drawing.GameMapVisualization import GameMapVisualization


"""
main class starts the game
"""


playerColor = [EColor.BLUE, EColor.GREEN, EColor.RED, EColor.YELLOW]

gameMapVisu = GameMapVisualization(playerColor)

gameMapVisu.startVisualization()



