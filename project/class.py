# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import math

class Population:
    def __init__(self, initialList):
        """
        individuals is a list of individual objects
        initialList is the list of relative numbers given at the beginning
        """
        self.initialList = initialList
        self.nbOfIndividuals = 100
        self.l = len(initialList)
        self.individuals = 0 # useless to put It here since It will be defined with generateIndividuals method, but we want to keep a list of all the attributes of Population class
        self.nbOfGenerations = 5000



    """
    BASIC METHODS
    """

    def generateIndividuals(self):
        res = []
        for i in range(self.nbOfIndividuals):
            temp = []
            for j in range(self.l):
                temp += [rd.randint(0,1)]
            res += [Individual(temp, self.initialList)]
        self.individuals = res

    def evaluateFitness(self, individual):
        return np.abs(np.dot(self.initialList, individual.geneticCode)) +10*(1-self.lenOfIndividual(individual)/self.l)

    def setFitnessForOneIndividual(self, individual):
        individual.fitness = self.evaluateFitness(individual)

    def setFitnessForAllIndividuals(self, manyIndividuals):
        for i in range(len(manyIndividuals)):
            self.setFitnessForOneIndividual(manyIndividuals[i])

    def sumOfList(self, individual):
        return np.abs(np.dot(self.initialList, individual.geneticCode))

    def lenOfIndividual(self, individual):
        return np.dot(np.ones(self.l), individual.geneticCode)

    """
    def evaluateFitness(self, individual):
        return np.abs(np.dot(self.initialList, individual.geneticCode))
    """

    def evaluateFitness(self, individual):
        return np.abs(np.dot(self.initialList, individual.geneticCode)) / self.lenOfIndividual(individual)



    """
    STEP 1:
    Tournament
    """

    def selectTwoIndividualsByTournament(self):
        selected_individuals = rd.sample(self.individuals, 10)
        finalTwoIndividuals = []
        for step in range(2):
            length = len(selected_individuals)
            listOfFitness = [selected_individuals[i].fitness for i in range(length)] + np.ones(length)/100000
            weights = [100/(listOfFitness[i]*sum(1/listOfFitness)) for i in range(length)]
            index = 0
            pickANumber = rd.random()
            while ((pickANumber - weights[index]/100) > 0):
                pickANumber -= weights[index]/100
                index+=1
            finalTwoIndividuals += [selected_individuals[index]]
            del selected_individuals[index]
        return finalTwoIndividuals


    """
    STEP 2 :
    Crossovers
    """

    def crossoverIndividuals(self, firstIndividual, otherIndividual, crossoverPoint):
        a = firstIndividual.geneticCode
        b = otherIndividual.geneticCode
        return Individual(a[:crossoverPoint] + b[crossoverPoint:], self.initialList)


    def crossoverOfSelectedIndividuals(self, individualsToCross):
        individual1 = individualsToCross[0]
        individual2 = individualsToCross[1]
        newIndividual1 = self.crossoverIndividuals(individual1, individual2, rd.randint(0,self.l))
        newIndividual2 = self.crossoverIndividuals(individual2, individual1, rd.randint(0,self.l))
        return [newIndividual1, newIndividual2]


    """
    STEP 3 :
    Mutations
    """

    def mutateIndividuals(self, individual):
        for i in range(self.l):
            if rd.randint(0,self.l - 1) == 0:
                individual.geneticCode[i] = -individual.geneticCode[i] + 1


    """
    STEP 4 :
    Elitism
    """

    def sortIndividualsByFitness(self, manyIndividuals):
        return sorted(manyIndividuals, key = lambda x: x.fitness)

    def createNewPopulationWithElitism(self, newIndividuals):
        pourcentageOfNewIndividuals = 0.9
        numberOfNewIndividuals = round(pourcentageOfNewIndividuals * self.nbOfIndividuals)
        numberOfOldIndividuals = self.nbOfIndividuals - numberOfNewIndividuals
        newIndividuals = self.sortIndividualsByFitness(newIndividuals)[:numberOfNewIndividuals]
        oldIndividuals = self.individuals[:numberOfOldIndividuals] # The individuals here will already be sorted
        self.individuals = self.sortIndividualsByFitness(oldIndividuals + newIndividuals)


    """
    STEP 5 :
    UPDATE THE BEST ANSWER
    """
    def updateBestAnswer(self, answer):
        """
        By definition, the fitness is 0 when the sum of the sublist linked to an individual is 0. Since the fitness function does not necesarry consider the lenght of the list, we need to consider It there, only for the individuals with a sum of 0.
        self.individuals here is sorted by fitness to make considering the lenght of each individuals faster.
        We define a best possible answer as the individual with the best fitness AND the longest lenght.
        """
        if self.individuals[0].fitness < answer.fitness:
            answer = self.individuals[0]
        return answer


    """
    SUM UP
    """
    def main(self):
        self.generateIndividuals()
        self.setFitnessForAllIndividuals(self.individuals)
        self.individuals = self.sortIndividualsByFitness(self.individuals)
        answer = self.individuals[0]
        for i in range(self.nbOfGenerations):
            tournamentSelectedIndividuals = []
            for j in range(self.nbOfIndividuals // 2):
                tournamentSelectedIndividuals += self.crossoverOfSelectedIndividuals(self.selectTwoIndividualsByTournament())
            for individual in tournamentSelectedIndividuals:
                self.mutateIndividuals(individual)
            self.setFitnessForAllIndividuals(tournamentSelectedIndividuals)
            self.createNewPopulationWithElitism(tournamentSelectedIndividuals)
            self.updateBestAnswer(answer)
            print(self.sumOfList(answer))
            print(self.lenOfIndividual((answer)))
            answer = self.updateBestAnswer(answer)
        print(answer.geneticCode)
        return answer





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