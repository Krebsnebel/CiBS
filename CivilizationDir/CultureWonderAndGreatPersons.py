from CivEnums.EConstants import EConstants
from CivEnums.ECulturalEvent import ECulturalEvent
from CivEnums.EGreatPerson import EGreatPerson
from CivEnums.ERotation import ERotation
from CivEnums.EWonder import EWonder
from CivObjects.CulturalEvent import CulturalEvent
from CivObjects.GreatPerson import GreatPerson
from CivObjects.Position import Position
from CivObjects.Wonder import Wonder
from Drawing.EImageObject import EImageObject


class CultureWonderAndGreatPersons:

    def __init__(self, civ, imgInfoCiv):
        self.civilization = civ
        self.imgInfo = imgInfoCiv
        self.cultureCards = []
        self.wonderCards = []
        self.artistMarker = []
        self.builderMarker = []
        self.generalMarker = []
        self.humanitarianMarker = []
        self.industrialistMarker = []
        self.scientistMarker = []

        self.wonderCards.append(Wonder(EWonder.THE_ORACLE))
        self.wonderCards[0].setVisible(True)
        self.wonderCards.append(Wonder(EWonder.THE_LOUVRE))
        self.wonderCards[1].setVisible(True)
        self.wonderCards.append(Wonder(EWonder.OPERA_HOUSE_OF_SIDNEY))
        self.wonderCards[2].setVisible(True)

        self.artistMarker.append(GreatPerson(EGreatPerson.ARTIST))
        self.artistMarker[0].setVisible(True)
        self.artistMarker.append(GreatPerson(EGreatPerson.ARTIST))
        self.artistMarker[1].setVisible(True)
        self.artistMarker.append(GreatPerson(EGreatPerson.ARTIST))
        self.artistMarker[2].setVisible(True)

        self.builderMarker.append(GreatPerson(EGreatPerson.BUILDER))
        self.builderMarker[0].setVisible(True)
        self.builderMarker.append(GreatPerson(EGreatPerson.BUILDER))
        self.builderMarker[1].setVisible(True)
        self.builderMarker.append(GreatPerson(EGreatPerson.BUILDER))
        self.builderMarker[2].setVisible(True)

        self.industrialistMarker.append(GreatPerson(EGreatPerson.INDUSTRIALIST))
        self.industrialistMarker[0].setVisible(True)
        self.industrialistMarker.append(GreatPerson(EGreatPerson.INDUSTRIALIST))
        self.industrialistMarker[1].setVisible(True)
        self.industrialistMarker.append(GreatPerson(EGreatPerson.INDUSTRIALIST))
        self.industrialistMarker[2].setVisible(True)

        self.humanitarianMarker.append(GreatPerson(EGreatPerson.HUMANITARIAN))
        self.humanitarianMarker[0].setVisible(True)
        self.humanitarianMarker.append(GreatPerson(EGreatPerson.HUMANITARIAN))
        self.humanitarianMarker[1].setVisible(True)
        self.humanitarianMarker.append(GreatPerson(EGreatPerson.HUMANITARIAN))
        self.humanitarianMarker[2].setVisible(True)

        self.scientistMarker.append(GreatPerson(EGreatPerson.SCIENTIST))
        self.scientistMarker[0].setVisible(True)
        self.scientistMarker.append(GreatPerson(EGreatPerson.SCIENTIST))
        self.scientistMarker[1].setVisible(True)
        self.scientistMarker.append(GreatPerson(EGreatPerson.SCIENTIST))
        self.scientistMarker[2].setVisible(True)

        self.generalMarker.append(GreatPerson(EGreatPerson.GENERAL))
        self.generalMarker[0].setVisible(True)
        self.generalMarker.append(GreatPerson(EGreatPerson.GENERAL))
        self.generalMarker[1].setVisible(True)
        self.generalMarker.append(GreatPerson(EGreatPerson.GENERAL))
        self.generalMarker[2].setVisible(True)

        self.cultureCards.append(CulturalEvent(ECulturalEvent.REVOLTING_CITIZENS_1))
        self.cultureCards[0].setVisible(True)
        self.cultureCards.append(CulturalEvent(ECulturalEvent.DISORIENTED))
        self.cultureCards[1].setVisible(True)
        self.cultureCards.append(CulturalEvent(ECulturalEvent.REVOLTING_CITIZENS_2))
        self.cultureCards[2].setVisible(True)
        self.cultureCards.append(CulturalEvent(ECulturalEvent.CATASTROPHE))
        self.cultureCards[3].setVisible(True)
        self.cultureCards.append(CulturalEvent(ECulturalEvent.LOST))
        self.cultureCards[4].setVisible(True)
        self.cultureCards.append(CulturalEvent(ECulturalEvent.DISASTER))
        self.cultureCards[5].setVisible(True)
        self.cultureCards.append(CulturalEvent(ECulturalEvent.PRESIDENT_HOLIDAY))
        self.cultureCards[6].setVisible(True)
        self.cultureCards.append(CulturalEvent(ECulturalEvent.DISPLACED))
        self.cultureCards[7].setVisible(True)

    def draw(self, window):
        scale = self.imgInfo.getScale()

        for idx in range(len(self.wonderCards)):
            imgObj = None
            if idx == 0:
                imgObj = EImageObject.WONDER_CARD_CIV_POS_1
            elif idx == 1:
                imgObj = EImageObject.WONDER_CARD_CIV_POS_2
            elif idx == 2:
                imgObj = EImageObject.WONDER_CARD_CIV_POS_3

            pos = self.imgInfo.getImgPosOf(imgObj, True, False)
            resize = imgObj.getResize()
            self.wonderCards[idx].drawCard(window, ERotation.NO_ROTATION, pos, resize, scale)

        delta = EConstants.DELTA_MARKER_BUILDINGS_STACK.value
        self.drawStack(window, self.artistMarker, EImageObject.ARTIST_MARKER_CIV, delta)
        self.drawStack(window, self.builderMarker, EImageObject.BUILDER_MARKER_CIV, delta)
        self.drawStack(window, self.industrialistMarker, EImageObject.INDUSTRIALIST_MARKER_CIV, delta)
        self.drawStack(window, self.generalMarker, EImageObject.GENERAL_MARKER_CIV, delta)
        self.drawStack(window, self.scientistMarker, EImageObject.SCIENTIST_MARKER_CIV, delta)
        self.drawStack(window, self.humanitarianMarker, EImageObject.HUMANITARIAN_MARKER_CIV, delta)
        self.drawCultureCards(window)

    def drawCultureCards(self, window):
        scale = self.imgInfo.getScale()
        resize = EImageObject.CULTURE_CARDS_CIV.getResize()
        for i in range(len(self.cultureCards)):
            cardPos = self.imgInfo.getImgPosOfCultureCard(True, False, i)
            self.cultureCards[i].draw(window, ERotation.NO_ROTATION, cardPos, resize, scale)

    def drawStack(self, window, stack, imgObj, s):
        scale = self.imgInfo.getScale()
        i = 0
        resize = imgObj.getResize()
        stackPos = self.imgInfo.getImgPosOf(imgObj, True, False)
        for obj in stack:
            pos = Position(stackPos.getX() + i, stackPos.getY() - i)
            obj.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
            i = i + s
