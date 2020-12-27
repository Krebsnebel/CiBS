from CivEnums.EArmyStrength import EArmyStrength
from CivEnums.EBuilding import EBuilding
from CivEnums.EPolity import EPolity
from CivEnums.EResearch import EResearch
from CivEnums.ERotation import ERotation
from CivEnums.EUnitType import EUnitType
from CivEnums.EWonder import EWonder
from CivObjects.Research import Research
from Drawing.EImageObject import EImageObject


"""
this class handles all research cards
function research and draw are implemented
"""


class ResearchManager:

    def __init__(self, civ, imgInfoCivilization, pl):
        self.civilization = civ
        self.imgInfo = imgInfoCivilization
        self.playerNr = pl
        self.unresearchedCards = []
        self.researchedCards_I = []
        self.researchedCards_II = []
        self.researchedCards_III = []
        self.researchedCards_IV = []
        self.researchedCards_V = []

        # level I
        self.unresearchedCards.append(Research(EResearch.IRON_PROCESSING))
        self.unresearchedCards.append(Research(EResearch.LEGISLATION))
        self.unresearchedCards.append(Research(EResearch.CERAMICS))
        self.unresearchedCards.append(Research(EResearch.NAVIGATION))
        self.unresearchedCards.append(Research(EResearch.PHILOSOPHY))
        self.unresearchedCards.append(Research(EResearch.CAVALRY))
        self.unresearchedCards.append(Research(EResearch.SCRIPTURE))
        self.unresearchedCards.append(Research(EResearch.STONE_CARVING))
        self.unresearchedCards.append(Research(EResearch.STOCK_BREEDING))
        self.unresearchedCards.append(Research(EResearch.CURRENCY))

        # level I
        self.unresearchedCards.append(Research(EResearch.IRON_PROCESSING))
        self.unresearchedCards.append(Research(EResearch.LEGISLATION))
        self.unresearchedCards.append(Research(EResearch.CERAMICS))
        self.unresearchedCards.append(Research(EResearch.NAVIGATION))
        self.unresearchedCards.append(Research(EResearch.PHILOSOPHY))
        self.unresearchedCards.append(Research(EResearch.CAVALRY))
        self.unresearchedCards.append(Research(EResearch.SCRIPTURE))
        self.unresearchedCards.append(Research(EResearch.STONE_CARVING))
        self.unresearchedCards.append(Research(EResearch.STOCK_BREEDING))
        self.unresearchedCards.append(Research(EResearch.CURRENCY))

        # level II
        self.unresearchedCards.append(Research(EResearch.CONSTRUCTION_INDUSTRY))
        self.unresearchedCards.append(Research(EResearch.IRRIGATION))
        self.unresearchedCards.append(Research(EResearch.DEMOCRACY))
        self.unresearchedCards.append(Research(EResearch.PRINTING_PRESS))
        self.unresearchedCards.append(Research(EResearch.MECHANICAL_ENGINEERING))
        self.unresearchedCards.append(Research(EResearch.MATHEMATICS))
        self.unresearchedCards.append(Research(EResearch.MONARCHY))
        self.unresearchedCards.append(Research(EResearch.PUBLIC_ADMINISTRATION))
        self.unresearchedCards.append(Research(EResearch.KNIGHTHOOD))
        self.unresearchedCards.append(Research(EResearch.SAILING))

        # level III
        self.unresearchedCards.append(Research(EResearch.BANKING))
        self.unresearchedCards.append(Research(EResearch.BIOLOGY))
        self.unresearchedCards.append(Research(EResearch.STEAM_ENGINE))
        self.unresearchedCards.append(Research(EResearch.RAILROAD))
        self.unresearchedCards.append(Research(EResearch.COMMUNISM))
        self.unresearchedCards.append(Research(EResearch.METAL_CASTING))
        self.unresearchedCards.append(Research(EResearch.MILITARY_SCIENCE))
        self.unresearchedCards.append(Research(EResearch.GUNPOWDER))
        self.unresearchedCards.append(Research(EResearch.THEOLOGY))

        # level IV
        self.unresearchedCards.append(Research(EResearch.NUCLEAR_THEORY))
        self.unresearchedCards.append(Research(EResearch.BALLISTICS))
        self.unresearchedCards.append(Research(EResearch.COMPUTER_TECHNOLOGY))
        self.unresearchedCards.append(Research(EResearch.SPARE_PARTS))
        self.unresearchedCards.append(Research(EResearch.AVIATION))
        self.unresearchedCards.append(Research(EResearch.MASS_MEDIA))
        self.unresearchedCards.append(Research(EResearch.COMBUSTION_ENGINE))

    def research(self, research, desLevel, forced):
        for idx in range(len(self.unresearchedCards)):
            r = self.unresearchedCards[idx]
            if r.research == research:
                l1 = len(self.researchedCards_I)
                l2 = len(self.researchedCards_II)
                l3 = len(self.researchedCards_III)
                l4 = len(self.researchedCards_IV)
                l5 = len(self.researchedCards_V)
                if desLevel == 0:
                    level = r.research.getLevel()
                else:
                    level = desLevel
                if level == 1:
                    self.unresearchedCards.pop(idx)
                    r.setVisible()
                    self.researchedCards_I.append(r)
                    self.imgInfo.setWidth(level, len(self.researchedCards_I))
                    self.executeResearch(r.research)
                    return True
                elif level == 2:
                    if forced or l1 - 1 > l2:
                        self.unresearchedCards.pop(idx)
                        r.setVisible()
                        self.researchedCards_II.append(r)
                        self.imgInfo.setWidth(level, len(self.researchedCards_II))
                        self.executeResearch(r.research)
                        return True
                    else:
                        return False
                elif level == 3:
                    if forced or (l1 > l2 and l2 - 1 > l3):
                        self.unresearchedCards.pop(idx)
                        r.setVisible()
                        self.researchedCards_III.append(r)
                        self.imgInfo.setWidth(level, len(self.researchedCards_III))
                        self.executeResearch(r.research)
                        return True
                    else:
                        return False
                elif level == 4:
                    if forced or (l1 > l2 > l3 and l3 - 1 > l4):
                        self.unresearchedCards.pop(idx)
                        r.setVisible()
                        self.researchedCards_IV.append(r)
                        self.imgInfo.setWidth(level, len(self.researchedCards_IV))
                        self.executeResearch(r.research)
                        return True
                    else:
                        return False
                elif level == 5:
                    if forced or (l1 > l2 > l3 > l4 and l4 - 1 > l5):
                        self.unresearchedCards.pop(idx)
                        r.setVisible()
                        self.researchedCards_V.append(r)
                        self.imgInfo.setWidth(level, len(self.researchedCards_V))
                        self.executeResearch(r.research)
                        return True
                    else:
                        return False
                else:
                    return False
        return False

    def draw(self, window):
        scale = self.imgInfo.getScale()
        resize = EImageObject.RESEARCH_CARDS.getResize()
        i = 0
        for r in self.researchedCards_I:
            imgPos = self.imgInfo.getImgPosOfResearchCard(1, i, True, False)
            r.draw(window, ERotation.NO_ROTATION, imgPos, resize, scale)
            i = i + 1

        i = 0
        for r in self.researchedCards_II:
            imgPos = self.imgInfo.getImgPosOfResearchCard(2, i, True, False)
            r.draw(window, ERotation.NO_ROTATION, imgPos, resize, scale)
            i = i + 1

        i = 0
        for r in self.researchedCards_III:
            imgPos = self.imgInfo.getImgPosOfResearchCard(3, i, True, False)
            r.draw(window, ERotation.NO_ROTATION, imgPos, resize, scale)
            i = i + 1

        i = 0
        for r in self.researchedCards_IV:
            imgPos = self.imgInfo.getImgPosOfResearchCard(4, i, True, False)
            r.draw(window, ERotation.NO_ROTATION, imgPos, resize, scale)
            i = i + 1

    def executeResearch(self, research):
        if research is EResearch.CAVALRY:
            self.civilization.setMovingRange(3)
        elif research is EResearch.CERAMICS:
            self.civilization.unlockBuilding(EBuilding.GRANARY)
            self.civilization.increaseCultureCardLimit()
        elif research is EResearch.CURRENCY:
            self.civilization.unlockBuilding(EBuilding.MARKET)
        elif research is EResearch.IRON_PROCESSING:
            self.civilization.unlockBuilding(EBuilding.BARRACK)
            self.civilization.addWonderWithReducedCosts(EWonder.THE_COLOSSUS)
        elif research is EResearch.LEGISLATION:
            self.civilization.unlockBuilding(EBuilding.TRADING_POST)
            self.civilization.addWonderWithReducedCosts(EWonder.THE_ORACLE)
            self.civilization.unlockPolity(EPolity.REPUBLIC)
        elif research is EResearch.NAVIGATION:
            self.civilization.setPermissionForFigures_MoveOverWater()
        elif research is EResearch.PHILOSOPHY:
            self.civilization.unlockBuilding(EBuilding.TEMPLE)
        elif research is EResearch.SCRIPTURE:
            self.civilization.unlockBuilding(EBuilding.LIBRARY)
        elif research is EResearch.STOCK_BREEDING:
            self.civilization.addWonderWithReducedCosts(EWonder.THE_HANGING_GARDENS)
        elif research is EResearch.STONE_CARVING:
            self.civilization.setFigureLimit(3)
        elif research is EResearch.CONSTRUCTION_INDUSTRY:
            self.civilization.unlockBuilding(EBuilding.BLACKSMITH)
            self.civilization.addWonderWithReducedCosts(EWonder.PORCELAIN_TOWER)
        elif research is EResearch.DEMOCRACY:
            self.civilization.unlockPolity(EPolity.DEMOCRACY)
            self.civilization.setArmyStrength(EUnitType.INFANTRY, EArmyStrength.SECOND_LEVEL)
        elif research is EResearch.IRRIGATION:
            self.civilization.activateThirdCity()
        elif research is EResearch.KNIGHTHOOD:
            self.civilization.unlockPolity(EPolity.FEUDALISM)
            self.civilization.setArmyStrength(EUnitType.CAVALRY, EArmyStrength.SECOND_LEVEL)
        elif research is EResearch.MATHEMATICS:
            self.civilization.setArmyStrength(EUnitType.ARTILLERY, EArmyStrength.SECOND_LEVEL)
        elif research is EResearch.MECHANICAL_ENGINEERING:
            self.civilization.unlockBuilding(EBuilding.AQUEDUCT)
            self.civilization.addWonderWithReducedCosts(EWonder.PANAMA_CANAL)
        elif research is EResearch.MONARCHY:
            self.civilization.addWonderWithReducedCosts(EWonder.CASTLE_HIMEJI)
            self.civilization.unlockPolity(EPolity.MONARCHY)
        elif research is EResearch.PRINTING_PRESS:
            self.civilization.unlockBuilding(EBuilding.UNIVERSITY)
            self.civilization.addWonderWithReducedCosts(EWonder.THE_LOUVRE)
            self.civilization.setFigureLimit(4)
        elif research is EResearch.PUBLIC_ADMINISTRATION:
            self.civilization.increaseCultureCardLimit()
        elif research is EResearch.SAILING:
            self.civilization.setMovingRange(4)
            self.civilization.setPermissionForFigures_StopOnWater()
        elif research is EResearch.BANKING:
            self.civilization.unlockBuilding(EBuilding.BANK)
        elif research is EResearch.BIOLOGY:
            self.civilization.setFigureLimit(5)
        elif research is EResearch.COMMUNISM:
            self.civilization.unlockPolity(EPolity.COMMUNISM)
        elif research is EResearch.GUNPOWDER:
            self.civilization.setArmyStrength(EUnitType.INFANTRY, EArmyStrength.THIRD_LEVEL)
        elif research is EResearch.METAL_CASTING:
            self.civilization.addWonderWithReducedCosts(EWonder.STATUE_OF_LIBERTY)
            self.civilization.setArmyStrength(EUnitType.ARTILLERY, EArmyStrength.THIRD_LEVEL)
        elif research is EResearch.MILITARY_SCIENCE:
            self.civilization.unlockBuilding(EBuilding.ACADEMY)
        elif research is EResearch.RAILROAD:
            self.civilization.unlockBuilding(EBuilding.IRONMINE)
            self.civilization.setArmyStrength(EUnitType.CAVALRY, EArmyStrength.THIRD_LEVEL)
        elif research is EResearch.STEAM_ENGINE:
            self.civilization.setMovingRange(5)
            self.civilization.setPermissionForFigures_StopOnWater()
        elif research is EResearch.THEOLOGY:
            self.civilization.unlockBuilding(EBuilding.CATHEDRAL)
            self.civilization.addWonderWithReducedCosts(EWonder.ANGKOR_WAT)
            self.civilization.unlockPolity(EPolity.FUNDAMENTALISM)
            self.civilization.increaseCultureCardLimit()
        elif research is EResearch.AVIATION:
            self.civilization.setMovingRange(6)
            self.civilization.setPermissionForFigures_StopOnWater()
            self.civilization.setArmyStrength(EUnitType.AIR_FORCE, EArmyStrength.AIR_FORCE)
        elif research is EResearch.BALLISTICS:
            self.civilization.setArmyStrength(EUnitType.ARTILLERY, EArmyStrength.FORTH_LEVEL)
        elif research is EResearch.COMBUSTION_ENGINE:
            self.civilization.setArmyStrength(EUnitType.CAVALRY, EArmyStrength.FORTH_LEVEL)
        elif research is EResearch.COMPUTER_TECHNOLOGY:
            self.civilization.setAsResearched(EResearch.COMPUTER_TECHNOLOGY)
        elif research is EResearch.MASS_MEDIA:
            pass
        elif research is EResearch.NUCLEAR_THEORY:
            pass
        elif research is EResearch.SPARE_PARTS:
            self.civilization.setArmyStrength(EUnitType.INFANTRY, EArmyStrength.FORTH_LEVEL)
            self.civilization.setFigureLimit(6)
        elif research is EResearch.ASTRONAUTICS:
            pass
        else:
            print("research error")
