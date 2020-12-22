from CivEnums.EResearch import EResearch
from CivEnums.ERotation import ERotation
from CivObjects.Research import Research
from Drawing.EImageObject import EImageObject


"""
this class handles all research cards
function research and draw are implemented
"""


class ResearchManager:

    def __init__(self, imgInfoCivilization, pl):
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
                    return True
                elif level == 2:
                    if forced or l1 - 1 > l2:
                        self.unresearchedCards.pop(idx)
                        r.setVisible()
                        self.researchedCards_II.append(r)
                        self.imgInfo.setWidth(level, len(self.researchedCards_II))
                        return True
                    else:
                        return False
                elif level == 3:
                    if forced or (l1 > l2 and l2 - 1 > l3):
                        self.unresearchedCards.pop(idx)
                        r.setVisible()
                        self.researchedCards_III.append(r)
                        self.imgInfo.setWidth(level, len(self.researchedCards_III))
                        return True
                    else:
                        return False
                elif level == 4:
                    if forced or (l1 > l2 > l3 and l3 - 1 > l4):
                        self.unresearchedCards.pop(idx)
                        r.setVisible()
                        self.researchedCards_IV.append(r)
                        self.imgInfo.setWidth(level, len(self.researchedCards_IV))
                        return True
                    else:
                        return False
                elif level == 5:
                    if forced or (l1 > l2 > l3 > l4 and l4 - 1 > l5):
                        self.unresearchedCards.pop(idx)
                        r.setVisible()
                        self.researchedCards_V.append(r)
                        self.imgInfo.setWidth(level, len(self.researchedCards_V))
                        return True
                    else:
                        return False
                else:
                    return False
        return False

    def draw(self, window):
        resize = self.imgInfo.getResize(EImageObject.RESEARCH_CARDS)
        i = 0
        for r in self.researchedCards_I:
            imgPos = self.imgInfo.getImgPosOfResearchCard(1, i, True)
            r.draw(window, ERotation.NO_ROTATION, imgPos, resize)
            i = i + 1

        i = 0
        for r in self.researchedCards_II:
            imgPos = self.imgInfo.getImgPosOfResearchCard(2, i, True)
            r.draw(window, ERotation.NO_ROTATION, imgPos, resize)
            i = i + 1

        i = 0
        for r in self.researchedCards_III:
            imgPos = self.imgInfo.getImgPosOfResearchCard(3, i, True)
            r.draw(window, ERotation.NO_ROTATION, imgPos, resize)
            i = i + 1

        i = 0
        for r in self.researchedCards_IV:
            imgPos = self.imgInfo.getImgPosOfResearchCard(4, i, True)
            r.draw(window, ERotation.NO_ROTATION, imgPos, resize)
            i = i + 1
