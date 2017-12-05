import secrets
import random

from Utils.Utils import *
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
            new_person = Population.create_random_person()
            self.group.append(new_person)

    @staticmethod
    def create_random_person(self):
        name = secrets.token_hex(5)
        race = random.choice(list(Race))
        sexual_preference = random.choice(list(SexualPreference))
        sex = random.choice(list(Sex))
        height = random.choice([n for n in range(110, 200)])
        weight = random.choice([n for n in range(50, 150)])
        fat_percentage = random.choice([n for n in range(1, 40)])
        skin_tone = random.choice(list(SkinTone))
        hair_color = random.choice(list(HairColor))

        new_person = Person(name, race, "empty", sexual_preference, sex, height, weight, fat_percentage, skin_tone,
                            hair_color)

        return new_person

    def stats_per_race(self, race):
        """ Received a race as argument and returns data about the existent population"""

        race = Population.cast_race_string(race)
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
            "percentageOfPopulation": number_of_people / len(self.group),
            "description": {
                "SexualPreference": {
                    "Heterosexual": 100 * number_sexual_pref[SexualPreference.HETERO] / number_of_people,
                    "Homosexual": 100 * number_sexual_pref[SexualPreference.HOMOSEXUAL] / number_of_people,
                    "Bisexual": 100 * number_sexual_pref[SexualPreference.BISEXUAL] / number_of_people
                },
                "Sex": {
                    "Male": 100 * number_sex[Sex.MALE] / number_of_people,
                    "Female": 100 * number_sex[Sex.FEMALE] / number_of_people,
                    "Other": 100 * number_sex[Sex.OTHER] / number_of_people
                },
                "SkinTone": {
                    "Light": 100 * number_skin_tone[SkinTone.LIGHT] / number_of_people,
                    "Medium": 100 * number_skin_tone[SkinTone.MEDIUM] / number_of_people,
                    "Dark": 100 * number_skin_tone[SkinTone.DARK] / number_of_people
                },
                "HairColor": {
                    "Brown": 100 * number_hair_color[HairColor.BROWN] / number_of_people,
                    "Dark": 100 * number_hair_color[HairColor.DARK] / number_of_people,
                    "Red": 100 * number_hair_color[HairColor.RED] / number_of_people,
                    "Blonde": 100 * number_hair_color[HairColor.BLONDE] / number_of_people,
                    "White": 100 * number_hair_color[HairColor.WHITE] / number_of_people,
                }
            }
        }

        return population_statistics_by_race

    def calculate_fitness(self):

        fitness = 0

        # Stats by race
        list_stats_by_race = []
        for race in self.statisticalObject.races:
            list_stats_by_race.append(self.stats_per_race(race.race))

        # calculate fitness
        for stats_seen in list_stats_by_race:
            for real_stats in self.statisticalObject.races:
                if stats_seen['race'] == Population.cast_race_string(real_stats.race):
                    fitness += (1 - abs(stats_seen["percentageOfPopulation"] - (real_stats.percentageOfPopulation /
                                                                                100)))
                    fitness += Population.determine_distance(stats_seen["description"], real_stats)

        self.fitness = fitness

    @staticmethod
    def determine_distance(object_seen, object_desired):

        fitness = 0
        weight_of_each_section = 1 / len(object_seen)

        # Sexual Preference
        sexual_pref_fitness = calculate_distance_between_dictionaries(object_seen["SexualPreference"],
                                                                      object_desired.percentageOfSexualPreference)

        # Sex
        sex_fitness = calculate_distance_between_dictionaries(object_seen["Sex"], object_desired.percentageOfSex)

        # Skin Tone
        skin_tone_fitness = calculate_distance_between_dictionaries(object_seen["SkinTone"],
                                                                    object_desired.percentageOfSkinTone)

        # Hair Color
        hair_color_fitness = calculate_distance_between_dictionaries(object_seen["HairColor"],
                                                                     object_desired.percentageOfHairColor)

        fitness += weight_of_each_section * sexual_pref_fitness + weight_of_each_section * sex_fitness\
                   + weight_of_each_section * skin_tone_fitness + weight_of_each_section * hair_color_fitness

        return fitness

    @staticmethod
    def cast_race_string(race):
        """ Receives a string representing a race and converts it to a race enum"""
        if race == "White":
            return Race.WHITE
        elif race == "Black":
            return Race.BLACK
        elif race == "Hispanic":
            return Race.HISPANIC
        else:
            return Race.ASIAN

    def __str__(self):
        string_to_return = ''
        for p in self.group:
            string_to_return += str(p) + '\n'
        return string_to_return
