from Individual.Population import Population


def initiatePopulation():
    pop = Population()
    pop.createRandomPopulation()


if __name__ == "__main__":
    initiatePopulation()
