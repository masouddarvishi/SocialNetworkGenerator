import secrets

from numpy import random

from Individual.Person import *


class Population:
    """Class that contains all the people from a city"""

    def __init__(self):
        self.population = []
        self.fitness = 0

    def createRandomPopulation(self):
        """ Creates a random population of 100 people"""
        for p in range(0, 100):
            name = secrets.token_hex(15)
            race = random.choice(list(Race))
            sexualPreference = random.choice(list(SexualPreference))
            sex = random.choice(list(Sex))
            height = random.choice(110, 200)
            weight = random.choice(50, 150)
            fatpercentage = random.choice(1, 40)
            skinTone = random.choice(list(SkinTone))
            hairColor = random.choice(list(HairColor))

            newPerson = Person(name, race, [], sexualPreference, sex, height, weight, fatpercentage, skinTone,
                               hairColor)
            self.population.append(newPerson)

    def printPopulation(self):
        return
        # print(self.population)

    def calculateFitness(self):
        return 0
