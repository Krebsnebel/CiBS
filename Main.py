from CivEnums.EColor import EColor
from Drawing.GameMapVisualization import GameMapVisualization


"""
main class starts the game
"""


playerColor = [EColor.BLUE, EColor.GREEN, EColor.RED, EColor.YELLOW]

gameMapVisu = GameMapVisualization(playerColor)

gameMapVisu.startVisualization()


#fig = Figure(EFigure.ARMY, ECivilization.RUSSIA, EColor.YELLOW)
#figures = [fig]

#print(isinstance(figures, List))


#imgBack = pygame.image.load("Material/Civilizations/Civilization_Back.jpg")
#print(imgBack.get_height())




