from Individual.Population import Population


def initiatePopulation():
    pop = Population()
    pop.createRandomPopulation()
    pop.printPopulation()


if __name__ == "__main__":
    initiatePopulation()
