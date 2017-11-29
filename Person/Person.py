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


class SexualPreference(Enum):
    HETERO = 1
    HOMOSEXUAL = 2
    BISEXUAL = 3


class Person:
    """A class that represents a person generated """

    def __init__(self, name, parents, sexualpreference, sex, height, weight, fatpercentage, skintone, haircolor):
        # constants through life
        self.name = name
        self.parents = parents
        self.sexualPreference = sexualpreference
        self.sex = sex
        self.height = height
        self.weight = weight
        self.fatPercentage = fatpercentage
        self.skinTone = skintone
        self.hairColor = haircolor
