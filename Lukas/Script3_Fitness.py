from Script1_Data import nutrients, commodities, columns
import numpy as np

def monetary_fitness(population, commodities):
    '''
    This function calculates the fitness of individuals.
    In the stiger diet problem, the fitness is the sum of the food values.
    '''
    price_list = np.array([i[1] for i in list(commodities.values())])
    fitness = [np.dot(population[i], price_list) for i in population]
    return fitness