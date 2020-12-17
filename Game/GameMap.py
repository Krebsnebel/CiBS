from typing import List

from CivEnums.ECity import ECity
from CivEnums.ECivilization import ECivilization
from CivEnums.EException import EException
from CivEnums.EFigure import EFigure
from CivEnums.ENote import ENote
from CivEnums.EPermission import EPermission
from CivEnums.ERotation import ERotation
from CivEnums.ETerrain import ETerrain
from CivEnums.EVisibility import EVisibility
from CivObjects.Building import Building
from CivObjects.BusinessObject import BusinessObject
from CivObjects.DisasterMarker import DisasterMarker
from CivObjects.Figure import Figure
from CivObjects.Position import Position
from CivObjects.Wonder import Wonder


"""
this class is responsible for build up game map, make checks whether setting object is possible or not
following functions are defined
* is putting object on square possible
* is putting object on terrain possible
* is putting object in city possible
* is putting figure on square possible
* is putting disaster marker on square possible
* is putting kapitol on square possible
* is putting town on square currently possible
* is putting town on square possible
* several getters and setters
* refresh potentially town positions
* mark and clear squares for highlighting
* draw function to draw all map tiles
* get square with coordinate
* set game
* set business object, city and figures
* set outskirt
* print map and line of square
* find map tile
* get city
"""


def isPuttingObjectInCityPossible(obj, s, city, civ):
    if city is None:
        # print("Hier gibt es keine Stadt wo gebaut werden kann")
        return False
    if city.getCivilization() is not civ:
        # print("Das Wirtschaftsobjekt kann nicht in eine fremde Stadt gebaut werden")
        return False
    if isinstance(obj, Wonder):
        if city.isWonderInOutskirt():
            # print("Es gibt schon ein Wunder in der Stadt")
            return False
        else:
            return True
    if isinstance(obj, Building):
        if obj.isLabeledUnique():
            if city.isUniqueBuildingThere():
                # print("Es gibt schon ein einzigartiges Gebäude in der Stadt")
                return False
            else:
                return True
    if s.getDisasterMarker() is not None:
        # print("Auf einem Katastrophenmarker kann nicht gebaut werden")
        return False
    return True


def isPuttingFigureOnSquarePossible(figures, s, n_max, exception):
    if figures is None or len(figures) == 0:
        # print("keine gültige Figurenübergabe bei Funktion isPuttingFigureOnSquare()")
        return False
    if n_max <= len(figures):
        # print("nicht möglich, da Figurenlimit #01")
        return False
    ftype = figures[0].getType()
    civ = figures[0].getCivilization()
    for f in figures:
        if ftype is not f.getType():
            # print("Figuren verschiedner Typen")
            return False
        if civ is not f.getCivilization():
            # print("Figuren verschiedner Civilisationen")
            return False
    mk = s.getMarker()
    if mk is not None:
        mkt = mk.getType()
        if ftype == EFigure.PIONEER:
            if mkt is ENote.COTTAGE:
                if exception is not EException.PIONEER_DISCOVER_COTTAGE:
                    # print("Deine Pioniere können keine Hütten erkunden")
                    return False
            elif mkt is ENote.COTTAGE:
                # print("Pioniere können keine Barbarendörfer erobern")
                return False
    sCiv = s.getCivOfFigures()
    sArmy = s.getArmies()
    sPio = s.getPioneers()
    if sCiv is civ:
        if n_max < len(sArmy) + len(sPio) + len(figures):
            # print("nicht möglich, da Figurenlimit #02")
            return False
    elif sCiv is not ECivilization.NONE:
        if ftype == EFigure.PIONEER:
            # print("Pioniere können keine gegnerische Figuren angreifen")
            return False
    city = s.getCity()
    if city is not None:
        if ftype == EFigure.PIONEER:
            if city.getCivilization() is not civ:
                # print("Pioniere können keine Städte angreifen")
                return False
            else:
                # print("Pioniere können nicht in die eigene Stadt einziehen")
                return False
        else:
            if city.getCivilization() is civ:
                # print("Armeen können nicht in die eigene Stadt einziehen")
                return False
    return True


