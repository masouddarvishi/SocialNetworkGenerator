from Individual.Population import Population


class GeneticAlgorithm:

    def __init__(self):
        self.population = []

        for i in range(0, 4):
            p = Population()
            p.createRandomPopulation()
            self.population.append(p)

    def print(self):
        for i in range(0, len(self.population)):
            print(self.population[i])