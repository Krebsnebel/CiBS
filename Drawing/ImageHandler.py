import pygame

from CivEnums.EBuilding import EBuilding
from CivEnums.ECity import ECity
from CivEnums.EColor import EColor
from CivEnums.ECulturalEvent import ECulturalEvent
from CivEnums.EFigure import EFigure
from CivEnums.EGreatPerson import EGreatPerson
from CivEnums.ELabel import ELabel
from CivEnums.ENote import ENote
from CivEnums.EPolity import EPolity
from CivEnums.EProcess import EProcess
from CivEnums.EResearch import EResearch
from CivEnums.EResource import EResource
from CivEnums.ETerrain import ETerrain
from CivEnums.EUnitStrength import EUnitStrength
from CivEnums.EUnitType import EUnitType
from CivEnums.EVisibility import EVisibility
from CivEnums.EWonder import EWonder


class ImageHandler:
    imgArmyBlue = pygame.image.load(
        "Material/Figures/" + EFigure.ARMY.getImgName() + "_" + str(EColor.BLUE) + ".png")
    imgArmyGreen = pygame.image.load(
        "Material/Figures/" + EFigure.ARMY.getImgName() + "_" + str(EColor.GREEN) + ".png")
    imgArmyYellow = pygame.image.load(
        "Material/Figures/" + EFigure.ARMY.getImgName() + "_" + str(EColor.YELLOW) + ".png")
    imgArmyRed = pygame.image.load(
        "Material/Figures/" + EFigure.ARMY.getImgName() + "_" + str(EColor.RED) + ".png")
    imgArmyWhite = pygame.image.load(
        "Material/Figures/" + EFigure.ARMY.getImgName() + "_" + str(EColor.WHITE) + ".png")

    # Pioneer
    imgPioneerBlue = pygame.image.load(
        "Material/Figures/" + EFigure.PIONEER.getImgName() + "_" + str(EColor.BLUE) + ".png")
    imgPioneerGreen = pygame.image.load(
        "Material/Figures/" + EFigure.PIONEER.getImgName() + "_" + str(EColor.GREEN) + ".png")
    imgPioneerYellow = pygame.image.load(
        "Material/Figures/" + EFigure.PIONEER.getImgName() + "_" + str(EColor.YELLOW) + ".png")
    imgPioneerRed = pygame.image.load(
        "Material/Figures/" + EFigure.PIONEER.getImgName() + "_" + str(EColor.RED) + ".png")

    # Buildings
    imgMarina = pygame.image.load("Material/Buildings/" + EBuilding.MARINA.getImgName(False) + ".png")
    imgTradingPost = pygame.image.load("Material/Buildings/" + EBuilding.TRADING_POST.getImgName(False) + ".png")
    imgBlacksmith = pygame.image.load("Material/Buildings/" + EBuilding.BLACKSMITH.getImgName(False) + ".png")
    imgIronmine = pygame.image.load("Material/Buildings/" + EBuilding.BLACKSMITH.getImgName(True) + ".png")
    imgLibrary = pygame.image.load("Material/Buildings/" + EBuilding.LIBRARY.getImgName(False) + ".png")
    imgUniversity = pygame.image.load("Material/Buildings/" + EBuilding.LIBRARY.getImgName(True) + ".png")
    imgGranary = pygame.image.load("Material/Buildings/" + EBuilding.GRANARY.getImgName(False) + ".png")
    imgAqueduct = pygame.image.load("Material/Buildings/" + EBuilding.GRANARY.getImgName(True) + ".png")
    imgMarket = pygame.image.load("Material/Buildings/" + EBuilding.MARKET.getImgName(False) + ".png")
    imgBank = pygame.image.load("Material/Buildings/" + EBuilding.MARKET.getImgName(True) + ".png")
    imgTemple = pygame.image.load("Material/Buildings/" + EBuilding.TEMPLE.getImgName(False) + ".png")
    imgCathedral = pygame.image.load("Material/Buildings/" + EBuilding.TEMPLE.getImgName(True) + ".png")
    imgBarrack = pygame.image.load("Material/Buildings/" + EBuilding.BARRACK.getImgName(False) + ".png")
    imgAcademy = pygame.image.load("Material/Buildings/" + EBuilding.BARRACK.getImgName(True) + ".png")

    # Map Tile front
    imgMapTile01 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_01.getFrontImgName())
    imgMapTile02 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_02.getFrontImgName())
    imgMapTile03 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_03.getFrontImgName())
    imgMapTile04 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_04.getFrontImgName())
    imgMapTile05 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_05.getFrontImgName())
    imgMapTile06 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_06.getFrontImgName())
    imgMapTile07 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_07.getFrontImgName())
    imgMapTile08 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_08.getFrontImgName())
    imgMapTile09 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_09.getFrontImgName())
    imgMapTile10 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_10.getFrontImgName())
    imgMapTile11 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_11.getFrontImgName())
    imgMapTile12 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_12.getFrontImgName())
    imgMapTile13 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_13.getFrontImgName())
    imgMapTile14 = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_14.getFrontImgName())
    imgMapTileAgypt = pygame.image.load("Material/MapTiles/" + ELabel.AGYPT.getFrontImgName())
    imgMapTileAmerica = pygame.image.load("Material/MapTiles/" + ELabel.AMERICA.getFrontImgName())
    imgMapTileChina = pygame.image.load("Material/MapTiles/" + ELabel.CHINA.getFrontImgName())
    imgMapTileGermany = pygame.image.load("Material/MapTiles/" + ELabel.GERMANY.getFrontImgName())
    imgMapTileRome = pygame.image.load("Material/MapTiles/" + ELabel.ROME.getFrontImgName())
    imgMapTileRussia = pygame.image.load("Material/MapTiles/" + ELabel.RUSSIA.getFrontImgName())

    # Map Tile back
    imgMapTileBack = pygame.image.load("Material/MapTiles/" + ELabel.MAP_TILE_01.getBackImgName())
    imgMapTileAgyptBack = pygame.image.load("Material/MapTiles/" + ELabel.AGYPT.getBackImgName())
    imgMapTileAmericaBack = pygame.image.load("Material/MapTiles/" + ELabel.AMERICA.getBackImgName())
    imgMapTileChinaBack = pygame.image.load("Material/MapTiles/" + ELabel.CHINA.getBackImgName())
    imgMapTileGermanyBack = pygame.image.load("Material/MapTiles/" + ELabel.GERMANY.getBackImgName())
    imgMapTileRomeBack = pygame.image.load("Material/MapTiles/" + ELabel.ROME.getBackImgName())
    imgMapTileRussiaBack = pygame.image.load("Material/MapTiles/" + ELabel.RUSSIA.getBackImgName())

    # Cultural Event
    e = ECulturalEvent.REVOLTING_CITIZENS_1
    imgRevoltingCitizens_I = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                               e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.REVOLTING_CITIZENS_2
    imgRevoltingCitizens_II = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                                e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.DISORIENTED
    imgDisOriented = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                       e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.DISASTER
    imgDisaster = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                    e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.CATASTROPHE
    imgCatastrophe = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                       e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.PRESIDENT_HOLIDAY
    imgPresidentHoliday = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                            e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.DISPLACED
    imgDisplaced = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                     e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.LOST
    imgLost = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.A_PRINCELY_GIFT
    imgAPrincelyGift = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                         e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.MASS_EXODUS
    imgMassExodus = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                      e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.IDEASMITH
    imgIdeasmith = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                     e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.DEFORESTATION
    imgDeforestation = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                         e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.SABOTAGE
    imgSabotage = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                    e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.BREAD_AND_GAMES
    imgBreadAndGames = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                         e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.FAITHLESS
    imgFaithless = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                     e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.DROUGHT
    imgDrought = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                   e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.LONG_LIVE_THE_QUEEN
    imgLongLiveTheQueen = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                            e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.GENERAL_DESERTION
    imgGeneralDesertion = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                            e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.PRIME_TIME
    imgPrimeTime = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                     e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.KNIGHT_TOURNAMENT
    imgKnighthoodTournament = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                                e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.GIFT_FROM_A_DISTANCE
    imgGiftFromADistance = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                             e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.EXCHANGE_OF_IDEAS
    imgExchangeOfIdeas = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                           e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.GENEROUS_GIFT
    imgGenerousGift = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                        e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.SHARED_KNOWLEDGE
    imgSharedKnowledge = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                           e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    e = ECulturalEvent.DESPOT_HOLIDAY
    imgDespotHoliday = pygame.image.load("Material/CultureCards/" + e.getPrefix() +
                                         e.getImgName(EVisibility.FOR_ALL) + ".jpg")
    imgCulturalEventIBack = pygame.image.load("Material/CultureCards/I_CultureCard.jpg")
    imgCulturalEventIIBack = pygame.image.load("Material/CultureCards/II_CultureCard.jpg")
    imgCulturalEventIIIBack = pygame.image.load("Material/CultureCards/III_CultureCard.jpg")

    imgCavalryWeak = pygame.image.load("Material/MilitaryUnits/" + EUnitType.CAVALRY.getImgName() + "_" +
                                       EUnitStrength.WEAK.getImgName() + ".jpg")
    imgCavalryMedium = pygame.image.load("Material/MilitaryUnits/" + EUnitType.CAVALRY.getImgName() + "_" +
                                         EUnitStrength.MEDIUM.getImgName() + ".jpg")
    imgCavalryStrong = pygame.image.load("Material/MilitaryUnits/" + EUnitType.CAVALRY.getImgName() + "_" +
                                         EUnitStrength.STRONG.getImgName() + ".jpg")
    imgInfantryWeak = pygame.image.load("Material/MilitaryUnits/" + EUnitType.INFANTRY.getImgName() + "_" +
                                        EUnitStrength.WEAK.getImgName() + ".jpg")
    imgInfantryMedium = pygame.image.load("Material/MilitaryUnits/" + EUnitType.INFANTRY.getImgName() + "_" +
                                          EUnitStrength.MEDIUM.getImgName() + ".jpg")
    imgInfantryStrong = pygame.image.load("Material/MilitaryUnits/" + EUnitType.INFANTRY.getImgName() + "_" +
                                          EUnitStrength.STRONG.getImgName() + ".jpg")
    imgArtilleryWeak = pygame.image.load("Material/MilitaryUnits/" + EUnitType.ARTILLERY.getImgName() + "_" +
                                         EUnitStrength.WEAK.getImgName() + ".jpg")
    imgArtilleryMedium = pygame.image.load("Material/MilitaryUnits/" + EUnitType.ARTILLERY.getImgName() + "_" +
                                           EUnitStrength.MEDIUM.getImgName() + ".jpg")
    imgArtilleryStrong = pygame.image.load("Material/MilitaryUnits/" + EUnitType.ARTILLERY.getImgName() + "_" +
                                           EUnitStrength.STRONG.getImgName() + ".jpg")
    imgAirForceWeak = pygame.image.load("Material/MilitaryUnits/" + EUnitType.AIR_FORCE.getImgName() + "_" +
                                        EUnitStrength.WEAK.getImgName() + ".jpg")
    imgAirForceMedium = pygame.image.load("Material/MilitaryUnits/" + EUnitType.AIR_FORCE.getImgName() + "_" +
                                          EUnitStrength.MEDIUM.getImgName() + ".jpg")
    imgAirForceStrong = pygame.image.load("Material/MilitaryUnits/" + EUnitType.AIR_FORCE.getImgName() + "_" +
                                          EUnitStrength.STRONG.getImgName() + ".jpg")
    imgMilUnitBack = pygame.image.load("Material/MilitaryUnits/MilitaryUnit_Back.jpg")

    # Cities
    imgKapitolFortifiedBlue = pygame.image.load(
        "Material/Cities/" + ECity.KAPITOL.getImgName(True) + "_" + str(EColor.BLUE) + ".png")
    imgKapitolFortifiedGreen = pygame.image.load(
        "Material/Cities/" + ECity.KAPITOL.getImgName(True) + "_" + str(EColor.GREEN) + ".png")
    imgKapitolFortifiedYellow = pygame.image.load(
        "Material/Cities/" + ECity.KAPITOL.getImgName(True) + "_" + str(EColor.YELLOW) + ".png")
    imgKapitolFortifiedRed = pygame.image.load(
        "Material/Cities/" + ECity.KAPITOL.getImgName(True) + "_" + str(EColor.RED) + ".png")
    imgTownFortifiedBlue = pygame.image.load(
        "Material/Cities/" + ECity.TOWN.getImgName(True) + "_" + str(EColor.BLUE) + ".png")
    imgTownFortifiedGreen = pygame.image.load(
        "Material/Cities/" + ECity.TOWN.getImgName(True) + "_" + str(EColor.GREEN) + ".png")
    imgTownFortifiedYellow = pygame.image.load(
        "Material/Cities/" + ECity.TOWN.getImgName(True) + "_" + str(EColor.YELLOW) + ".png")
    imgTownFortifiedRed = pygame.image.load(
        "Material/Cities/" + ECity.TOWN.getImgName(True) + "_" + str(EColor.RED) + ".png")
    imgKapitolUnpavedBlue = pygame.image.load(
        "Material/Cities/" + ECity.KAPITOL.getImgName(False) + "_" + str(EColor.BLUE) + ".png")
    imgKapitolUnpavedGreen = pygame.image.load(
        "Material/Cities/" + ECity.KAPITOL.getImgName(False) + "_" + str(EColor.GREEN) + ".png")
    imgKapitolUnpavedYellow = pygame.image.load(
        "Material/Cities/" + ECity.KAPITOL.getImgName(False) + "_" + str(EColor.YELLOW) + ".png")
    imgKapitolUnpavedRed = pygame.image.load(
        "Material/Cities/" + ECity.KAPITOL.getImgName(False) + "_" + str(EColor.RED) + ".png")
    imgTownUnpavedBlue = pygame.image.load(
        "Material/Cities/" + ECity.TOWN.getImgName(False) + "_" + str(EColor.BLUE) + ".png")
    imgTownUnpavedGreen = pygame.image.load(
        "Material/Cities/" + ECity.TOWN.getImgName(False) + "_" + str(EColor.GREEN) + ".png")
    imgTownUnpavedYellow = pygame.image.load(
        "Material/Cities/" + ECity.TOWN.getImgName(False) + "_" + str(EColor.YELLOW) + ".png")
    imgTownUnpavedRed = pygame.image.load(
        "Material/Cities/" + ECity.TOWN.getImgName(False) + "_" + str(EColor.RED) + ".png")

    # Disaster Marker
    imgDroughtMarker = pygame.image.load("Material/Terrain/" + ETerrain.DROUGHT.getImgName() + ".jpg")
    imgDeforestationMarker = pygame.image.load("Material/Terrain/" + ETerrain.DEFORESTATION.getImgName() + ".jpg")

    # Great Persons
    imgArtist = pygame.image.load("Material/GreatPersons/" + EGreatPerson.ARTIST.getImgName() + ".jpg")
    imgBuilder = pygame.image.load("Material/GreatPersons/" + EGreatPerson.BUILDER.getImgName() + ".jpg")
    imgGeneral = pygame.image.load("Material/GreatPersons/" + EGreatPerson.GENERAL.getImgName() + ".jpg")
    imgHumanitarian = pygame.image.load("Material/GreatPersons/" + EGreatPerson.HUMANITARIAN.getImgName() + ".jpg")
    imgIndustrialist = pygame.image.load("Material/GreatPersons/" + EGreatPerson.INDUSTRIALIST.getImgName() + ".jpg")
    imgScientist = pygame.image.load("Material/GreatPersons/" + EGreatPerson.SCIENTIST.getImgName() + ".jpg")
    imgGreatPersonBack = pygame.image.load("Material/GreatPersons/GreatPerson_back.jpg")

    # Research
    imgIronProcessing = pygame.image.load("Material/Research/" + EResearch.IRON_PROCESSING.getImgFrontName() + ".jpg")
    imgLegislation = pygame.image.load("Material/Research/" + EResearch.LEGISLATION.getImgFrontName() + ".jpg")
    imgCeramics = pygame.image.load("Material/Research/" + EResearch.CERAMICS.getImgFrontName() + ".jpg")
    imgNavigation = pygame.image.load("Material/Research/" + EResearch.NAVIGATION.getImgFrontName() + ".jpg")
    imgPhilosophy = pygame.image.load("Material/Research/" + EResearch.PHILOSOPHY.getImgFrontName() + ".jpg")
    imgCavalry = pygame.image.load("Material/Research/" + EResearch.CAVALRY.getImgFrontName() + ".jpg")
    imgScripture = pygame.image.load("Material/Research/" + EResearch.SCRIPTURE.getImgFrontName() + ".jpg")
    imgStoneCarving = pygame.image.load("Material/Research/" + EResearch.STONE_CARVING.getImgFrontName() + ".jpg")
    imgStockBreeding = pygame.image.load("Material/Research/" + EResearch.STOCK_BREEDING.getImgFrontName() + ".jpg")
    imgCurrency = pygame.image.load("Material/Research/" + EResearch.CURRENCY.getImgFrontName() + ".jpg")
    imgConstructionIndustry = pygame.image.load(
        "Material/Research/" + EResearch.CONSTRUCTION_INDUSTRY.getImgFrontName() + ".jpg")
    imgIrrigation = pygame.image.load("Material/Research/" + EResearch.IRRIGATION.getImgFrontName() + ".jpg")
    imgDemocracy = pygame.image.load("Material/Research/" + EResearch.DEMOCRACY.getImgFrontName() + ".jpg")
    imgPrintingPress = pygame.image.load("Material/Research/" + EResearch.PRINTING_PRESS.getImgFrontName() + ".jpg")
    imgMechanicalEngineering = pygame.image.load(
        "Material/Research/" + EResearch.MECHANICAL_ENGINEERING.getImgFrontName() + ".jpg")
    imgMathematics = pygame.image.load("Material/Research/" + EResearch.MATHEMATICS.getImgFrontName() + ".jpg")
    imgMonarchy = pygame.image.load("Material/Research/" + EResearch.MONARCHY.getImgFrontName() + ".jpg")
    imgPublicAdministration = pygame.image.load(
        "Material/Research/" + EResearch.PUBLIC_ADMINISTRATION.getImgFrontName() + ".jpg")
    imgKnighthood = pygame.image.load("Material/Research/" + EResearch.KNIGHTHOOD.getImgFrontName() + ".jpg")
    imgSailing = pygame.image.load("Material/Research/" + EResearch.SAILING.getImgFrontName() + ".jpg")
    imgBanking = pygame.image.load("Material/Research/" + EResearch.BANKING.getImgFrontName() + ".jpg")
    imgBiology = pygame.image.load("Material/Research/" + EResearch.BIOLOGY.getImgFrontName() + ".jpg")
    imgSteamEngine = pygame.image.load("Material/Research/" + EResearch.STEAM_ENGINE.getImgFrontName() + ".jpg")
    imgRailroad = pygame.image.load("Material/Research/" + EResearch.RAILROAD.getImgFrontName() + ".jpg")
    imgCommunism = pygame.image.load("Material/Research/" + EResearch.COMMUNISM.getImgFrontName() + ".jpg")
    imgMetalCasting = pygame.image.load("Material/Research/" + EResearch.METAL_CASTING.getImgFrontName() + ".jpg")
    imgMilitaryScience = pygame.image.load("Material/Research/" + EResearch.MILITARY_SCIENCE.getImgFrontName() + ".jpg")
    imgGunpowder = pygame.image.load("Material/Research/" + EResearch.GUNPOWDER.getImgFrontName() + ".jpg")
    imgTheology = pygame.image.load("Material/Research/" + EResearch.THEOLOGY.getImgFrontName() + ".jpg")
    imgNuclearTheory = pygame.image.load("Material/Research/" + EResearch.NUCLEAR_THEORY.getImgFrontName() + ".jpg")
    imgBallistics = pygame.image.load("Material/Research/" + EResearch.BALLISTICS.getImgFrontName() + ".jpg")
    imgComputerTechnology = pygame.image.load(
        "Material/Research/" + EResearch.COMPUTER_TECHNOLOGY.getImgFrontName() + ".jpg")
    imgSpareParts = pygame.image.load("Material/Research/" + EResearch.SPARE_PARTS.getImgFrontName() + ".jpg")
    imgAviation = pygame.image.load("Material/Research/" + EResearch.AVIATION.getImgFrontName() + ".jpg")
    imgMassMedia = pygame.image.load("Material/Research/" + EResearch.MASS_MEDIA.getImgFrontName() + ".jpg")
    imgCombustionEngine = pygame.image.load(
        "Material/Research/" + EResearch.COMBUSTION_ENGINE.getImgFrontName() + ".jpg")
    imgAstronautics = pygame.image.load("Material/Research/" + EResearch.ASTRONAUTICS.getImgFrontName() + ".jpg")

    imgResearchIBack = pygame.image.load("Material/Research/I_Research.jpg")
    imgResearchIIBack = pygame.image.load("Material/Research/II_Research.jpg")
    imgResearchIIIBack = pygame.image.load("Material/Research/III_Research.jpg")
    imgResearchIVBack = pygame.image.load("Material/Research/IV_Research.jpg")
    imgResearchVBack = pygame.image.load("Material/Research/V_Research.jpg")

    # Wonder Marker
    imgStonehengeMarker = pygame.image.load("Material/Wonders/" + EWonder.STONEHENGE.getMarkerImgName() + ".png")
    imgTheHangingGardensMarker = pygame.image.load(
        "Material/Wonders/" + EWonder.THE_HANGING_GARDENS.getMarkerImgName() + ".png")
    imgTheColossusMarker = pygame.image.load("Material/Wonders/" + EWonder.THE_COLOSSUS.getMarkerImgName() + ".png")
    imgTheOracleMarker = pygame.image.load("Material/Wonders/" + EWonder.THE_ORACLE.getMarkerImgName() + ".png")
    imgTheLouvreMarker = pygame.image.load("Material/Wonders/" + EWonder.THE_LOUVRE.getMarkerImgName() + ".png")
    imgCastleHimejiMarker = pygame.image.load("Material/Wonders/" + EWonder.CASTLE_HIMEJI.getMarkerImgName() + ".png")
    imgAngkorWatMarker = pygame.image.load("Material/Wonders/" + EWonder.ANGKOR_WAT.getMarkerImgName() + ".png")
    imgPorcelainTowerMarker = pygame.image.load(
        "Material/Wonders/" + EWonder.PORCELAIN_TOWER.getMarkerImgName() + ".png")
    imgPanamaCanalMarker = pygame.image.load("Material/Wonders/" + EWonder.PANAMA_CANAL.getMarkerImgName() + ".png")
    imgOperaHouseOfSidneyMarker = pygame.image.load(
        "Material/Wonders/" + EWonder.OPERA_HOUSE_OF_SIDNEY.getMarkerImgName() + ".png")
    imgStatueOfLibertyMarker = pygame.image.load(
        "Material/Wonders/" + EWonder.STATUE_OF_LIBERTY.getMarkerImgName() + ".png")
    imgUnitedNationsMarker = pygame.image.load(
        "Material/Wonders/" + EWonder.UNITED_NATIONS.getMarkerImgName() + ".png")

    # Wonder Cards
    imgStonehengeCard = pygame.image.load("Material/Wonders/" + EWonder.STONEHENGE.getCardImgName(True) + ".jpg")
    imgTheHangingGardensCard = pygame.image.load(
        "Material/Wonders/" + EWonder.THE_HANGING_GARDENS.getCardImgName(True) + ".jpg")
    imgTheColossusCard = pygame.image.load("Material/Wonders/" + EWonder.THE_COLOSSUS.getCardImgName(True) + ".jpg")
    imgTheOracleCard = pygame.image.load("Material/Wonders/" + EWonder.THE_ORACLE.getCardImgName(True) + ".jpg")
    imgTheLouvreCard = pygame.image.load("Material/Wonders/" + EWonder.THE_LOUVRE.getCardImgName(True) + ".jpg")
    imgCastleHimejiCard = pygame.image.load("Material/Wonders/" + EWonder.CASTLE_HIMEJI.getCardImgName(True) + ".jpg")
    imgAngkorWatCard = pygame.image.load("Material/Wonders/" + EWonder.ANGKOR_WAT.getCardImgName(True) + ".jpg")
    imgPorcelainTowerCard = pygame.image.load(
        "Material/Wonders/" + EWonder.PORCELAIN_TOWER.getCardImgName(True) + ".jpg")
    imgPanamaCanalCard = pygame.image.load("Material/Wonders/" + EWonder.PANAMA_CANAL.getCardImgName(True) + ".jpg")
    imgOperaHouseOfSidneyCard = pygame.image.load(
        "Material/Wonders/" + EWonder.OPERA_HOUSE_OF_SIDNEY.getCardImgName(True) + ".jpg")
    imgStatueOfLibertyCard = pygame.image.load(
        "Material/Wonders/" + EWonder.STATUE_OF_LIBERTY.getCardImgName(True) + ".jpg")
    imgUnitedNationsCard = pygame.image.load("Material/Wonders/" + EWonder.UNITED_NATIONS.getCardImgName(True) + ".jpg")

    imgAncientCard = pygame.image.load("Material/Wonders/" + EWonder.STONEHENGE.getCardImgName(False) + ".jpg")
    imgMiddleAgeCard = pygame.image.load("Material/Wonders/" + EWonder.THE_LOUVRE.getCardImgName(False) + ".jpg")
    imgModernCard = pygame.image.load("Material/Wonders/" + EWonder.PANAMA_CANAL.getCardImgName(False) + ".jpg")

    # polity
    imgPolityAnarchy = pygame.image.load("Material/Civilizations/Polity_" + EPolity.ANARCHY.getImgName() + ".jpg")
    imgPolityCommunism = pygame.image.load("Material/Civilizations/Polity_" + EPolity.COMMUNISM.getImgName() + ".jpg")
    imgPolityDemocracy = pygame.image.load("Material/Civilizations/Polity_" + EPolity.DEMOCRACY.getImgName() + ".jpg")
    imgPolityDespotism = pygame.image.load("Material/Civilizations/Polity_" + EPolity.DESPOTISM.getImgName() + ".jpg")
    imgPolityFeudalism = pygame.image.load("Material/Civilizations/Polity_" + EPolity.FEUDALISM.getImgName() + ".jpg")
    imgPolityFundamentalism = pygame.image.load("Material/Civilizations/Polity_" +
                                                EPolity.FUNDAMENTALISM.getImgName() + ".jpg")
    imgPolityMonarchy = pygame.image.load("Material/Civilizations/Polity_" + EPolity.MONARCHY.getImgName() + ".jpg")
    imgPolityRepublic = pygame.image.load("Material/Civilizations/Polity_" + EPolity.REPUBLIC.getImgName() + ".jpg")

    # process
    imgNextButton = pygame.image.load("Material/Process/NextButton.png")

    # marker
    imgBarbarian = pygame.image.load("Material/Marker/Barbarian.png")
    imgCottage = pygame.image.load("Material/Marker/Cottage.png")
    imgIron = pygame.image.load("Material/Marker/Iron.png")
    imgIncense = pygame.image.load("Material/Marker/Incense.png")
    imgSilk = pygame.image.load("Material/Marker/Silk.png")
    imgWheat = pygame.image.load("Material/Marker/Wheat.png")
    imgSpy = pygame.image.load("Material/Marker/Spy.png")
    imgUranium = pygame.image.load("Material/Marker/Uranium.png")
    imgGreatPersonRes = pygame.image.load("Material/Marker/GreatPersonRes.png")
    imgCoin = pygame.image.load("Material/Marker/Coin.png")
    imgCultureMarker = pygame.image.load("Material/Marker/CultureMarker.png")
    imgHitMarker = pygame.image.load("Material/Marker/HitMarker.png")


