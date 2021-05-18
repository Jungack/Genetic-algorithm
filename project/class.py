import numpy as np
import random as rd

class Population:
    def __init__(self, individuals, initialList):
        """
        individuals is a list of individual objects
        initialList is the list of relative numbers given at the beginning
        """
        self.individuals = individuals
        self.initialList = initialList
        
    def generate_genetic_code()
        
    def sort_individuals_by_fitness(self):
        return sorted(self.individuals, key = lambda x: x.fitness)
    

    def select_two_individuals_by_tournament(self):
        selected_individuals = rd.choices(self.individuals, k = floor(0.1*len(initialList)))
        weights = [100/sum(selected_individuals[i].fitness/selected_individuals[j].fitness) for i in len(selected_individuals) for j in len(selected_individuals)]
        
            
    

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
        self.fitness = np.abs(np.dot(initialList, geneticCode))        
    
        
    def len_of_individual(self):
        return np.dot(np.ones(len(initialList)), self.geneticCode)



