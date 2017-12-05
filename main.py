from AlgGenetic.GeneticAlgorithm import GeneticAlgorithm
from Utils import Utils
from Individual import Population

def initiate_genetic_population():
    genetic = GeneticAlgorithm()

    i = 0
    while i < 10000:

        genetic.determine_new_generation_parents()
        genetic.determine_crossover()

        _, max_fit = Utils.retrieve_max_fitness(genetic.population)
        #assert isinstance(max_fit, Population)

        print(max_fit.fitness)

        i += 1


if __name__ == "__main__":
    initiate_genetic_population()