def getImageOfMarker(mType, res, front):
    if mType is ENote.BARBARIAN and not front:
        return ImageHandler.imgBarbarian
    elif mType is ENote.COTTAGE and not front:
        return ImageHandler.imgCottage
    else:       # resource, culture, coin, hit marker
        if res is EResource.IRON:
            return ImageHandler.imgIron
        elif res is EResource.INCENSE:
            return ImageHandler.imgIncense
        elif res is EResource.SILK:
            return ImageHandler.imgSilk
        elif res is EResource.WHEAT:
            return ImageHandler.imgWheat
        elif res is EResource.SPY:
            return ImageHandler.imgSpy
        elif res is EResource.URANIUM:
            return ImageHandler.imgUranium
        elif res is EResource.GREAT_PERSON:
            return ImageHandler.imgGreatPersonRes
        elif res is EResource.COIN:
            return ImageHandler.imgCoin
        elif res is EResource.CULTURE:
            return ImageHandler.imgCultureMarker
        elif res is EResource.HIT:
            return ImageHandler.imgHitMarker
        else:
            return None


def getImageOfProcess(process):
    if process is EProcess.NEXT_BUTTON:
        return ImageHandler.imgNextButton


def getImageOfPolity(polity):
    if polity is EPolity.COMMUNISM:
        return ImageHandler.imgPolityCommunism
    elif polity is EPolity.DEMOCRACY:
        return ImageHandler.imgPolityDemocracy
    elif polity is EPolity.DESPOTISM:
        return ImageHandler.imgPolityDespotism
    elif polity is EPolity.FEUDALISM:
        return ImageHandler.imgPolityFeudalism
    elif polity is EPolity.FUNDAMENTALISM:
        return ImageHandler.imgPolityFundamentalism
    elif polity is EPolity.MONARCHY:
        return ImageHandler.imgPolityMonarchy
    elif polity is EPolity.REPUBLIC:
        return ImageHandler.imgPolityRepublic
    else:
        return ImageHandler.imgPolityAnarchy


