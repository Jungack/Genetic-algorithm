# -*- coding: utf-8 -*-

import numpy as np
import random as rd

class Population:
    def __init__(self, initialList):
        """
        individuals is a list of individual objects
        initialList is the list of relative numbers given at the beginning
        """
        self.initialList = initialList
        self.individuals = self.generateIndividuals()
        self.l = len(initialList)


    """
    BASIC METHODS
    """

    def generateIndividuals(self):
        return 0

    def sortIndividualsByFitness(self):
        return sorted(self.individuals, key = lambda x: x.fitness)

    def evaluateFitness(self, individual):
        return np.abs(np.dot(self.initialList, individual.geneticCode))

    def setFitness(self, individual):
        individual.fitness = self.evaluateFitness(individual)

    def sumOfList(self, individual):
        return np.abs(np.dot(self.initialList, individual.geneticCode))

    def lenOfIndividual(self, individual):
        return np.dot(np.ones(self.l), individual.geneticCode)


    """
    STEP 1:
    Tournament
    """

    def selectTwoIndividualsByTournament(self):
        selected_individuals = rd.choices(self.individuals, k = floor(0.1*self.l))
        length = len(selected_individuals)
        listOfFitness = np.array([selected_individuals[i].fitness for i in range(length))])
        weights = [100/(listOfFitness[i]*sum(1/listOfFitness)) for i in range(length)]
        finalTwoIndividuals = []
        for step in range(2):
            index = 0
            pickANumber = rd.random()
            while ((pickANumber - weights[index]/100) > 0):
                pickANumber -= weights[index]/100
                index++
            finalTwoIndividuals.append(selected_individuals[index])
        return finalTwoIndividuals


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
        self.individuals = self.sortIndividualsByFitness(oldIndividuals + newIndividuals)


    """
    STEP 5 :
    UPDATE THE BEST ANSWER
    """
    def updateBestAnswer(self, answer):
        i = 0
        while self.individuals[i].sumOfList() == 0:
  #          if
            i += 1


    """
    SUM UP
    """
    def main(self):
        """
        STEP 1 TO BE DONE
        """




class Individual(Population):
    def __init__(self, geneticCode, initialList):
        """
        geneticCode is a list of 0 and 1 linked to a specific list :
        - if there is a 0 at position i, this means that the number list[i] is not in the individual
        - if there is a 1 at position i, this means that the number list[i] is in the individual
        fitness is a number that evaluate if an individual is, or is almost an answer. The nearer to 0, the better. If equal to 0, then the sum of the extracted list associated to the individual is 0.
        """
        self.geneticCode = geneticCode
        Population.initialList = initialList
        self.fitness = 0