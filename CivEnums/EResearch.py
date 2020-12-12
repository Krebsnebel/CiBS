from enum import Enum


class EResearch(Enum):

    def __init__(self, lev, na, img):
        self.level = lev
        self.researchName = na
        self.imgName = img
        if self.level == 1:
            self.imgBackName = "I_Research"
        elif self.level == 2:
            self.imgBackName = "II_Research"
        elif self.level == 3:
            self.imgBackName = "III_Research"
        elif self.level == 4:
            self.imgBackName = "IV_Research"
        elif self.level == 5:
            self.imgBackName = "V_Research"
        else:
            self.imgBackName = "-"

    def getLevel(self):
        return self.level

    def getName(self):
        return self.researchName

    def getImgFrontName(self):
        return self.imgName

    def getImgBackName(self):
        return self.imgBackName

    NONE = (0, "keine Forschung", "-")
    IRON_PROCESSING = (1, "Eisenverarbeitung", "I_IronProcessing")
    LEGISLATION = (1, "Gesetzgebung", "I_Legislation")
    CERAMICS = (1, "Keramik", "I_Ceramics")
    NAVIGATION = (1, "Navigation", "I_Navigation")
    PHILOSOPHY = (1, "Philosophie", "I_Philosophy")
    CAVALRY = (1, "Reiterei", "I_Cavalry")
    SCRIPTURE = (1, "Schrift", "I_Scripture")
    STONE_CARVING = (1, "Steinmetzkunst", "I_StoneCarving")
    STOCK_BREEDING = (1, "Tierzucht", "I_StockBreeding")
    CURRENCY = (1, "Währung", "I_Currency")
    CONSTRUCTION_INDUSTRY = (2, "Bauwesen", "II_ConstructionIndustry")
    IRRIGATION = (2, "Bewässerung", "II_Irrigation")
    DEMOCRACY = (2, "Demokratie", "II_Democracy")
    PRINTING_PRESS = (2, "Druckerpresse", "II_PrintingPress")
    MECHANICAL_ENGINEERING = (2, "Maschinenbau", "II_MechanicalEngineering")
    MATHEMATICS = (2, "Mathematik", "II_Mathematics")
    MONARCHY = (2, "Monarchie", "II_Monarchy")
    PUBLIC_ADMINISTRATION = (2, "öffentliche Verwaltungsarbeit", "II_PublicAdministration")
    KNIGHTHOOD = (2, "Rittertum", "II_Knighthood")
    SAILING = (2, "Segeln", "II_Sailing")
    BANKING = (3, "Bankwesen", "III_Banking")
    BIOLOGY = (3, "Biologie", "III_Biology")
    STEAM_ENGINE = (3, "Dampfmaschine", "III_SteamEngine")
    RAILROAD = (3, "Eisenbahn", "III_Railroad")
    COMMUNISM = (3, "Kommunismus", "III_Communism")
    METAL_CASTING = (3, "Metallguss", "III_MetalCasting")
    MILITARY_SCIENCE = (3, "Militärwissenschaften", "III_MilitaryScience")
    GUNPOWDER = (3, "Schießpulver", "III_Gunpowder")
    THEOLOGY = (3, "Theologie", "III_Theology")
    NUCLEAR_THEORY = (4, "Atomtheorie", "IV_NuclearTheory")
    BALLISTICS = (4, "Balistik", "IV_Ballistics")
    COMPUTER_TECHNOLOGY = (4, "Computertechnologie", "IV_ComputerTechnology")
    SPARE_PARTS = (4, "Ersatzteile", "IV_SpareParts")
    AVIATION = (4, "Luftfahrt", "IV_Aviation")
    MASS_MEDIA = (4, "Massenmedien", "IV_MassMedia")
    COMBUSTION_ENGINE = (4, "Verbrennungsmotor", "IV_CombustionEngine")
    ASTRONAUTICS = (5, "Raumfahrt", "V_Astronautics")
