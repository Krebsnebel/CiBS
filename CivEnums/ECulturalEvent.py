from enum import Enum

from CivEnums.EVisibility import EVisibility


class ECulturalEvent(Enum):

    def __init__(self, lev, na, img):
        self.level = lev
        self.polityName = na
        self.imgNameFront = img
        self.imgNameBack = "CultureCard"
        if self.level == 1:
            self.prefix = "I_"
        elif self.level == 2:
            self.prefix = "II_"
        else:
            self.prefix = "III_"

    def getPrefix(self):
        return self.prefix

    def getLevel(self):
        return self.level

    def getImgName(self, visible):
        if visible is EVisibility.FOR_NOBODY:
            return self.imgNameBack
        else:
            return self.imgNameFront

    REVOLTING_CITIZENS_1 = (1, "Die Bürger revoltieren!", "RevoltingCitizens")
    REVOLTING_CITIZENS_2 = (2, "Die Bürger revoltieren!", "RevoltingCitizens")
    DISORIENTED = (1, "Orientierungslos", "Disoriented")
    DISASTER = (3, "Desaster", "Disaster")
    CATASTROPHE = (2, "Katastrophe", "Catastrophe")
    PRESIDENT_HOLIDAY = (3, "Präsidenten-Feiertag!", "PresidentHoliday")
    DISPLACED = (3, "Deplatziert", "Displaced")
    LOST = (2, "Verirrt", "Lost")

    A_PRINCELY_GIFT = (3, "Ein fürstliches Geschenk", "APrincelyGift")
    MASS_EXODUS = (2, "Massenflucht", "MassExodus")
    IDEASMITH = (3, "Ideenschmiede", "Ideasmith")
    DEFORESTATION = (2, "Abholzung", "Deforestation")
    SABOTAGE = (1, "Sabotage", "Sabotage")
    BREAD_AND_GAMES = (1, "Brot und Spiele", "BreadAndGames")
    FAITHLESS = (1, "Treulos", "Faithless")
    DROUGHT = (1, "Dürre", "Drought")
    LONG_LIVE_THE_QUEEN = (2, "Lang lebe die Königin!", "LongLiveTheQueen")
    GENERAL_DESERTION = (3, "Allgemeine Fahnenflucht", "GeneralDesertion")
    PRIME_TIME = (3, "Beste Sendezeit!", "PrimeTime")
    KNIGHT_TOURNAMENT = (2, "Ritterturnier", "KnightTournament")

    GIFT_FROM_A_DISTANCE = (1, "Ein Geschenk aus der Ferne", "GiftFromADistance")
    EXCHANGE_OF_IDEAS = (1, "Austausch von Ideen", "ExchangeOfIdeas")
    GENEROUS_GIFT = (2, "Ein großzügiges Geschenk", "GenerousGift")
    SHARED_KNOWLEDGE = (2, "Geteiltes Wissen", "SharedKnowledge")
    DESPOT_HOLIDAY = (1, "Despoten Feiertag!", "DespotHoliday")
