import secrets
import random

from Utils.Utils import StatsClass
from Individual.Person import *


class Population:
    """Class that contains all the people from a city"""

    def __init__(self):
        self.group = []
        self.fitness = 0
        self.statisticalObject = StatsClass("data.json")

    def create_random_population(self):
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

        print(self.calculate_fitness())

    def stats_per_race(self, race):
        """ Received a race as argument and returns data about the existent population"""

        number_of_people = 1
        number_sexual_pref = {SexualPreference.HOMOSEXUAL: 0, SexualPreference.HETERO: 0, SexualPreference.BISEXUAL: 0}
        number_sex = {Sex.MALE: 0, Sex.FEMALE: 0, Sex.OTHER: 0}
        number_skin_tone = {SkinTone.LIGHT: 0, SkinTone.MEDIUM: 0, SkinTone.DARK: 0}
        number_hair_color = {HairColor.BROWN: 0, HairColor.DARK: 0, HairColor.RED: 0, HairColor.BLONDE: 0, HairColor.WHITE: 0}

        for person in self.group:
            if person.race == race:
                number_of_people += 1
                number_sexual_pref[person.sexualPreference] += 1
                number_sex[person.sex] += 1
                number_skin_tone[person.skinTone] += 1
                number_hair_color[person.hairColor] += 1

        population_statistics_by_race = {
            "race": race,
            "percentageOfTotal": number_of_people / len(self.group),
            "description": {
                "SexualPreference": {
                    "Heterosexual": number_sexual_pref[SexualPreference.HETERO] / number_of_people,
                    "Homosexual": number_sexual_pref[SexualPreference.HOMOSEXUAL] / number_of_people,
                    "Bisexual": number_sexual_pref[SexualPreference.BISEXUAL] / number_of_people
                },
                "Sex": {
                    "Male": number_sex[Sex.MALE] / number_of_people,
                    "Female": number_sex[Sex.FEMALE] / number_of_people,
                    "Other": number_sex[Sex.OTHER] / number_of_people
                },
                "SkinTone": {
                    "Light": number_skin_tone[SkinTone.LIGHT] / number_of_people,
                    "Medium": number_skin_tone[SkinTone.MEDIUM] / number_of_people,
                    "Dark": number_skin_tone[SkinTone.DARK] / number_of_people
                },
                "HairColor": {
                    "Brown": number_hair_color[HairColor.BROWN] / number_of_people,
                    "Dark": number_hair_color[HairColor.DARK] / number_of_people,
                    "Red": number_hair_color[HairColor.RED] / number_of_people,
                    "Blonde": number_hair_color[HairColor.BLONDE] / number_of_people,
                    "White": number_hair_color[HairColor.WHITE] / number_of_people,
                }
            }
        }

        return population_statistics_by_race

    def calculate_fitness(self):

        #Stats by race
        list_stats_by_race = []
        for race in self.statisticalObject.races:
            list_stats_by_race.append(self.stats_per_race(race.race))

        return

    def __str__(self):
        string_to_return = ''
        for p in self.group:
            string_to_return += str(p) + '\n'
        return string_to_return
