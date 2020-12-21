from random import shuffle

from CivEnums.EConstants import EConstants
from CivEnums.ECulturalEvent import ECulturalEvent
from CivEnums.ERotation import ERotation
from CivObjects.CulturalEvent import CulturalEvent
from CivObjects.Position import Position
from Drawing.EImageObject import EImageObject


"""
this class is a collection of all cultural events
cultural events of level I, II and III are collected and shuffled here
depending of move of each player, cultural event can be taken from stack (ToDo)
there is a function to draw the cultural events on market place
"""


class CulturalEventCollection:

    def __init__(self, imgInfoMarketMap):
        self.imgInfo = imgInfoMarketMap
        self.culturalEvent_I = []
        self.culturalEvent_II = []
        self.culturalEvent_III = []

        self.culturalEvent_I.append(CulturalEvent(ECulturalEvent.REVOLTING_CITIZENS_1))
        self.culturalEvent_I.append(CulturalEvent(ECulturalEvent.DISORIENTED))
        self.culturalEvent_II.append(CulturalEvent(ECulturalEvent.REVOLTING_CITIZENS_2))
        self.culturalEvent_II.append(CulturalEvent(ECulturalEvent.CATASTROPHE))
        self.culturalEvent_II.append(CulturalEvent(ECulturalEvent.LOST))
        self.culturalEvent_III.append(CulturalEvent(ECulturalEvent.DISASTER))
        self.culturalEvent_III.append(CulturalEvent(ECulturalEvent.PRESIDENT_HOLIDAY))
        self.culturalEvent_III.append(CulturalEvent(ECulturalEvent.DISPLACED))

        for i in range(2):
            self.culturalEvent_I.append(CulturalEvent(ECulturalEvent.SABOTAGE))
            self.culturalEvent_I.append(CulturalEvent(ECulturalEvent.BREAD_AND_GAMES))
            self.culturalEvent_I.append(CulturalEvent(ECulturalEvent.FAITHLESS))
            self.culturalEvent_I.append(CulturalEvent(ECulturalEvent.DROUGHT))
            self.culturalEvent_II.append(CulturalEvent(ECulturalEvent.MASS_EXODUS))
            self.culturalEvent_II.append(CulturalEvent(ECulturalEvent.DEFORESTATION))
            self.culturalEvent_II.append(CulturalEvent(ECulturalEvent.LONG_LIVE_THE_QUEEN))
            self.culturalEvent_II.append(CulturalEvent(ECulturalEvent.KNIGHT_TOURNAMENT))
            self.culturalEvent_III.append(CulturalEvent(ECulturalEvent.A_PRINCELY_GIFT))
            self.culturalEvent_III.append(CulturalEvent(ECulturalEvent.IDEASMITH))
            self.culturalEvent_III.append(CulturalEvent(ECulturalEvent.GENERAL_DESERTION))
            self.culturalEvent_III.append(CulturalEvent(ECulturalEvent.PRIME_TIME))

        for i in range(3):
            self.culturalEvent_I.append(CulturalEvent(ECulturalEvent.GIFT_FROM_A_DISTANCE))
            self.culturalEvent_I.append(CulturalEvent(ECulturalEvent.EXCHANGE_OF_IDEAS))
            self.culturalEvent_I.append(CulturalEvent(ECulturalEvent.DESPOT_HOLIDAY))
            self.culturalEvent_II.append(CulturalEvent(ECulturalEvent.GENEROUS_GIFT))
            self.culturalEvent_II.append(CulturalEvent(ECulturalEvent.SHARED_KNOWLEDGE))

        self.shuffleCards()

    def getStackLengthOfCultureCards(self, level):
        if level == 1:
            return len(self.culturalEvent_I)
        elif level == 2:
            return len(self.culturalEvent_II)
        elif level == 3:
            return len(self.culturalEvent_III)
        else:
            return -1

    def shuffleCards(self):
        shuffle(self.culturalEvent_I)
        shuffle(self.culturalEvent_II)
        shuffle(self.culturalEvent_III)

    def draw(self, window):

        resize = self.imgInfo.getResize(EImageObject.CULTURE_CARDS)

        dx = EConstants.DELTA_CULTURE_CARDS_STACK.value
        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.CULTURE_EVENT_1)
        for c in self.culturalEvent_I:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
            c.draw(window, ERotation.NO_ROTATION, pos, resize)
            delta = delta + dx

        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.CULTURE_EVENT_2)
        for c in self.culturalEvent_II:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
            c.draw(window, ERotation.NO_ROTATION, pos, resize)
            delta = delta + dx

        delta = 0
        stackPos = self.imgInfo.getImgPosOf(EImageObject.CULTURE_EVENT_3)
        for c in self.culturalEvent_III:
            pos = Position(stackPos.getX() + delta, stackPos.getY() - delta)
            c.draw(window, ERotation.NO_ROTATION, pos, resize)
            delta = delta + dx