def getImageOfWonder(wType, card, front):
    if card:
        if front:
            if wType is EWonder.STONEHENGE:
                return ImageHandler.imgStonehengeCard
            elif wType is EWonder.THE_HANGING_GARDENS:
                return ImageHandler.imgTheHangingGardensCard
            elif wType is EWonder.THE_COLOSSUS:
                return ImageHandler.imgTheColossusCard
            elif wType is EWonder.THE_ORACLE:
                return ImageHandler.imgTheOracleCard
            elif wType is EWonder.THE_LOUVRE:
                return ImageHandler.imgTheLouvreCard
            elif wType is EWonder.CASTLE_HIMEJI:
                return ImageHandler.imgCastleHimejiCard
            elif wType is EWonder.ANGKOR_WAT:
                return ImageHandler.imgAngkorWatCard
            elif wType is EWonder.PORCELAIN_TOWER:
                return ImageHandler.imgPorcelainTowerCard
            elif wType is EWonder.PANAMA_CANAL:
                return ImageHandler.imgPanamaCanalCard
            elif wType is EWonder.OPERA_HOUSE_OF_SIDNEY:
                return ImageHandler.imgOperaHouseOfSidneyCard
            elif wType is EWonder.STATUE_OF_LIBERTY:
                return ImageHandler.imgStatueOfLibertyCard
            else:       # EWonder.UNITED_NATIONS:
                return ImageHandler.imgUnitedNationsCard
        else:       # back
            if wType is EWonder.STONEHENGE or EWonder.THE_HANGING_GARDENS or EWonder.THE_COLOSSUS or EWonder.THE_ORACLE:
                return ImageHandler.imgAncientCard
            elif wType is EWonder.THE_LOUVRE or EWonder.CASTLE_HIMEJI or EWonder.ANGKOR_WAT or EWonder.PORCELAIN_TOWER:
                return ImageHandler.imgMiddleAgeCard
            else:
                # EWonder.PANAMA_CANAL, EWonder.OPERA_HOUSE_OF_SIDNEY, EWonder.STATUE_OF_LIBERTY, EWonder.UNITED_NATIONS
                return ImageHandler.imgModernCard
    else:   # marker
        if wType is EWonder.STONEHENGE:
            return ImageHandler.imgStonehengeMarker
        elif wType is EWonder.THE_HANGING_GARDENS:
            return ImageHandler.imgTheHangingGardensMarker
        elif wType is EWonder.THE_COLOSSUS:
            return ImageHandler.imgTheColossusMarker
        elif wType is EWonder.THE_ORACLE:
            return ImageHandler.imgTheOracleMarker
        elif wType is EWonder.THE_LOUVRE:
            return ImageHandler.imgTheLouvreMarker
        elif wType is EWonder.CASTLE_HIMEJI:
            return ImageHandler.imgCastleHimejiMarker
        elif wType is EWonder.ANGKOR_WAT:
            return ImageHandler.imgAngkorWatMarker
        elif wType is EWonder.PORCELAIN_TOWER:
            return ImageHandler.imgPorcelainTowerMarker
        elif wType is EWonder.PANAMA_CANAL:
            return ImageHandler.imgPanamaCanalMarker
        elif wType is EWonder.OPERA_HOUSE_OF_SIDNEY:
            return ImageHandler.imgOperaHouseOfSidneyMarker
        elif wType is EWonder.STATUE_OF_LIBERTY:
            return ImageHandler.imgStatueOfLibertyMarker
        else:  # EWonder.UNITED_NATIONS:
            return ImageHandler.imgUnitedNationsMarker


