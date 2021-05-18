import numpy as np
import random

class Population:
    def __init__(self, individuals, initialList):
        """
        individuals is a list of individual objects
        initialList is the list of relative numbers given at the beginning
        """
        self.individuals = individuals
        self.initialList = initialList
        self.l = len(initialList)


    """
    STEP 2 :
    Crossovers
    """

    def crossoverIndividuals(self, firstIndividual, otherIndividual, crossoverPoint):
        a = firstIndividual.geneticCode
        b = otherIndividual.geneticCode
        for i in range(crossoverPoint,self.l):
            a.pop(-1)
        for i in range(crossoverPoint):
            b.pop(0)
        return a + b

    def crossoverOfSelectedIndividuals(self, individual1, individual2):
        newIndividual1 = self.crossoverIndividuals(individual1, individual2, randint(0,self.l))
        newIndividual2 = self.crossoverIndividuals(individual2, individual1, randint(0,self.l))
        return [newIndividual1, newIndividual2]


    """
    STEP 3 :
    Mutations
    """

    def mutateIndividuals(self, individual):
        for i in range(self.l):
            if random.randint(0,self.l) == 0:
                individual.geneticCode[i] = -individual.geneticCode[i] + 1


    """
    STEP 4 :
    Elitism
    """

    def sortIndividualsByFitness(self, population):
        return sorted(population.individuals, key = lambda x: x.fitness)

    def createNewPopulationWithElitism(self, newIndividuals):
        pourcentageOfNewIndividuals = 0.9
        numberOfNewIndividuals = round(pourcentageOfNewIndividuals * self.l)
        numberOfOlfIndividuals = self.l - numberOfNewIndividuals
        newIndividuals = self.sortIndividualByFitness(newPopulation)[:numberOfNewIndividuals]
        oldIndividuals = self.sortIndividualByFitness(self.individuals)[:numberOfOldIndividuals]
        return oldIndividuals + newIndividuals


    """
    STEP 5 :
    UPDATE THE BEST ANSWER
    """
    def updateBestAnswer(self, answer):
        return 0

    """
    SUM UP
    """
    def main(self):
        return True
        """
        STEP 1 TO BE DONE
        """




class Individual(Population):
    def __init__(self, geneticCode, fitness):
        """
        geneticCode is a list of 0 and 1 linked to a specific list :
        - if there is a 0 at position i, this means that the number list[i] is not in the individual
        - if there is a 1 at position i, this means that the number list[i] is in the individual
        """
        self.geneticCode = geneticCode
        self.fitness = fitness

    def evaluateFitness(self):
        return np.abs(np.dot(initialList, geneticCode))

    def sumOfList(self):
        return np.abs(np.dot(initialList, geneticCode))

    def lenOfIndividual(self, individual):
        return np.dot(np.ones(len(initialList)), individual)