# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import matplotlib.pyplot as plt

class Population:
    def __init__(self, INITIAL_LIST):
        """
        individuals is a list of individual objects
        INITIAL_LIST is the list of relative numbers given at the beginning
        """
        self.INITIAL_LIST = INITIAL_LIST
        self.NB_OF_INDIVIDUALS = 100
        self.L = len(INITIAL_LIST)
        self.individuals = 0 # useless to put It here since It will be defined with generateIndividuals method, but we want to keep a list of all the attributes of Population class
        self.NB_OF_GENERATIONS = 50


    """
    BASIC METHODS
    """

    def generate_individuals(self):
        res = []
        for i in range(self.NB_OF_INDIVIDUALS):
            temp = []
            for j in range(self.L):
                temp += [rd.randint(0,1)]
            res += [Individual(temp, self.INITIAL_LIST)]
        self.individuals = res

    def generate_specific_number_of_individuals(self, NB_OF_INDIVIDUALS):
        res = []
        for i in range(NB_OF_INDIVIDUALS):
            temp = []
            for j in range(self.L):
                temp += [rd.randint(0,1)]
            res += [Individual(temp, self.INITIAL_LIST)]
        self.set_fitness_for_all_individuals(res)
        return res

    def set_fitness_for_one_individual(self, individual):
        individual.fitness = self.evaluate_fitness(individual)

    def set_fitness_for_all_individuals(self, many_individuals):
        for i in range(len(many_individuals)):
            self.set_fitness_for_one_individual(many_individuals[i])

    def sum_of_list(self, individual):
        return np.abs(np.dot(self.INITIAL_LIST, individual.genetic_code))

    def len_of_individual(self, individual):
        return np.dot(np.ones(self.L), individual.genetic_code)


    """
    /!\ IMPORTANT /!\
        
    Choose one fitness function among the following two
        - first fitness function comes with first update_answer in section 5
        - second fitness function comes with second update_answer in section 5
    """
    
    
    def evaluate_fitness(self, individual):
        return np.abs(np.dot(self.INITIAL_LIST, individual.genetic_code))
    
    
    """
    def evaluate_fitness(self, individual):
        return np.abs(np.dot(self.INITIAL_LIST, individual.genetic_code)) + (1 - self.len_of_individual(individual)/self.L)
    """



    """
    STEP 1:
    Tournament
    
    Uncomment the wanted method
    """


    """
        Option 1 : random selection
        """
    
    
    def select_two_individuals(self):
        return [self.individuals[rd.randint(0,self.NB_OF_INDIVIDUALS - 1)] for i in range(2)]
    
    
    """
        Option 2 : selection with tournament
        """
    """ 
    def select_two_individuals(self):
        selected_individuals = rd.sample(self.individuals, round(0.1*self.NB_OF_INDIVIDUALS))
        final_two_individuals = []
        for step in range(2):
            length = len(selected_individuals)
            list_of_fitness = [selected_individuals[i].fitness for i in range(length)] + np.ones(length)/100000
            weights = [100/(list_of_fitness[i]*sum(1/list_of_fitness)) for i in range(length)]
            index = 0
            pick_a_number = rd.random()
            while ((pick_a_number - weights[index]/100) > 0):
                pick_a_number -= weights[index]/100
                index+=1
            final_two_individuals += [selected_individuals[index]]
            del selected_individuals[index]
        return final_two_individuals
    """
    



    """
    STEP 2 :
    Crossovers
    """

    def crossover_individuals(self, first_individual, second_individual, crossover_point):
        a = first_individual.genetic_code
        b = second_individual.genetic_code
        return Individual(a[:crossover_point] + b[crossover_point:], self.INITIAL_LIST)


    def crossover_of_selected_individuals(self, individuals_to_cross):
        individual_1 = individuals_to_cross[0]
        individual_2 = individuals_to_cross[1]
        crossover_point = rd.randint(0,self.L - 1)
        new_individual_1 = self.crossover_individuals(individual_1, individual_2, crossover_point)
        new_individual_2 = self.crossover_individuals(individual_2, individual_1, crossover_point)
        return [new_individual_1, new_individual_2]


    """
    STEP 3 :
    Mutations

    """

    def mutate_individuals(self, individual):
        for i in range(self.L):
            if rd.randint(0,self.L - 1) == 0:
                individual.genetic_code[i] = -individual.genetic_code[i] + 1


    """
    STEP 4 :
    Extras
    
    Uncomment the wanted method
    """


    def sort_individuals_by_fitness(self, many_individuals):
        return sorted(many_individuals, key = lambda x: x.fitness)
    
    """
        Option 1 : without elitism
        """
    
    def create_new_population(self, new_individuals):
        PERCENTAGE_OF_NEW_INDIVIDUALS = 0.8
        number_of_new_individuals = round(PERCENTAGE_OF_NEW_INDIVIDUALS * self.NB_OF_INDIVIDUALS)
        number_of_extras = self.NB_OF_INDIVIDUALS - number_of_new_individuals
        new_individuals = self.sort_individuals_by_fitness(new_individuals)[:number_of_new_individuals]
        extras = self.generate_specific_number_of_individuals(number_of_extras)
        self.individuals = self.sort_individuals_by_fitness(new_individuals + extras)
    
    
    
    """
        Option 2 : with elitism
        """ 
        
    """
    def create_new_population(self, new_individuals):
        PERCENTAGE_OF_NEW_INDIVIDUALS = 0.6
        PERCENTAGE_OF_EXTRAS = 0.2
        number_of_new_individuals = round(PERCENTAGE_OF_NEW_INDIVIDUALS * self.NB_OF_INDIVIDUALS)
        number_of_extras = round(PERCENTAGE_OF_EXTRAS * self.NB_OF_INDIVIDUALS)
        number_of_old_individuals = self.NB_OF_INDIVIDUALS - number_of_new_individuals - number_of_extras
        new_individuals = self.sort_individuals_by_fitness(new_individuals)[:number_of_new_individuals]
        extras = self.generate_specific_number_of_individuals(number_of_extras)
        old_individuals = self.individuals[:number_of_old_individuals]
        self.individuals = self.sort_individuals_by_fitness(old_individuals + new_individuals + extras)
    """
    



    """
    STEP 5 :
    UPDATE THE BEST ANSWER
    """
    
    """
    /!\ IMPORTANT /!\
        
    Choose one update_function among the following two
        - first update function comes with first evaluate_fitness in introduction
        - second update function comes with second evaluate_fitness in introduction
    """
    
    """
    Since the first fitness function does not necessarily consider the lenght of the list, we need to consider It there.
    self.individuals here is sorted by fitness to make considering the lenght of each individuals faster.
    We define a best possible answer as the individual with the best fitness first, and then sum nearer to 0 and finally the longest lenght.
    """
    
    
    def update_answer(self, answer):
        i = 0
        while (self.individuals[i].fitness <= answer.fitness) & (i < self.NB_OF_INDIVIDUALS):
            if (self.sum_of_list(answer) != 0) or (self.sum_of_list(answer) == 0 and self.len_of_individual(self.individuals[i]) >= self.len_of_individual(answer)):
                answer = self.individuals[i]
            i += 1
        return answer
    
    
    """
    def update_answer(self, answer):
        if self.individuals[0].fitness < answer.fitness:
            answer = self.individuals[0]
        return answer
    """
    


    """
    SUM UP
    """
    def main(self):
        self.generate_individuals()
        self.set_fitness_for_all_individuals(self.individuals)
        self.individuals = self.sort_individuals_by_fitness(self.individuals)
        answer = self.individuals[0]
        fitness_list = [answer.fitness]
        actual_fitness_list = [answer.fitness]
        len_list = [self.len_of_individual(answer)]
        abs = [i for i in range(self.NB_OF_GENERATIONS + 1)]
        for i in range(self.NB_OF_GENERATIONS):
            tournament_selected_individuals = []
            for j in range(self.NB_OF_INDIVIDUALS // 2):
                tournament_selected_individuals += self.crossover_of_selected_individuals(self.select_two_individuals())
            for individual in tournament_selected_individuals:
                self.mutate_individuals(individual)
            self.set_fitness_for_all_individuals(tournament_selected_individuals)
            self.create_new_population(tournament_selected_individuals)
            answer = self.update_answer(answer)
            fitness_list += [answer.fitness]
            actual_fitness_list += [self.individuals[0].fitness]
            len_list += [self.len_of_individual(answer)]
            
            
            
        """
        Plot this way if you have chosen not to take elitism
        It will plot the fitness of the best member of each generation as well
        as the overall best fitness
        """
        """
        plt.plot(abs,fitness_list, color='tab:red')
        plt.plot(abs,actual_fitness_list, color='tab:blue')
        plt.show()
        return answer
        """
        
        
        
        """
        This plot works in any case
        It will plot the length of the best solution as well as its fitness
        """
        """
        fig, ax1 = plt.subplots()
        ax1.plot(abs,fitness_list, color='tab:red')
        ax2 = ax1.twinx()
        ax2.plot(abs,len_list, color='tab:blue')
        plt.show()
        """



class Individual(Population):

    def __init__(self, genetic_code, INITIAL_LIST):
        """
        genetic_code is a list of 0 and 1 linked to a specific list :
        - if there is a 0 at position i, this means that the number list[i] is not in the individual
        - if there is a 1 at position i, this means that the number list[i] is in the individual
        fitness is a number that evaluate if an individual is, or is almost an answer. The nearer to 0, the better. If equal to 0, then the sum of the extracted list associated to the individual is 0.
        """
        self.genetic_code = genetic_code
        Population.INITIAL_LIST = INITIAL_LIST
        self.fitness = 0