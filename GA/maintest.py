# -*- coding: utf-8 -*-


import unittest
from main import Population
from main import Individual

class KnownValues(unittest.TestCase):
    
    def testsum_of_list(self):
        randomList = Population([-12, 0, 0, 1, 13, 2, 3])
        randomIndividual1 = Individual([1, 0, 1, 1, 1, 0, 0], randomList.INITIAL_LIST)
        randomIndividual2 = Individual([1, 1, 1, 0, 0, 0, 1], randomList.INITIAL_LIST)
        randomIndividual3 = Individual([0, 0, 0, 0, 0, 0, 0], randomList.INITIAL_LIST)
        self.assertEqual(randomList.sum_of_list(randomIndividual1), 2)
        self.assertEqual(randomList.sum_of_list(randomIndividual2), 9)
        self.assertEqual(randomList.sum_of_list(randomIndividual3), 0)
        
    def testlen_of_individual(self):
        randomList = Population([0, 0, 0, 0, 0, 0, 0])
        randomIndividual1 = Individual([1, 1, 1, 1, 1, 1, 1], randomList.INITIAL_LIST)
        randomIndividual2 = Individual([1, 1, 1, 0, 0, 0, 1], randomList.INITIAL_LIST)
        randomIndividual3 = Individual([0, 0, 0, 0, 0, 0, 0], randomList.INITIAL_LIST)
        randomIndividual4 = Individual([1, 0, 1, 0, 1, 0, 1], randomList.INITIAL_LIST)
        self.assertEqual(randomList.len_of_individual(randomIndividual1), 7)
        self.assertEqual(randomList.len_of_individual(randomIndividual2), 4)
        self.assertEqual(randomList.len_of_individual(randomIndividual3), 0)
        self.assertEqual(randomList.len_of_individual(randomIndividual4), 4)
        
    def testcrossover_individuals(self):
        randomList = Population([0, 0, 0, 0, 0, 0, 0])
        randomParent1 = Individual([1, 0, 1, 1, 1, 0, 0], randomList.INITIAL_LIST)
        randomParent2 = Individual([1, 1, 1, 0, 0, 0, 1], randomList.INITIAL_LIST)
        randomParent3 = Individual([0, 0, 0, 0, 0, 0, 0], randomList.INITIAL_LIST)
        randomCrossoverPoint1 = 3
        randomCrossoverPoint2 = 0
        self.assertEqual(randomList.crossover_individuals(randomParent1, randomParent2, randomCrossoverPoint1).genetic_code, [1,0,1,0,0,0,1])
        self.assertEqual(randomList.crossover_individuals(randomParent2, randomParent1, randomCrossoverPoint1).genetic_code, [1,1,1,1,1,0,0])
        self.assertEqual(randomList.crossover_individuals(randomParent1, randomParent2, randomCrossoverPoint2).genetic_code, [1,1,1,0,0,0,1])
        self.assertEqual(randomList.crossover_individuals(randomParent2, randomParent1, randomCrossoverPoint2).genetic_code, [1,0,1,1,1,0,0])
        self.assertEqual(randomList.crossover_individuals(randomParent3, randomParent3, randomCrossoverPoint1).genetic_code, [0,0,0,0,0,0,0])
        self.assertEqual(randomList.crossover_individuals(randomParent3, randomParent3, randomCrossoverPoint2).genetic_code, [0,0,0,0,0,0,0])
        self.assertEqual(randomList.crossover_individuals(randomParent1, randomParent3, randomCrossoverPoint1).genetic_code, [1,0,1,0,0,0,0])
        self.assertEqual(randomList.crossover_individuals(randomParent3, randomParent1, randomCrossoverPoint1).genetic_code, [0,0,0,1,1,0,0])
        
    def testsort_individuals_by_fitness(self):
        randomList = Population([-12, 0, 0, 1, 11, 2, 3])
        randomIndividual1 = Individual([1, 0, 1, 0, 0, 1, 0], randomList.INITIAL_LIST)
        randomIndividual2 = Individual([1, 1, 1, 0, 0, 0, 1], randomList.INITIAL_LIST)
        randomIndividual3 = Individual([1, 0, 0, 1, 1, 0, 0], randomList.INITIAL_LIST)
        sortedList = [randomIndividual3, randomIndividual2, randomIndividual1]
        randomList.set_fitness_for_all_individuals([randomIndividual1, randomIndividual2, randomIndividual3])
        self.assertEqual(randomList.sort_individuals_by_fitness([randomIndividual1, randomIndividual2, randomIndividual3]), sortedList)

        
        
        

if __name__ == '__main__':
    unittest.main()