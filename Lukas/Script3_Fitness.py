from Script1_Data import nutrients, commodities
import numpy as np

def monetary_fitness(population, commodities):
    '''
    This function calculates the fitness of individuals.
    In the stiger diet problem, the fitness is the sum of the food values.
    '''
    # create list with prices
    price_list = np.array([i[1] for i in list(commodities.values())])
    # calculate price for each individual via dot product
    # DISCLAIMER: fitness is in Cents not Dollars
    fitness = [np.dot(np.array(population[i]), price_list) for i in range(len(population))]
    return fitness