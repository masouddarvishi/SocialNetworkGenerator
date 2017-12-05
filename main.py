from AlgGenetic.GeneticAlgorithm import GeneticAlgorithm


def initiate_genetic_population():
    genetic = GeneticAlgorithm()

    i = 0
    while i < 100:

        genetic.determine_offspring()
        i += 1

    genetic.print()

if __name__ == "__main__":
    initiate_genetic_population()
