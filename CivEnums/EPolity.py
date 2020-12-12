from enum import Enum


class EPolity(Enum):

    def __init__(self, na, img):
        self.polityName = na
        self.imgName = img

    def getImgName(self):
        return self.imgName

    ANARCHY = ("Arnachie", "Arnachy")
    FUNDAMENTALISM = ("Fundamentalismus", "Fundamentalism")
    MONARCHY = ("Monarchie", "Monarchy")
    FEUDALISM = ("Feudalismus", "Feudalism")
    DEMOCRACY = ("Demokratie", "Democracy")
    COMMUNISM = ("Kommunismus", "Communism")
    DESPOTISM = ("Despotismus", "Despotism")
    REPUBLIC = ("Republik", "Republic")