def isPuttingDisasterMarkerOnSquarePossible(s):
    if s.getCity() is not None:
        # print("Der Katastrophenmarker kann nicht statt einer Stadt gesetzt werden")
        return False
    bo = s.getBusinessObject()
    if isinstance(bo, Building):
        # print("Der Katastrophenmarker kann nicht statt einem Gebäude gesetzt werden")
        return False
    if isinstance(bo, Wonder):
        # print("Der Katastrophenmarker kann nicht statt einem Wunder gesetzt werden")
        return False
    return True


class GameMap:

    def __init__(self, ImgInfoGameMap):
        self.imgInfo = ImgInfoGameMap
        self.map = []
        self.numberOfPlayer = 0
        self.numSquaresX = 0
        self.numSquaresY = 0

        self.potentiallyPointsForTown = []

    def isObjectOnTerrainPermitted(self, x, y, permission, temporary):
        terrain = self.getSquare(x, y).getTerrain()
        if permission == EPermission.STOP_ON_WATER:
            return True
        elif permission == EPermission.MOVE_OVER_WATER:
            if not temporary and terrain == ETerrain.SEA:
                # print("You cannot stop on water")
                return False
            else:
                return True
        elif permission == EPermission.ALL_EXCEPT_WATER:
            if terrain == ETerrain.SEA:
                # print("You cannot stop/build on water")
                return False
            else:
                return True
        elif permission == EPermission.ALL_EXCEPT_WATER_AND_MOUNTAIN:
            if terrain == ETerrain.SEA or terrain == ETerrain.MOUNTAIN:
                # print("You cannot build on water or mountain")
                return False
            else:
                return True
        elif permission == EPermission.ONLY_DESERT:
            if terrain == ETerrain.DESERT:
                return True
            else:
                # print("You can only build at desert")
                return False
        elif permission == EPermission.ONLY_GRASSLAND:
            if terrain == ETerrain.GRASSLAND:
                return True
            else:
                # print("You can only build at grassland")
                return False
        elif permission == EPermission.ONLY_WATER:
            if terrain == ETerrain.SEA:
                return True
            else:
                # print("You can only build at sea")
                return False
        elif permission == EPermission.ONLY_MOUNTAIN:
            if terrain == ETerrain.MOUNTAIN:
                return True
            else:
                # print("You can only build at mountain")
                return False
        elif permission == EPermission.ONLY_FOREST:
            if terrain == ETerrain.FOREST:
                return True
            else:
                # print("You can only build at forest")
                return False
        else:
            return False

    def getPotentiallyPointsForTown(self):
        return self.potentiallyPointsForTown

    def getImgInfo(self):
        return self.imgInfo

    # refresh is necessary under following conditions:
    # * disaster marker is set
    # * map tile is discovered
    # * cottage / barbarian marker is occupied
    # * new city is built up
    def refreshPotentiallyTownPositions(self):
        self.potentiallyPointsForTown = []
        for y in range(16):
            for x in range(16):
                possible = True
                s = self.getSquare(x, y)
                if s is None:
                    # print("Es gibt hier kein Terrain")
                    possible = False
                m = self.findMapTile(x, y)
                if possible and m.getVisibility() == EVisibility.FOR_NOBODY:
                    # print("The Terrain is not discovered")
                    possible = False
                if possible:
                    # template town which represents all towns of civilizations
                    possible = self.isPuttingTownOnSquarePossible(s)
                if possible:
                    self.potentiallyPointsForTown.append(s)

    def clearSquaresForHighlighting(self):
        self.imgInfo.clearPossibilities()

    def markSquaresForHighlighting(self, obj, civ, n_max):
        marked = self.imgInfo.arePossibilitiesMarked()
        if not marked:
            for y in range(16):
                for x in range(16):
                    p = Position(x, y)
                    possible = self.isPuttingObjectOnSquarePossible(obj, p.getX(), p.getY(), civ, False, n_max)
                    if possible:
                        self.imgInfo.markSquareForHighlighting(p)
            self.imgInfo.finishPossibilities()

    def draw(self, window):
        for m in self.map:
            m.draw(window)

        self.imgInfo.draw(window)

    def getSquare(self, x, y):
        m = self.findMapTile(x, y)
        if m is None:
            return None
        pos = m.getPosition()
        px = pos.getX()
        py = pos.getY()
        return m.getSquare(x - px, y - py)

    def getNumSquaresX(self):
        return self.numSquaresX

    def getNumSquaresY(self):
        return self.numSquaresY

    def setGame(self, civilization, mapTileCollection):
        self.numberOfPlayer = len(civilization)
        if self.numberOfPlayer == 2:
            self.numSquaresX = 8
            self.numSquaresY = 16
            self.map.append(civilization[0].popMapTile(4, 0, ERotation.CLOCKWISE_180))
            self.map.append(civilization[1].popMapTile(0, 12, ERotation.NO_ROTATION))

            for i in range(3):
                self.map.append(mapTileCollection.popMapTile(0, 4 * i, ERotation.NO_ROTATION))

            for i in range(3):
                self.map.append(mapTileCollection.popMapTile(4, 4 * (i + 1), ERotation.NO_ROTATION))
        elif self.numberOfPlayer == 3:
            self.numSquaresX = 16
            self.numSquaresY = 16
            self.map.append(civilization[0].popMapTile(6, 0, ERotation.CLOCKWISE_180))
            self.map.append(civilization[1].popMapTile(0, 12, ERotation.CLOCKWISE_90))
            self.map.append(civilization[2].popMapTile(12, 12, ERotation.CLOCKWISE_270))

            for i in range(2):
                self.map.append(mapTileCollection.popMapTile(4 * (i + 1), 4, ERotation.NO_ROTATION))
                self.map.append(mapTileCollection.popMapTile(4 * (i + 1), 12, ERotation.NO_ROTATION))

            for i in range(3):
                self.map.append(mapTileCollection.popMapTile(4 * i + 2, 8, ERotation.NO_ROTATION))
        else:  # self.numberOfPlayer == 4
            self.numSquaresX = 16
            self.numSquaresY = 16
            self.map.append(civilization[0].popMapTile(0, 0, ERotation.CLOCKWISE_180))
            self.map.append(civilization[1].popMapTile(12, 0, ERotation.CLOCKWISE_180))
            self.map.append(civilization[2].popMapTile(0, 12, ERotation.NO_ROTATION))
            self.map.append(civilization[3].popMapTile(12, 12, ERotation.NO_ROTATION))

            for i in range(2):
                self.map.append(mapTileCollection.popMapTile(4 * (i + 1), 0, ERotation.NO_ROTATION))
                self.map.append(mapTileCollection.popMapTile(4 * (i + 1), 12, ERotation.NO_ROTATION))

            for i in range(4):
                self.map.append(mapTileCollection.popMapTile(4 * i, 4, ERotation.NO_ROTATION))
                self.map.append(mapTileCollection.popMapTile(4 * i, 8, ERotation.NO_ROTATION))

        for i in range(len(self.map)):
            print(self.map[i].label.getSign() + ": " +
                  str(self.map[i].position.getX()) + ", " + str(self.map[i].position.getY()))

    def isPuttingObjectOnSquarePossible(self, obj, x, y, civ, temp, n_max):
        s = self.getSquare(x, y)
        if s is None:
            # print("Es gibt hier kein Terrain")
            return False
        m = self.findMapTile(x, y)
        if m.getVisibility() == EVisibility.FOR_NOBODY:
            # print("The Terrain is not discovered")
            return False
        bt = self.isPuttingObjectOnTerrainPossible(obj, s, temp)
        if not bt:
            # print("Setzen des Objekts aufgrund des Terrain nicht möglich")
            return False
        if isinstance(obj, BusinessObject):
            city = self.getCity(x, y)
            bu = isPuttingObjectInCityPossible(obj, s, city, civ)
        else:
            bu = True
        if not bu:
            # print("Setzen des Wirtschaftsobjekts nicht möglich")
            return False
