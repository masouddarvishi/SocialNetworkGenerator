import json
import math

class StatsClass:
    """ Class that holds the stats read in the file"""

    def __init__(self, file_url):
        file = open(file_url, 'r')
        data = json.load(file)

        self.races = []

        for race in data["races"]:
            new_race = RaceStat()
            new_race.defineRace(race["race"], race["percentageOfPopulation"])
            new_race.definePercentage(race["description"]["SexualPreference"], race["description"]["Sex"],
                                      race["description"]["SkinTone"], race["description"]["HairColor"])
            self.races.append(new_race)


class RaceStat:
    """ Class that holds the stats for a determined race"""

    def __init__(self):
        self.race = None
        self.percentageOfPopulation = None
        self.percentageOfSex = None
        self.percentageOfSexualPreference = None
        self.percentageOfSkinTone = None
        self.percentageOfHairColor = None

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


def calculate_distance_between_dictionaries(firstDict, secondDict):

    distance = 0
    weight_for_each_key = 1 / len(firstDict.items())

    for key_seen, value_seen in firstDict.items():
        for key_desired, value_desired in secondDict.items():
            if key_seen == key_desired:
                distance += weight_for_each_key * (1 - abs(value_desired - value_seen) /
                                                   (math.sqrt(math.pow(value_desired,2) + math.pow(value_seen,2)) + 1))

    return distance


def retrieve_max_fitness(populations):
    """ Receives an array of individuals and retrieves a new population without the fittest element and
    the fittest population"""

    fittest_population = populations[0]

    for population in populations:
        if population == fittest_population:
            continue
        else:
            if population.fitness > fittest_population.fitness:
                fittest_population = population

    new_population = [pop for pop in populations if pop != fittest_population]

    return new_population, fittest_population
