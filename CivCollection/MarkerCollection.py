from CivEnums.EConstants import EConstants
from CivEnums.ENote import ENote
from CivEnums.EResource import EResource
from CivObjects.Marker import Marker


"""
this class is a collection of different markers on market map
resource, cottage, barbarian, coin and culture markers collected and - if necessary - shuffled (ToDo) here
depending of move of each player markers can be taken from marker pile (ToDo)
there is a function to draw the marker piles on market place (ToDo)
"""


class MarkerCollection:

    def __init__(self, imgInfoMarketMap, num_player):
        self.imgInfo = imgInfoMarketMap
        self.wheat = []
        self.iron = []
        self.silk = []
        self.incense = []
        self.cottage = []
        self.barbarian = []
        self.coin = EConstants.NUMBER_COINS.value
        self.culture = EConstants.NUMBER_CULTURE.value

        for i in range(2):
            self.barbarian.append(Marker(ENote.BARBARIAN, EResource.GREAT_PERSON))
            self.barbarian.append(Marker(ENote.BARBARIAN, EResource.URANIUM))
            self.cottage.append(Marker(ENote.COTTAGE, EResource.IRON))

        for i in range(3):
            self.barbarian.append(Marker(ENote.BARBARIAN, EResource.SPY))
            self.barbarian.append(Marker(ENote.BARBARIAN, EResource.IRON))
            self.cottage.append(Marker(ENote.COTTAGE, EResource.SPY))

        for i in range(num_player):
            self.wheat.append(Marker(ENote.RESOURCE, EResource.WHEAT))
            self.iron.append(Marker(ENote.RESOURCE, EResource.IRON))
            self.silk.append(Marker(ENote.RESOURCE, EResource.SILK))
            self.incense.append(Marker(ENote.RESOURCE, EResource.INCENSE))

        for i in range(5):
            self.cottage.append(Marker(ENote.COTTAGE, EResource.WHEAT))
            self.cottage.append(Marker(ENote.COTTAGE, EResource.SILK))
            self.cottage.append(Marker(ENote.COTTAGE, EResource.INCENSE))
