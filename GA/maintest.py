# -*- coding: utf-8 -*-


import unittest
from mainf import Population
from mainf import Individual

class KnownValues(unittest.TestCase):
    
    def testSumOfList(self):
        randomList = Population([-12, 0, 0, 1, 13, 2, 3])
        randomIndividual1 = Individual([1, 0, 1, 1, 1, 0, 0], randomList.initialList)
        randomIndividual2 = Individual([1, 1, 1, 0, 0, 0, 1], randomList.initialList)
        randomIndividual3 = Individual([0, 0, 0, 0, 0, 0, 0], randomList.initialList)
        self.assertEqual(randomList.sumOfList(randomIndividual1), 2)
        self.assertEqual(randomList.sumOfList(randomIndividual2), 9)
        self.assertEqual(randomList.sumOfList(randomIndividual3), 0)
        
    def testLenOfIndividual(self):
        randomList = Population([0, 0, 0, 0, 0, 0, 0])
        randomIndividual1 = Individual([1, 1, 1, 1, 1, 1, 1], randomList.initialList)
        randomIndividual2 = Individual([1, 1, 1, 0, 0, 0, 1], randomList.initialList)
        randomIndividual3 = Individual([0, 0, 0, 0, 0, 0, 0], randomList.initialList)
        randomIndividual4 = Individual([1, 0, 1, 0, 1, 0, 1], randomList.initialList)
        self.assertEqual(randomList.lenOfIndividual(randomIndividual1), 7)
        self.assertEqual(randomList.lenOfIndividual(randomIndividual2), 4)
        self.assertEqual(randomList.lenOfIndividual(randomIndividual3), 0)
        self.assertEqual(randomList.lenOfIndividual(randomIndividual4), 4)
        
    def testCrossoverIndividuals(self):
        randomList = Population([0, 0, 0, 0, 0, 0, 0])
        randomParent1 = Individual([1, 0, 1, 1, 1, 0, 0], randomList.initialList)
        randomParent2 = Individual([1, 1, 1, 0, 0, 0, 1], randomList.initialList)
        randomParent3 = Individual([0, 0, 0, 0, 0, 0, 0], randomList.initialList)
        randomCrossoverPoint1 = 3
        randomCrossoverPoint2 = 0
        self.assertEqual(randomList.crossoverIndividuals(randomParent1, randomParent2, randomCrossoverPoint1).geneticCode, [1,0,1,0,0,0,1])
        self.assertEqual(randomList.crossoverIndividuals(randomParent2, randomParent1, randomCrossoverPoint1).geneticCode, [1,1,1,1,1,0,0])
        self.assertEqual(randomList.crossoverIndividuals(randomParent1, randomParent2, randomCrossoverPoint2).geneticCode, [1,1,1,0,0,0,1])
        self.assertEqual(randomList.crossoverIndividuals(randomParent2, randomParent1, randomCrossoverPoint2).geneticCode, [1,0,1,1,1,0,0])
        self.assertEqual(randomList.crossoverIndividuals(randomParent3, randomParent3, randomCrossoverPoint1).geneticCode, [0,0,0,0,0,0,0])
        self.assertEqual(randomList.crossoverIndividuals(randomParent3, randomParent3, randomCrossoverPoint2).geneticCode, [0,0,0,0,0,0,0])
        self.assertEqual(randomList.crossoverIndividuals(randomParent1, randomParent3, randomCrossoverPoint1).geneticCode, [1,0,1,0,0,0,0])
        self.assertEqual(randomList.crossoverIndividuals(randomParent3, randomParent1, randomCrossoverPoint1).geneticCode, [0,0,0,1,1,0,0])
        
    def testSortIndividualsByFitness(self):
        randomList = Population([-12, 0, 0, 1, 11, 2, 3])
        randomIndividual1 = Individual([1, 0, 1, 0, 0, 1, 0], randomList.initialList)
        randomIndividual2 = Individual([1, 1, 1, 0, 0, 0, 1], randomList.initialList)
        randomIndividual3 = Individual([1, 0, 0, 1, 1, 0, 0], randomList.initialList)
        sortedList = [randomIndividual3, randomIndividual2, randomIndividual1]
        randomList.setFitnessForAllIndividuals([randomIndividual1, randomIndividual2, randomIndividual3])
        self.assertEqual(randomList.sortIndividualsByFitness([randomIndividual1, randomIndividual2, randomIndividual3]), sortedList)

        
        
        

if __name__ == '__main__':
    unittest.main()