def getImageOfResearch(rType, front):
    if front:
        if rType is EResearch.IRON_PROCESSING:
            return ImageHandler.imgIronProcessing
        elif rType is EResearch.LEGISLATION:
            return ImageHandler.imgLegislation
        elif rType is EResearch.CERAMICS:
            return ImageHandler.imgCeramics
        elif rType is EResearch.NAVIGATION:
            return ImageHandler.imgNavigation
        elif rType is EResearch.PHILOSOPHY:
            return ImageHandler.imgPhilosophy
        elif rType is EResearch.CAVALRY:
            return ImageHandler.imgCavalry
        elif rType is EResearch.SCRIPTURE:
            return ImageHandler.imgScripture
        elif rType is EResearch.STONE_CARVING:
            return ImageHandler.imgStoneCarving
        elif rType is EResearch.STOCK_BREEDING:
            return ImageHandler.imgStockBreeding
        elif rType is EResearch.CURRENCY:
            return ImageHandler.imgCurrency
        elif rType is EResearch.CONSTRUCTION_INDUSTRY:
            return ImageHandler.imgConstructionIndustry
        elif rType is EResearch.IRRIGATION:
            return ImageHandler.imgIrrigation
        elif rType is EResearch.DEMOCRACY:
            return ImageHandler.imgDemocracy
        elif rType is EResearch.PRINTING_PRESS:
            return ImageHandler.imgPrintingPress
        elif rType is EResearch.MECHANICAL_ENGINEERING:
            return ImageHandler.imgMechanicalEngineering
        elif rType is EResearch.MATHEMATICS:
            return ImageHandler.imgMathematics
        elif rType is EResearch.MONARCHY:
            return ImageHandler.imgMonarchy
        elif rType is EResearch.PUBLIC_ADMINISTRATION:
            return ImageHandler.imgPublicAdministration
        elif rType is EResearch.KNIGHTHOOD:
            return ImageHandler.imgKnighthood
        elif rType is EResearch.SAILING:
            return ImageHandler.imgSailing
        elif rType is EResearch.BANKING:
            return ImageHandler.imgBanking
        elif rType is EResearch.BIOLOGY:
            return ImageHandler.imgBiology
        elif rType is EResearch.STEAM_ENGINE:
            return ImageHandler.imgSteamEngine
        elif rType is EResearch.RAILROAD:
            return ImageHandler.imgRailroad
        elif rType is EResearch.COMMUNISM:
            return ImageHandler.imgCommunism
        elif rType is EResearch.METAL_CASTING:
            return ImageHandler.imgMetalCasting
        elif rType is EResearch.MILITARY_SCIENCE:
            return ImageHandler.imgMilitaryScience
        elif rType is EResearch.GUNPOWDER:
            return ImageHandler.imgGunpowder
        elif rType is EResearch.THEOLOGY:
            return ImageHandler.imgTheology
        elif rType is EResearch.NUCLEAR_THEORY:
            return ImageHandler.imgNuclearTheory
        elif rType is EResearch.BALLISTICS:
            return ImageHandler.imgBallistics
        elif rType is EResearch.COMPUTER_TECHNOLOGY:
            return ImageHandler.imgComputerTechnology
        elif rType is EResearch.SPARE_PARTS:
            return ImageHandler.imgSpareParts
        elif rType is EResearch.AVIATION:
            return ImageHandler.imgAviation
        elif rType is EResearch.MASS_MEDIA:
            return ImageHandler.imgMassMedia
        elif rType is EResearch.COMBUSTION_ENGINE:
            return ImageHandler.imgCombustionEngine
        elif rType is EResearch.ASTRONAUTICS:
            return ImageHandler.imgAstronautics
    else:
        if rType.getLevel() == 1:
            return ImageHandler.imgResearchIBack
        elif rType.getLevel() == 2:
            return ImageHandler.imgResearchIIBack
        elif rType.getLevel() == 3:
            return ImageHandler.imgResearchIIIBack
        elif rType.getLevel() == 4:
            return ImageHandler.imgResearchIVBack
        else:  # rType.getLevel() == 5:
            return ImageHandler.imgResearchVBack


