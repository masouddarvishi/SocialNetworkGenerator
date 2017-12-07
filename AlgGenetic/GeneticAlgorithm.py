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

        print("Parents B: " + str(len(self.generation)))

        next_generation = []
        sum_of_fitness = 0
        sum_of_fitness_by_index = []

        # Roulette Wheel Selection
        for pop in self.generation:
            assert isinstance(pop, Population)
            sum_of_fitness += pop.fitness
            sum_of_fitness_by_index.append(sum_of_fitness)

        while len(next_generation) < 2:#len(self.generation)/2:
            random_int = random.randint(0, int(sum_of_fitness))

            for index in range(len(sum_of_fitness_by_index)):
                if random_int <= sum_of_fitness_by_index[index]:
                    next_generation.append(self.generation[index])

        self.generation = next_generation

        print("Parents E: " + str(len(self.generation)))

    def determine_crossover(self):
        """ Creates a new offspring with bias"""

        new_generation_size = len(self.generation)
        # Bias uniform crossover
        for index in range(0, new_generation_size, 2):
           # print(str(index) + '____' + str(len(self.generation)))
            #print(index)
            first_mate, second_mate = self.generation[index], self.generation[index + 1]
            offspring_1, offspring_2 = Population(), Population()

            assert isinstance(first_mate, Population)
            assert isinstance(second_mate, Population)

            # bias
            frst_m_prb = 0.6 if first_mate.fitness > second_mate.fitness else 0.4

            for chrom in range(0, len(first_mate.group)):
                # first offspring
                rnd = random.uniform(0.0, 1.0)
                offspring_1.group.append(first_mate.group[chrom] if rnd <= frst_m_prb else second_mate.group[chrom])

                #second offspring
                rnd = random.randrange(0, 1)
                offspring_2.group.append(first_mate.group[chrom] if rnd <= frst_m_prb else second_mate.group[chrom])

            self.generation.append(offspring_1)
            self.generation.append(offspring_2)


    def determine_mutation(self):
        """ Generates a new random person as a result of the mutation"""
        assert isinstance(self.generation, list)

        for indx, pop in enumerate(self.generation):
            if indx >= (len(self.generation)/2):
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
