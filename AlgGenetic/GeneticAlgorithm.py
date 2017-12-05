from Individual.Population import Population
from Utils.Utils import retrieve_max_fitness

import random


class GeneticAlgorithm:

    def __init__(self):

        self.population = []

        for i in range(0, 4):
            p = Population()
            p.create_random_population()
            p.calculate_fitness()
            self.population.append(p)

    def determine_new_generation_parents(self):
        """ Responsible for the selection of the fittest"""

        next_generation = []

        # Selection
        new_population_temp, fittest = retrieve_max_fitness(self.population)
        _, second_fittest = retrieve_max_fitness(new_population_temp)

        next_generation.append(fittest)
        next_generation.append(second_fittest)

        self.population = next_generation

    def determine_crossover(self):
        """ Chooses a random crossover point and creates the offspring"""

        size_of_population = len(self.population[0].group)

        crossover_point = random.randint(0, size_of_population)
        first_mate, second_mate = self.population[0], self.population[1]

        assert isinstance(first_mate, Population)
        assert isinstance(second_mate, Population)

        offspring_1, offspring_2 = Population(), Population()

        offspring_1.group = second_mate.group[0: crossover_point] + first_mate.group[crossover_point + 1:
                                                                                     size_of_population]
        offspring_2.group = first_mate.group[0: crossover_point] + second_mate.group[crossover_point + 1:
                                                                                     size_of_population]

        offspring_1.calculate_fitness()
        offspring_2.calculate_fitness()

        self.population.append(offspring_1)
        self.population.append(offspring_2)

    def print(self):
        for i in range(0, len(self.population)):
            print(self.population[i])