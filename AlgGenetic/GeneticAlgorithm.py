from Individual.Population import Population
from Utils.Utils import retrieve_max_fitness


class GeneticAlgorithm:

    def __init__(self):

        self.population = []

        for i in range(0, 1):
            p = Population()
            p.create_random_population()
            self.population.append(p)

    def determine_offspring(self):
        """ Responsible for selection the fittest and creating the offspring  """

        new_population, fittest = retrieve_max_fitness(self.population)
        _, second_fittest = retrieve_max_fitness(new_population)




    def print(self):
        for i in range(0, len(self.population)):
            print(self.population[i])