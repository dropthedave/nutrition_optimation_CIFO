from individual import Individual
from population import Population
from data import nutrients, commodities
from selection import roulette, ranked, tournament
from variation import crossover, mutation
from copy import deepcopy
from random import random
from operator import attrgetter
import numpy as np 


def get_fitness(self):
    """A function to calculate the total costs if the constraints are fulfilled
    If a constraint is broken, it will return a negative fitness
    Returns:
        int: fitness 
    """
    # Create matrix with commodities
    commodities_matrix = np.array(list(commodities.values()))
    commodities_of_individual = self.representation.dot(commodities_matrix)
    
    # Create constraints list
    constraints = np.array(list(nutrients.values()))
    check = constraints <= commodities_of_individual[1:]                        # min constraints only here

    # Initial fitness based on costs
    fitness = commodities_of_individual[0]
    costs = fitness

    # Increase fitness for every broken constraint
    for i in range(len(constraints)):
        if check[i] == False:
            fitness += 10                                                       # arbitrary fix value rn 

    return fitness, costs, commodities_of_individual[1:]