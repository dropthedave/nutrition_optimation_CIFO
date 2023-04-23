from Script1_Data import nutrients, commodities
from Script3_Fitness import monetary_fitness
from Script4_SelectionProcess import roulette
import random
import numpy as np

def initial_population(population_size, nutrients=nutrients, commodities=commodities):
    '''
    This function generates random individuals (solutions) for the population of size "population_size"
    '''
    # create empty numpy array for population
    population = np.empty((0,len(commodities)))

    # create n solutions (n = population_size)
    for i in range(population_size):
        # generate random solution
        solution = np.random.randint(0, 2, size=(1,len(commodities)))
        # add solution to population
        population = np.append(population, solution, axis=0)
    
    return population



######
# Test
######

# pop = initial_population(10)
# print(roulette(pop, nutrients, commodities))