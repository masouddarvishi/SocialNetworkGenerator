import json


class StatsClass:
    """ Class that holds the stats read in the file"""

    def __init__(self, file_url):
        file = open(file_url, 'r')
        data = json.load(file)

        self.races = []

        for race in data["races"]:
            new_race = RaceStat()
            new_race.defineRace(race["race"], race["percentageOfTotal"])
            new_race.definePercentage(race["description"]["SexualPreference"], race["description"]["Sex"],
                                      race["description"]["SkinTone"], race["description"]["HairColor"])
            self.races.append(new_race)



class RaceStat:
    """ Class that holds the stats for a determined race"""

    def __init__(self):
        self.race = ""
        self.percentageOfPopulation = 0
        self.percentageOfSex = [0] * 3
        self.percentageOfSexualPreference = [0] * 3
        self.percentageOfSkinTone = [] * 3
        self.percentageOfHairColor = [] * 5

    def defineRace(self, race, percentageOfPop):
        """ Defines race and percentage of population"""
        self.race = race
        self.percentageOfPopulation = percentageOfPop

    def definePercentage(self, sexualPreference, percentageOfSex, skinTone, hairColor):
        """ Defines the percentage of sexual preferences and physical appearance"""
        self.percentageOfSexualPreference = sexualPreference
        self.percentageOfSex = percentageOfSex
        self.percentageOfSkinTone = skinTone
        self.percentageOfHairColor = hairColor
