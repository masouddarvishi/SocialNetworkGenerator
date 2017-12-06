from AlgGenetic.GeneticAlgorithm import GeneticAlgorithm
from Utils import Utils


def initiate_genetic_population():
    genetic = GeneticAlgorithm()

    i = 0
    while i < 100000:

        genetic.determine_new_generation_parents()
        genetic.determine_crossover()
        genetic.determine_mutation()

        genetic.calculate_all_fitness()

        _, max_fit = Utils.retrieve_max_fitness(genetic.generation)

        print(str(i) + ":" + str(max_fit.fitness))

        if max_fit.fitness <= 50:
            break

        i += 1

    print(max_fit.stats_per_race("White"))



if __name__ == "__main__":
    initiate_genetic_population()
