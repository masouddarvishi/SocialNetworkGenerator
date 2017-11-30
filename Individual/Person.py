from enum import Enum


class Sex(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3


class Race(Enum):
    WHITE = 1
    BLACK = 2
    HISPANIC = 3
    ASIAN = 4


class SkinTone(Enum):
    LIGHT = 1
    MEDIUM = 2
    DARK = 3


class SexualPreference(Enum):
    HETERO = 1
    HOMOSEXUAL = 2
    BISEXUAL = 3


class HairColor(Enum):
    BROWN = 1
    DARK = 2
    RED = 3
    BLONDE = 4
    WHITE = 5


class Person:
    """A class that represents a person generated """

    def __init__(self, name, race, parents, sexualpreference, sex, height, weight, fatpercentage, skinTone, hairColor):
        # constants through life
        self.name = name
        self.race = race
        self.parents = parents
        self.sexualPreference = sexualpreference
        self.sex = sex
        self.height = height
        self.weight = weight
        self.fatPercentage = fatpercentage
        self.skinTone = skinTone
        self.hairColor = hairColor

    def __str__(self):
        return self.name + ", " + self.race + ", " + self.parents + ", " + self.sexualPreference + ", " + self.sex + \
               ", " + self.height + ", " + self.weight + ", " + self.fatPercentage + ", " + self.skinTone + ", " \
               + self.hairColor
