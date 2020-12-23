from CivEnums.ECivilization import ECivilization
from CivEnums.EFigure import EFigure
from CivEnums.ERotation import ERotation
from CivObjects.BusinessObject import BusinessObject
from CivObjects.Position import Position


"""
class Square inherits by BusinessObject
with it all properties of each square can be defined
* trading points
* production points
* culture points
* defence points
* resource
* terrain, name and sign
* position
* bonus (for additional culture point)
* additional note (e.g. for barbarian or cottage)
* object on square
** businessObject
** marker
** city
** disaster marker
* list of armies
* list of pioneers
* and its civilization
"""


class Square(BusinessObject):

    def __init__(self, terr, res, bon, note):
        tp = terr.getTradingPoints()
        pp = terr.getProductionPoints()
        if bon:
            cp = 1
        else:
            cp = 0
        dp = 0
        s = terr.getSign()
        super().__init__(tp, pp, cp, dp, res, s)
        self.position = None
        self.terrain = terr
        self.bonus = bon
        self.note = note
        self.businessObject = None
        self.marker = None
        self.city = None
        self.disasterMarker = None
        self.figureCiv = ECivilization.NONE
        self.army = []
        self.pioneer = []

    def countTradingPoints(self, civ):
        for a in self.army:
            if a.getCivilization() is not civ:
                return 0

        for p in self.pioneer:
            if p.getCivilization() is not civ:
                return 0

        if self.businessObject is not None:
            return self.businessObject.getTradingPoints()

        if self.disasterMarker is not None:
            return self.disasterMarker.getTradingPoints()

        return self.getTradingPoints()

    def drawObjectsOfSquare(self, window, imgInfo, scale):
        pos = imgInfo.getImgPosOfSquare(self.position, True, False)
        resize = imgInfo.getResizeSquareObj()
        if self.businessObject is not None:
            self.businessObject.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
        if self.city is not None:
            self.city.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
        if self.disasterMarker is not None:
            self.disasterMarker.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
        for a in self.army:
            a.draw(window, ERotation.NO_ROTATION, pos, resize, scale)
        for p in self.pioneer:
            p.draw(window, ERotation.NO_ROTATION, pos, resize, scale)

    def getDisasterMarker(self):
        return self.disasterMarker

    def setDisasterMarker(self, disaster):
        self.disasterMarker = disaster

    def getCivOfFigures(self):
        return self.figureCiv

    def setFigures(self, figures):
        if figures is None or len(figures) == 0:
            print("keine gültige Figurenübergabe bei Funktion setFigures()")
            return False
        civ = figures[0].getCivilization()
        for f in figures:
            if civ is not f.getCivilization():
                print("Figuren verschiedner Civilisationen - figures")
                return False
        if (len(self.army) > 0 or len(self.pioneer) > 0) and self.figureCiv is not civ:
            print("Auf einem Feld dürfen nicht Figuren verschiedner Civilisationen")
            return False
        self.figureCiv = civ
        for f in figures:
            f.setPosition(self.position.getX(), self.position.getY())
            if f.getType() == EFigure.PIONEER:
                self.pioneer.append(f)
            elif f.getType() == EFigure.ARMY:
                self.army.append(f)
            else:
                print("Diese Figurenart gibt es nicht")
                return False
        return True

    def getArmies(self):
        return self.army

    def getPioneers(self):
        return self.pioneer

    def getMarker(self):
        return self.marker

    def getTerrain(self):
        return self.terrain

    def setPosition(self, x, y):
        if self.position is None:
            self.position = Position(x, y)
        else:
            self.position.setPosition(x, y)

    def getPosition(self):
        return self.position

    def getBusinessObject(self):
        return self.businessObject

    def setBusinessObject(self, obj):
        self.businessObject = obj

    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city
        self.city.setPosition(self.position.getX(), self.position.getY())

    def evalTradingPoints(self):
        if self.businessObject is not None:
            return self.businessObject.getTradingPoints()
        else:
            return self.getTradingPoints()

    def evalResource(self):
        if self.businessObject is not None:
            return self.businessObject.getResource().getSign()
        else:
            return self.getResource().getSign()

    def evalDefencePoints(self):
        if self.businessObject is not None:
            return self.businessObject.getDefencePoints()
        else:
            return self.getDefencePoints()