def getImageOfGreatPerson(gpType, front):
    if front:
        if gpType is EGreatPerson.ARTIST:
            return ImageHandler.imgArtist
        elif gpType is EGreatPerson.BUILDER:
            return ImageHandler.imgBuilder
        elif gpType is EGreatPerson.GENERAL:
            return ImageHandler.imgGeneral
        elif gpType is EGreatPerson.HUMANITARIAN:
            return ImageHandler.imgHumanitarian
        elif gpType is EGreatPerson.INDUSTRIALIST:
            return ImageHandler.imgIndustrialist
        elif gpType is EGreatPerson.SCIENTIST:
            return ImageHandler.imgScientist
    else:   # back
        return ImageHandler.imgGreatPersonBack


def getImageOfDisasterMarker(drought):
    if drought:
        return ImageHandler.imgDroughtMarker
    else:    # deforestation
        return ImageHandler.imgDeforestationMarker


def getImageOfCity(cType, color, fortified):
    if fortified:
        if cType is ECity.KAPITOL:
            if color is EColor.BLUE:
                return ImageHandler.imgKapitolFortifiedBlue
            elif color is EColor.GREEN:
                return ImageHandler.imgKapitolFortifiedGreen
            elif color is EColor.YELLOW:
                return ImageHandler.imgKapitolFortifiedYellow
            else:
                return ImageHandler.imgKapitolFortifiedRed
        else:   # TOWN
            if color is EColor.BLUE:
                return ImageHandler.imgTownFortifiedBlue
            elif color is EColor.GREEN:
                return ImageHandler.imgTownFortifiedGreen
            elif color is EColor.YELLOW:
                return ImageHandler.imgTownFortifiedYellow
            else:
                return ImageHandler.imgTownFortifiedRed
    else:   # unpaved
        if cType is ECity.KAPITOL:
            if color is EColor.BLUE:
                return ImageHandler.imgKapitolUnpavedBlue
            elif color is EColor.GREEN:
                return ImageHandler.imgKapitolUnpavedGreen
            elif color is EColor.YELLOW:
                return ImageHandler.imgKapitolUnpavedYellow
            else:
                return ImageHandler.imgKapitolUnpavedRed
        else:   # TOWN
            if color is EColor.BLUE:
                return ImageHandler.imgTownUnpavedBlue
            elif color is EColor.GREEN:
                return ImageHandler.imgTownUnpavedGreen
            elif color is EColor.YELLOW:
                return ImageHandler.imgTownUnpavedYellow
            else:
                return ImageHandler.imgTownUnpavedRed


