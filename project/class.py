from numpy import *
import random

class Population:
    def __init__(self, individuals, initialList):
        """
        individuals is a list of individual objects
        initialList is the list of relative numbers given at the beginning
        """
        self.individuals = individuals
        self.initialList = initialList

    def select_individuals(self):
        res = sorted(self.individuals, key = lambda x: x.fitness)
        return res

    def crossover_individuals(self, firstIndividual, otherIndividual, crossoverPoint):
        a = firstIndividual.geneticCode
        b = otherIndividual.geneticCode
        for i in range(crossoverPoint,len(a)):
            a.pop(-1)
        for i in range(0,crossoverPoint):
            b.pop(0)
        return a + b

    def mutate_individuals(self, individual):
        mutatePoint = random.randint(0,len(individual))
        individual[mutatePoint] = random.randint(0,2)
        return individual


class Individual(Population):
    def __init__(self, geneticCode, fitness):
        """
        geneticCode is a list of 0 and 1 linked to a specific list :
        - if there is a 0 at position i, this means that the number list[i] is not in the individual
        - if there is a 1 at position i, this means that the number list[i] is in the individual
        """
        self.geneticCode = geneticCode
        self.fitness = fitness

    def evaluate_fitness(self):
        return abs(vdot(initialList, geneticCode))

