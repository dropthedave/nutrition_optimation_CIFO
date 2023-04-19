from Script1_Data import nutrients, commodities
import random
import numpy as np

def random_population(population_size, nutrients=nutrients, commodities=commodities):
    '''
    This function generates random individuals for the population of size "population_size"
    Output: N (population_size) individuals with the quantity per item to satisfy the constraints
    '''
    # create list with constraints
    constraints = np.array(list(nutrients.values()))
    # create list for population
    population = []
    # repeat for each individual in the population
    for i in range(population_size):
        # create list for tracking nutrients
        cumulative_list = np.zeros(constraints.size)
        # create list for tracking items
        individual = np.zeros(len(commodities))
        # repeat till constraints/nutrients are met
        while not np.all((constraints - cumulative_list)<=0):
            # randomly select a item from the dictionary
            key = np.random.choice(list(commodities.keys()))
            # add the value array to the cumulative list
            cumulative_list += np.array(commodities[key][2:])
            # update the one-hot encoded array to indicate the selected key
            individual[list(commodities.keys()).index(key)] += 1
        # add the individual to the population
        population.append(individual)
    return population


###############
# Test Function
###############
# from Script3_Fitness import monetary_fitness
# set population size
# population_size = 10
# generate random population of size 10
# pop = random_population(population_size, nutrients, commodities)
# print population
# print(pop)
# print monetary fitness of the population
# print(monetary_fitness(pop, commodities))