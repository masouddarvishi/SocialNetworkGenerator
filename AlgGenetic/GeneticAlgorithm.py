from Individual.Population import Population
from Utils.Utils import retrieve_max_fitness

import random


class GeneticAlgorithm:

    def __init__(self, mutation_probability = 0.08):

        self.generation = []
        self.mutation_probability = mutation_probability

        for i in range(0, 4):
            p = Population()
            p.create_random_population()
            p.calculate_fitness()
            self.generation.append(p)

    def determine_new_generation_parents(self):
        """ Responsible for the selection of the fittest"""

        next_generation = []
        sum_of_fitness = 0
        sum_of_fitness_by_index = []

        # Roulette Wheel Selection
        for pop in self.generation:
            assert isinstance(pop, Population)
            sum_of_fitness += pop.fitness
            sum_of_fitness_by_index.append(sum_of_fitness)

        while len(next_generation) < len(self.generation)/2:

            random_int = random.randint(0, int(sum_of_fitness))

            for index in range(len(sum_of_fitness_by_index)):
                if random_int <= sum_of_fitness_by_index[index]:
                    next_generation.append(self.generation[index])


        self.generation = next_generation

    def determine_crossover(self):
        """ Chooses a random crossover point and creates the offspring"""

        size_of_population = len(self.generation[0].group)

        crossover_point = random.randint(0, size_of_population)
        first_mate, second_mate = self.generation[0], self.generation[1]

        assert isinstance(first_mate, Population)
        assert isinstance(second_mate, Population)

        offspring_1, offspring_2 = Population(), Population()

        offspring_1.group = second_mate.group[:crossover_point] + first_mate.group[crossover_point:]
        offspring_2.group = first_mate.group[:crossover_point] + second_mate.group[crossover_point + 1:]
        self.generation.append(offspring_1)
        self.generation.append(offspring_2)

    def determine_mutation(self):
        """ Generates a new random person as a result of the mutation"""
        assert isinstance(self.generation, list)

        for indx, pop in enumerate(self.generation):
            if indx > (len(self.generation)/2):
                # if offspring
                for index_ind, individual in enumerate(pop.group):
                    rnd_value = random.randint(0, 100)
                    if rnd_value < (self.mutation_probability * 100):
                        pop.group[index_ind] = Population.create_random_person()

    def calculate_all_fitness(self):
        """ Responsible for calculating all the population's fitness """
        for pop in self.generation:
            pop.calculate_fitness()

    def print(self):
        for i in range(0, len(self.generation)):
            print(self.generation[i])
