from random import shuffle

from CivEnums.ELabel import ELabel
from CivEnums.ECivilization import ECivilization
from CivEnums.ENote import ENote
from CivEnums.EResource import EResource
from CivEnums.ETerrain import ETerrain
from CivObjects.MapTile import MapTile
from CivObjects.Square import Square


"""
this class is a collection of all map tiles
home map tiles and other ones are collected and - if necessary - shuffled here
depending of building up game map, map tile can be taken from stack
"""


class MapTileCollection:

    def popMapTileCiv(self):
        shuffle(self.mapTilesCiv)
        return self.mapTilesCiv.pop(0)

    def popMapTile(self, x, y, rot):
        shuffle(self.mapTiles)
        self.mapTiles[0].setPosition(x, y, rot)
        return self.mapTiles.pop(0)

    def __init__(self, imgInfoGameMap):
        self.mapTiles = []
        self.mapTilesCiv = []

        # map tile Russia
        s00 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.KAPITOL_SUGGESTION)
        s13 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.FOREST, EResource.WHEAT, False, ENote.NONE)
        s31 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.MOUNTAIN, EResource.IRON, False, ENote.NONE)

        self.mapTilesCiv.append(
            MapTile(ECivilization.RUSSIA, ELabel.RUSSIA, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile Rome
        s00 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.DESERT, EResource.INCENSE, False, ENote.NONE)
        s02 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.FOREST, EResource.SILK, False, ENote.NONE)

        s10 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.MOUNTAIN, EResource.IRON, False, ENote.NONE)

        s20 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.KAPITOL_SUGGESTION)
        s23 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.SEA, EResource.WHEAT, False, ENote.NONE)
        s31 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        self.mapTilesCiv.append(
            MapTile(ECivilization.ROME, ELabel.ROME, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20, s21,
                    s22, s23, s30, s31, s32, s33))

        # map tile Germany
        s00 = Square(ETerrain.SEA, EResource.SILK, False, ENote.NONE)
        s01 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.KAPITOL_SUGGESTION)
        s13 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.MOUNTAIN, EResource.IRON, False, ENote.NONE)
        s23 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.MOUNTAIN, EResource.COIN, False, ENote.NONE)
        s31 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.GRASSLAND, EResource.WHEAT, False, ENote.NONE)

        self.mapTilesCiv.append(
            MapTile(ECivilization.GERMANY, ELabel.GERMANY, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile China
        s00 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.GRASSLAND, EResource.WHEAT, False, ENote.NONE)

        s10 = Square(ETerrain.MOUNTAIN, EResource.IRON, False, ENote.NONE)
        s11 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.KAPITOL_SUGGESTION)
        s12 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.MOUNTAIN, EResource.NONE, True, ENote.NONE)
        s31 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.SEA, EResource.SILK, False, ENote.NONE)

        self.mapTilesCiv.append(
            MapTile(ECivilization.CHINA, ELabel.CHINA, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20, s21,
                    s22, s23, s30, s31, s32, s33))

        # map tile America
        s00 = Square(ETerrain.MOUNTAIN, EResource.IRON, False, ENote.NONE)
        s01 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.MOUNTAIN, EResource.SILK, False, ENote.NONE)
        s12 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.KAPITOL_SUGGESTION)
        s13 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.MOUNTAIN, EResource.INCENSE, False, ENote.NONE)
        s23 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.FOREST, EResource.WHEAT, False, ENote.NONE)

        self.mapTilesCiv.append(
            MapTile(ECivilization.AMERICA, ELabel.AMERICA, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile Agypt
        s00 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.MOUNTAIN, EResource.INCENSE, False, ENote.NONE)

        s10 = Square(ETerrain.DESERT, EResource.WHEAT, False, ENote.NONE)
        s11 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.KAPITOL_SUGGESTION)
        s12 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.SEA, EResource.SILK, False, ENote.NONE)
        s33 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)

        self.mapTilesCiv.append(
            MapTile(ECivilization.AGYPT, ELabel.AGYPT, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20, s21,
                    s22, s23, s30, s31, s32, s33))

        # map tile 01
        s00 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.SEA, EResource.NONE, True, ENote.NONE)
        s02 = Square(ETerrain.FOREST, EResource.WHEAT, False, ENote.NONE)
        s03 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.BARBARIAN)

        s10 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)
        s22 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_01, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 02
        s00 = Square(ETerrain.MOUNTAIN, EResource.INCENSE, False, ENote.NONE)
        s01 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.DESERT, EResource.WHEAT, False, ENote.NONE)
        s03 = Square(ETerrain.SEA, EResource.NONE, False, ENote.BARBARIAN)

        s10 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.BARBARIAN)
        s12 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.COTTAGE)
        s22 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.COTTAGE)
        s31 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_02, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 03
        s00 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)
        s03 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.FOREST, EResource.INCENSE, False, ENote.NONE)
        s12 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)
        s32 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_03, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 04
        s00 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)
        s12 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.DESERT, EResource.NONE, True, ENote.NONE)
        s21 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.SEA, EResource.SILK, False, ENote.NONE)
        s23 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)
        s33 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_04, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 05
        s00 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.MOUNTAIN, EResource.IRON, False, ENote.NONE)

        s10 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)

        s20 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.COTTAGE)
        s21 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_05, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 06
        s00 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.COTTAGE)
        s02 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.DESERT, EResource.INCENSE, False, ENote.NONE)
        s21 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)
        s33 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_06, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 07
        s00 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.MOUNTAIN, EResource.IRON, False, ENote.NONE)
        s11 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)
        s12 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.BARBARIAN)

        s30 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.SEA, EResource.SILK, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_07, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 08
        s00 = Square(ETerrain.MOUNTAIN, EResource.SILK, False, ENote.NONE)
        s01 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.COTTAGE)
        s02 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)
        s23 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_08, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 09
        s00 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.BARBARIAN)
        s01 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.FOREST, EResource.WHEAT, False, ENote.NONE)
        s13 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.COTTAGE)
        s31 = Square(ETerrain.MOUNTAIN, EResource.NONE, True, ENote.NONE)
        s32 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_09, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 10
        s00 = Square(ETerrain.MOUNTAIN, EResource.IRON, False, ENote.NONE)
        s01 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)

        s20 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.BARBARIAN)
        s21 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.FOREST, EResource.NONE, True, ENote.NONE)

        s30 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_10, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 11
        s00 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.BARBARIAN)
        s03 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.GRASSLAND, EResource.NONE, True, ENote.NONE)
        s13 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.DESERT, EResource.INCENSE, False, ENote.NONE)
        s21 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.COTTAGE)
        s32 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_11, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 12
        s00 = Square(ETerrain.FOREST, EResource.WHEAT, False, ENote.NONE)
        s01 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)
        s13 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s20 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.COTTAGE)
        s31 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_12, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 13
        s00 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s03 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.BARBARIAN)
        s12 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.FOREST, EResource.WHEAT, False, ENote.NONE)

        s20 = Square(ETerrain.MOUNTAIN, EResource.COIN, False, ENote.NONE)
        s21 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)
        s22 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.MOUNTAIN, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.COTTAGE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_13, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))

        # map tile 14
        s00 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s01 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s02 = Square(ETerrain.SEA, EResource.SILK, False, ENote.NONE)
        s03 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)

        s10 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s11 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s12 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s13 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.COTTAGE)

        s20 = Square(ETerrain.SEA, EResource.NONE, False, ENote.NONE)
        s21 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.BARBARIAN)
        s22 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s23 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)

        s30 = Square(ETerrain.GRASSLAND, EResource.NONE, False, ENote.NONE)
        s31 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s32 = Square(ETerrain.FOREST, EResource.NONE, False, ENote.NONE)
        s33 = Square(ETerrain.DESERT, EResource.NONE, False, ENote.NONE)

        self.mapTiles.append(
            MapTile(ECivilization.NONE, ELabel.MAP_TILE_14, imgInfoGameMap, s00, s01, s02, s03, s10, s11, s12, s13, s20,
                    s21, s22, s23, s30, s31, s32, s33))