def getImageOfMilitaryUnit(uType, strength, front):
    if front:
        if uType is EUnitType.CAVALRY:
            if strength is EUnitStrength.WEAK:
                return ImageHandler.imgCavalryWeak
            elif strength is EUnitStrength.MEDIUM:
                return ImageHandler.imgCavalryMedium
            else:   # EUnitStrength.STRONG:
                return ImageHandler.imgCavalryStrong
        elif uType is EUnitType.INFANTRY:
            if strength is EUnitStrength.WEAK:
                return ImageHandler.imgInfantryWeak
            elif strength is EUnitStrength.MEDIUM:
                return ImageHandler.imgInfantryMedium
            else:   # EUnitStrength.STRONG:
                return ImageHandler.imgInfantryStrong
        elif uType is EUnitType.ARTILLERY:
            if strength is EUnitStrength.WEAK:
                return ImageHandler.imgArtilleryWeak
            elif strength is EUnitStrength.MEDIUM:
                return ImageHandler.imgArtilleryMedium
            else:   # EUnitStrength.STRONG:
                return ImageHandler.imgArtilleryStrong
        elif uType is EUnitType.AIR_FORCE:
            if strength is EUnitStrength.WEAK:
                return ImageHandler.imgAirForceWeak
            elif strength is EUnitStrength.MEDIUM:
                return ImageHandler.imgAirForceMedium
            else:   # EUnitStrength.STRONG:
                return ImageHandler.imgAirForceStrong
    else:   # back
        return ImageHandler.imgMilUnitBack


