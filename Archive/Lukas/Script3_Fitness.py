from Script1_Data import nutrients, commodities
import numpy as np

def monetary_fitness(population, nutrients=nutrients, commodities=commodities):
    '''
    This function calculates the fitness of individuals.
    In the diet problem, the fitness is the sum of the food values.
    '''
    # create list with prices
    price_list = np.array([i[0] for i in np.array(list(commodities.values()))])
    # create constraints list
    constraints =np.array(list(nutrients.values()))
    # create empty list for the fitness values
    fitness = np.array([])
    # calculate fitness for each solution
    for solution in population:
        cumulative_nutrients = np.zeros(len(nutrients.keys()))
        for index, i in enumerate(solution):
            if i == 1:
                cumulative_nutrients += np.array(list(commodities.values())[index][1:])
        # check if all constraints are met
        check = constraints - cumulative_nutrients
        if np.all(check <= 0):
            fitness = np.append(fitness, np.dot(solution, price_list))
        else:
            fitness = np.append(fitness, -1)

    return fitness