#        if isinstance(obj, City):
#            bc = self.isPuttingKapitolOnSquarePossible(obj, s, m)
#        else:
#            bc = True
        bc = True
        if not bc:
            # print("Setzen der Stadt nicht möglich")
            return False
        if isinstance(obj, List) and isinstance(obj[0], Figure):
            city = self.getCity(x, y)
            if obj[0].getPosition() is None:
                bf1 = isPuttingObjectInCityPossible(obj[0], s, city, civ)
            else:
                bf1 = True
            bf2 = isPuttingFigureOnSquarePossible(obj, s, n_max, civ.getException())
            bf = bf1 and bf2
        else:
            bf = True
        if not bf:
            # print("Setzen der Figuren nicht möglich")
            return False
        if isinstance(obj, DisasterMarker):
            bd = isPuttingDisasterMarkerOnSquarePossible(s)
        else:
            bd = True
        if not bd:
            # print("Setzen des Katastrophenmarkers nicht möglich")
            return False
        return True




    def isPuttingKapitolOnSquarePossible(self, city, s, m):
        if city.getType() == ECity.KAPITOL:
            if m.getCivilization() is not city.getCivilization():
                # print("Das ist nicht das Heimatspielteil! Hauptstädte müssen in Heimatspielteile gebaut werden")
                return False
        p = s.getPosition()
        x = p.getX()
        y = p.getY()
        for j in range(-1, 2):
            for i in range(-1, 2):
                su = self.getSquare(x + i, y + j)
                mu = self.findMapTile(x + i, y + j)
                if su is None:
                    # print("Es gibt hier kein Terrain bei Feld x = " + str(x + i) + ", y = " + str(y + j))
                    return False
                if mu.getVisibility() == EVisibility.FOR_NOBODY:
                    # print("The Terrain is not discovered")
                    return False
        return True

    def isPuttingTownOnSquareCurrentlyPossible(self, s, ownCiv):
        p = s.getPosition()
        x = p.getX()
        y = p.getY()
        for j in range(-1, 2):
            for i in range(-1, 2):
                su = self.getSquare(x + i, y + j)
                sCiv = su.getCivOfFigures()
                if sCiv is not ECivilization.NONE and sCiv is not ownCiv:
                    # print("Es sind gegnerische Figuren in der Umgebung")
                    return False
        return True

    def isPuttingTownOnSquarePossible(self, s):
        p = s.getPosition()
        x = p.getX()
        y = p.getY()
        for j in range(-2, 3):
            for i in range(-2, 3):
                su = self.getSquare(x + i, y + j)
                if -1 <= i <= 1 and -1 <= j <= 1:
                    if su is None:
                        # print("Es gibt hier kein Terrain bei Feld x = " + str(x + i) + ", y = " + str(y + j))
                        return False
                    m = self.findMapTile(x + i, y + j)
                    if m.getVisibility() == EVisibility.FOR_NOBODY:
                        # print("The Terrain is not discovered")
                        return False
                    mk = su.getMarker()
                    if mk is not None:
                        if mk.getType() == ENote.BARBARIAN:
                            # print("There is a barbarian marker nearby")
                            return False
                        elif mk.getType() == ENote.COTTAGE:
                            # print("There is a cottage marker nearby")
                            return False
                    d = su.getDisasterMarker()
                    if d is not None:
                        # print("There is a disaster marker nearby")
                        return False
                if su is not None:
                    c = su.getCity()
                    if c is not None:
                        # print("To close to a city of your own / of another player")
                        return False
        return True

    def setBusinessObject(self, obj, x, y):
        s = self.getSquare(x, y)
        if s is None:
            # print("Auf diesem Feld gibt es kein Terrain - 02")
            return False
        s.setBusinessObject(obj)
        return True

    def setFigures(self, fig, x, y):
        s = self.getSquare(x, y)
        if s is None:
            # print("Auf diesem Feld gibt es kein Terrain - 03")
            return False
        return s.setFigures(fig)

    def setCity(self, city, x, y):
        s = self.getSquare(x, y)
        if s is None:
            # print("Auf diesem Feld gibt es kein Terrain - 04")
            return False
        s.setCity(city)
        self.setOutskirt(city, x, y)
        return True

    def setOutskirt(self, city, x, y):
        for j in range(-1, 2):
            for i in range(-1, 2):
                if i != 0 or j != 0:
                    s = self.getSquare(x + i, y + j)
                    if s is None:
                        return
                    city.setOutskirt(s)

    def printMap(self):
        for y in range(16):
            for row in range(3):
                for x in range(16):
                    self.printLineOfSquare(x, y, row)
                print()

    def printLineOfSquare(self, x, y, row):
        m = self.findMapTile(x, y)
        if m is None:
            print("    ", end="")
        else:
            pos = m.getPosition()
            px = pos.getX()
            py = pos.getY()
            m.printLineOfSquare(x - px, y - py, row)

    def findMapTile(self, x, y):
        for m in self.map:
            pos = m.getPosition()
            if pos is not None:
                px = pos.getX()
                py = pos.getY()
                if px <= x < px + 4 and py <= y < py + 4:
                    return m
        return None

    def getCity(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    s = self.getSquare(x + i, y + j)
                    if s is not None:
                        c = s.getCity()
                        if c is not None:
                            return c
        return None
