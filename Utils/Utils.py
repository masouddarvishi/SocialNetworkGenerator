import json


class StatsClass:
    """ Class that holds the stats read in the file"""

    def __init__(self, file_url):
        file = open(file_url, 'r')
        self.data = json.load(file)

class RaceStat:
    """ Class that holds the stats for a determined race"""

    def __init__(self):
        self.race = ""
        self.percentageOfPopulation = 0
        self.percentageOfSex = [0] * 3
        self.percentageOfSexualPreference = [0] * 3
        self.percentageOfSkinTone = [] * 3
        self.percentageOfHairColor = [] * 5

    def defineRace(self, race, percentageOfPop, percentageOfSex):
        """ Defines race and percentage of population"""
        self.race = race
        self.percentageOfPopulation = percentageOfPop
        self.percentageOfSex = percentageOfSex

    def definePercentage(self, sexualPreference, skinTone, hairColor):
        """ Defines the percentage of sexual preferences and physical appearance"""
        self.percentageOfSexualPreference = sexualPreference
        self.percentageOfSkinTone = skinTone
        self.percentageOfHairColor = hairColor
