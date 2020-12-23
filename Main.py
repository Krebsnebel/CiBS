from CivEnums.EColor import EColor
from Drawing.GameMapVisualization import GameMapVisualization


"""
main class starts the game
"""

playerColor = [EColor.BLUE, EColor.GREEN, EColor.RED, EColor.YELLOW]
# playerColor = [EColor.BLUE, EColor.GREEN, EColor.RED]
# playerColor = [EColor.BLUE, EColor.GREEN]

gameMapVisu = GameMapVisualization(playerColor)

gameMapVisu.startVisualization()



