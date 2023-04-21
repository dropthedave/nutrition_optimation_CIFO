from individual import Individual
from population import Population
from data import nutrients, commodities
# from selection import fps
# from variation import single_point_xo
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
    # create matrix with commodities
    commodities_matrix = np.array(list(commodities.values()))
    commodities_of_individual = self.representation.dot(commodities_matrix)
    
    # create constraints list
    constraints = np.array(list(nutrients.values()))
    check = constraints <= commodities_of_individual[1:] # min constraints only here

    # initial fitness based on costs
    fitness = commodities_of_individual[0]

    # increase fitness for every broken constraint
    for i in range(len(constraints)):
        if check[i] == False:
            fitness += 10 # arbitrary fix value rn 

    return fitness


# Monkey Patching
Individual.get_fitness = get_fitness





# initialize pop
pop = Population(size=20, optim="min", sol_size=len(commodities), valid_set=list(range(6)), replacement=True)


# 100 generations
# for i in range(100): # our termination condition
#     new_gen = []
#     while len(new_gen) < len(pop):
#         # select
#         parent1, parent2 = fps(pop), fps(pop)
#         # crossover
#         xo_prob = 0.8
#         if random() < xo_prob:
#             offspring1, offspring2 = single_point_xo(parent1, parent2)
#         else: # replication
#             offspring1 = parent1
#             offspring2 = parent2
#         #mutation
#         mut_prob = 0.1
#         if random() < mut_prob:
#             offspring1 = binary_mutation(offspring1)
#         if random() < mut_prob:
#             offspring2 = binary_mutation(offspring2)

#         new_gen.append(Individual(offspring1))
#         new_gen.append(Individual(offspring2))
#     pop.individuals = new_gen
#     print(f'Best Individual: {max(pop, key=attrgetter("fitness"))}') # take best population wrt. attribut 'fitness'
