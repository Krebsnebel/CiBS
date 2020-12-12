from enum import Enum


class ELabel(Enum):

    def __init__(self, s, front, back):
        self.sign = s
        self.frontImg = front
        self.backImg = back

    def getSign(self):
        return self.sign

    def getFrontImgName(self):
        return self.frontImg

    def getBackImgName(self):
        return self.backImg

    RUSSIA = ("RU", "mt-front_russia.jpg", "mt-back_russia.jpg")
    AMERICA = ("US", "mt-front_america.jpg", "mt-back_america.jpg")
    AGYPT = ('ÄG', "mt-front_agypt.jpg", "mt-back_agypt.jpg")
    CHINA = ('CN', "mt-front_china.jpg", "mt-back_china.jpg")
    ROME = ('RO', "mt-front_rome.jpg", "mt-back_rome.jpg")
    GERMANY = ('GE', "mt-front_germany.jpg", "mt-back_germany.jpg")
    MAP_TILE_01 = ("01", "mt-front_map-tile-01.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_02 = ("02", "mt-front_map-tile-02.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_03 = ("03", "mt-front_map-tile-03.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_04 = ("04", "mt-front_map-tile-04.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_05 = ("05", "mt-front_map-tile-05.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_06 = ("06", "mt-front_map-tile-06.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_07 = ("07", "mt-front_map-tile-07.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_08 = ("08", "mt-front_map-tile-08.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_09 = ("09", "mt-front_map-tile-09.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_10 = ("10", "mt-front_map-tile-10.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_11 = ("11", "mt-front_map-tile-11.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_12 = ("12", "mt-front_map-tile-12.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_13 = ("13", "mt-front_map-tile-13.jpg", "mt-back_map-tile.jpg")
    MAP_TILE_14 = ("14", "mt-front_map-tile-14.jpg", "mt-back_map-tile.jpg")
