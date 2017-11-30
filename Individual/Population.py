import secrets
import random

from Individual.Person import *


class Population:
    """Class that contains all the people from a city"""

    def __init__(self):
        self.group = []
        self.fitness = 0

    def createRandomPopulation(self):
        """ Creates a random population of 100 people"""
        for p in range(0, 300):
            name = secrets.token_hex(5)
            race = random.choice(list(Race))
            sexualPreference = random.choice(list(SexualPreference))
            sex = random.choice(list(Sex))
            height = random.choice([n for n in range(110, 200)])
            weight = random.choice([n for n in range(50, 150)])
            fatpercentage = random.choice([n for n in range(1, 40)])
            skinTone = random.choice(list(SkinTone))
            hairColor = random.choice(list(HairColor))

            newPerson = Person(name, race, "empty", sexualPreference, sex, height, weight, fatpercentage, skinTone,
                               hairColor)
            self.group.append(newPerson)

    def __str__(self):
        stringToReturn = ''
        for p in self.group:
            stringToReturn += str(p) + '\n'
        return stringToReturn

    def calculateFitness(self):
        return 0