def getImageOfCulturalEvent(event, front):
    if front:
        if event is ECulturalEvent.REVOLTING_CITIZENS_1:
            return ImageHandler.imgRevoltingCitizens_I
        if event is ECulturalEvent.REVOLTING_CITIZENS_2:
            return ImageHandler.imgRevoltingCitizens_II
        if event is ECulturalEvent.DISORIENTED:
            return ImageHandler.imgDisOriented
        if event is ECulturalEvent.DISASTER:
            return ImageHandler.imgDisaster
        if event is ECulturalEvent.CATASTROPHE:
            return ImageHandler.imgCatastrophe
        if event is ECulturalEvent.PRESIDENT_HOLIDAY:
            return ImageHandler.imgPresidentHoliday
        if event is ECulturalEvent.DISPLACED:
            return ImageHandler.imgDisplaced
        if event is ECulturalEvent.LOST:
            return ImageHandler.imgLost
        if event is ECulturalEvent.A_PRINCELY_GIFT:
            return ImageHandler.imgAPrincelyGift
        if event is ECulturalEvent.MASS_EXODUS:
            return ImageHandler.imgMassExodus
        if event is ECulturalEvent.IDEASMITH:
            return ImageHandler.imgIdeasmith
        if event is ECulturalEvent.DEFORESTATION:
            return ImageHandler.imgDeforestation
        if event is ECulturalEvent.SABOTAGE:
            return ImageHandler.imgSabotage
        if event is ECulturalEvent.BREAD_AND_GAMES:
            return ImageHandler.imgBreadAndGames
        if event is ECulturalEvent.FAITHLESS:
            return ImageHandler.imgFaithless
        if event is ECulturalEvent.DROUGHT:
            return ImageHandler.imgDrought
        if event is ECulturalEvent.LONG_LIVE_THE_QUEEN:
            return ImageHandler.imgLongLiveTheQueen
        if event is ECulturalEvent.GENERAL_DESERTION:
            return ImageHandler.imgGeneralDesertion
        if event is ECulturalEvent.PRIME_TIME:
            return ImageHandler.imgPrimeTime
        if event is ECulturalEvent.KNIGHT_TOURNAMENT:
            return ImageHandler.imgKnighthoodTournament
        if event is ECulturalEvent.GIFT_FROM_A_DISTANCE:
            return ImageHandler.imgGiftFromADistance
        if event is ECulturalEvent.EXCHANGE_OF_IDEAS:
            return ImageHandler.imgExchangeOfIdeas
        if event is ECulturalEvent.GENEROUS_GIFT:
            return ImageHandler.imgGenerousGift
        if event is ECulturalEvent.SHARED_KNOWLEDGE:
            return ImageHandler.imgSharedKnowledge
        if event is ECulturalEvent.DESPOT_HOLIDAY:
            return ImageHandler.imgDespotHoliday
    else:  # back
        if event.getLevel() == 1:
            return ImageHandler.imgCulturalEventIBack
        elif event.getLevel() == 2:
            return ImageHandler.imgCulturalEventIIBack
        else:  # event.getLevel() == 3:
            return ImageHandler.imgCulturalEventIIIBack


