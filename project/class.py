<<<<<<< HEAD
from numpy import * 
=======
class Individual:
    def __init__(self, geneticCode, fitness):
        """
        geneticCode is a list of 0 and 1 linked to a specific list :
        - if there is a 0 at position i, this means that the number list[i] is not in the individual
        - if there is a 1 at position i, this means that the number list[i] is in the individual
        """
        self.geneticCode = geneticCode
        self.fitness = fitness

    def evaluate_fitness(self):
        while True:
            print("Bonjour Florian")

    def select_individuals(self):
        while True:
            print("Bonjour Jacques")

    def crossover_individuals(self, otherIndividual, crossoverPoint):
        a = self.geneticCode
        b = self.crossoverPoint
        for i in range(crossoverPoint,len(a)):
            a.pop(-1)
        for i in range(0,crossoverPoint):
            b.pop(0)
        return a + b

    def mutate_individuals(self, otherIndividual):
        while True:
            print("Bonjour")
>>>>>>> ec945ddf85b6c7503e2590286bfa0604f411a3c4

class Population:
    def __init__(self, individuals, initialList):
        """
        individuals is a list of individual objects
        initialList is the list of relative numbers given at the beginning
        """
        self.individuals = individuals
        self.initialList = initialList


    def len_of_individual(self, individual):
        res = 0
        for i in range(len(self.initialList)):
            res += individual.geneticCode[i]
        return res

    def select_individuals(self):
        selected_individuals = []
        for individual in self.individuals:
            if sum_of_individual(individual) == 0:
                selected_individuals += [individual]
        return Population(selected_individuals, self.initialList)
    
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
        

    def select_individuals(self):
        while True:
            print("Bonjour")

    def crossover_individuals(self, otherIndividual):
        while True:
            print("Bonjour")

    def mutate_individuals(self, otherIndividual):
        while True:
            print("Bonjour")
