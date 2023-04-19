from Script1_Data import nutrients, commodities, columns
import random
import numpy as np

#################
# Test Parameters
population_size = 5
#################

def random_population(population_size, nutrients, commodities):
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
        population.append(individual)
    return population

pop = random_population(population_size, nutrients, commodities)
print(pop)