def getImageOfMapTile(label, front):
    if front:
        if label is ELabel.MAP_TILE_01:
            return ImageHandler.imgMapTile01
        elif label is ELabel.MAP_TILE_02:
            return ImageHandler.imgMapTile02
        elif label is ELabel.MAP_TILE_03:
            return ImageHandler.imgMapTile03
        elif label is ELabel.MAP_TILE_04:
            return ImageHandler.imgMapTile04
        elif label is ELabel.MAP_TILE_05:
            return ImageHandler.imgMapTile05
        elif label is ELabel.MAP_TILE_06:
            return ImageHandler.imgMapTile06
        elif label is ELabel.MAP_TILE_07:
            return ImageHandler.imgMapTile07
        elif label is ELabel.MAP_TILE_08:
            return ImageHandler.imgMapTile08
        elif label is ELabel.MAP_TILE_09:
            return ImageHandler.imgMapTile09
        elif label is ELabel.MAP_TILE_10:
            return ImageHandler.imgMapTile10
        elif label is ELabel.MAP_TILE_11:
            return ImageHandler.imgMapTile11
        elif label is ELabel.MAP_TILE_12:
            return ImageHandler.imgMapTile12
        elif label is ELabel.MAP_TILE_13:
            return ImageHandler.imgMapTile13
        elif label is ELabel.MAP_TILE_14:
            return ImageHandler.imgMapTile14
        elif label is ELabel.AGYPT:
            return ImageHandler.imgMapTileAgypt
        elif label is ELabel.AMERICA:
            return ImageHandler.imgMapTileAmerica
        elif label is ELabel.CHINA:
            return ImageHandler.imgMapTileChina
        elif label is ELabel.GERMANY:
            return ImageHandler.imgMapTileGermany
        elif label is ELabel.ROME:
            return ImageHandler.imgMapTileRome
        else:  # ELabel.RUSSIA
            return ImageHandler.imgMapTileRussia
    else:  # back
        if label is ELabel.AGYPT:
            return ImageHandler.imgMapTileAgyptBack
        elif label is ELabel.AMERICA:
            return ImageHandler.imgMapTileAmericaBack
        elif label is ELabel.CHINA:
            return ImageHandler.imgMapTileChinaBack
        elif label is ELabel.GERMANY:
            return ImageHandler.imgMapTileGermanyBack
        elif label is ELabel.ROME:
            return ImageHandler.imgMapTileRomeBack
        elif label is ELabel.RUSSIA:
            return ImageHandler.imgMapTileRussiaBack
        else:  # map tile nr back
            return ImageHandler.imgMapTileBack


def getImageOfFigure(fType, color):
    if fType is EFigure.ARMY:
        if color is EColor.BLUE:
            return ImageHandler.imgArmyBlue
        elif color is EColor.GREEN:
            return ImageHandler.imgArmyGreen
        elif color is EColor.YELLOW:
            return ImageHandler.imgArmyYellow
        elif color is EColor.RED:
            return ImageHandler.imgArmyRed
        else:  # White
            return ImageHandler.imgArmyWhite
    else:  # Pioneer
        if color is EColor.BLUE:
            return ImageHandler.imgPioneerBlue
        elif color is EColor.GREEN:
            return ImageHandler.imgPioneerGreen
        elif color is EColor.YELLOW:
            return ImageHandler.imgPioneerYellow
        else:  # Red or no color
            return ImageHandler.imgPioneerRed


def getImageOfBuilding(bType, upgrade):
    if bType is EBuilding.MARINA:
        return ImageHandler.imgMarina
    elif bType is EBuilding.TRADING_POST:
        return ImageHandler.imgTradingPost
    elif bType is EBuilding.BLACKSMITH:
        if upgrade:
            return ImageHandler.imgIronmine
        else:
            return ImageHandler.imgBlacksmith
    elif bType is EBuilding.LIBRARY:
        if upgrade:
            return ImageHandler.imgUniversity
        else:
            return ImageHandler.imgLibrary
    elif bType is EBuilding.GRANARY:
        if upgrade:
            return ImageHandler.imgAqueduct
        else:
            return ImageHandler.imgGranary
    elif bType is EBuilding.MARKET:
        if upgrade:
            return ImageHandler.imgBank
        else:
            return ImageHandler.imgMarket
    elif bType is EBuilding.TEMPLE:
        if upgrade:
            return ImageHandler.imgCathedral
        else:
            return ImageHandler.imgTemple
    else:  # EBuilding.BARRACK
        if upgrade:
            return ImageHandler.imgAcademy
        else:
            return ImageHandler.imgBarrack
