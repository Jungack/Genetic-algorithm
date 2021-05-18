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
        
    def sort_individuals_by_fitness(self):
        sorted(self.individuals, key = lambda x: x.fitness)
        

    def select_individuals(self):
        self.individuals = [Individual(individuals[i], 0) for ]
    

    def crossover_individuals(self, otherIndividual, crossoverPoint):
        a = self.geneticCode
        b = self.crossoverPoint

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
        
    def evaluate_fitness(self):
        return np.abs(np.dot(initialList, geneticCode))        
        
        self.fitness = evaluate_fitness()
        
        
    def len_of_individual(self, individual):
        return np.dot(np.ones(len(initialList)), individual)



