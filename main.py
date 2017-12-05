from AlgGenetic.GeneticAlgorithm import GeneticAlgorithm
from Utils import Utils
from Individual import Population

def initiate_genetic_population():
    genetic = GeneticAlgorithm()

    max_fit = None
    i = 0
    while i < 1000:

        genetic.determine_new_generation_parents()
        genetic.determine_crossover()
        genetic.determine_mutation()

        _, max_fit = Utils.retrieve_max_fitness(genetic.generation)
        #assert isinstance(max_fit, Population)

        print(str(i) + ":" + str(max_fit.fitness))

        i += 1



if __name__ == "__main__":
    initiate_genetic_population()
