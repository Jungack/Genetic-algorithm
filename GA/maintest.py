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
        
    def 
        
        

if __name__ == '__main__':
    unittest.main()