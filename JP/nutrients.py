from individual import Individual
from population import Population
from data import nutrients, commodities
from selection import roulette, ranked, tournament
from variation import single_point_xo, add_one_mutation
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


def genetic_algorithm(select=None,
                      k=None,
                      crossover=None,
                      mutate=None,
                      gens= 500, 
                      pop_size=50, 
                      opt="min", 
                      val_set=list(range(4)), 
                      mut_prob= 0.02,
):
    # initialize pop
    pop = Population(size=pop_size, optim=opt, sol_size=len(commodities), valid_set=val_set, replacement=True)
    for i in range(gens): # our termination condition
        new_gen = []
        while len(new_gen) < len(pop):
            # select
            if k is None:
                parent1, parent2 = select(pop), select(pop)
            else:
                parent1, parent2 = select(pop=pop, k=k), select(pop=pop, k=k)
            # crossover
            xo_prob = 0.8
            if random() < xo_prob:
                offspring1, offspring2 = crossover(parent1, parent2)
            else: # replication
                offspring1 = parent1
                offspring2 = parent2
            #mutation
            offspring1 = mutate(offspring1, mut_prob)
            offspring2 = mutate(offspring2, mut_prob)

            new_gen.append(Individual(offspring1))
            new_gen.append(Individual(offspring2))
        pop.individuals = new_gen
        print(f'Best Individual: {min(pop, key=attrgetter("fitness"))}') # take best individual wrt. attribut 'fitness'


if __name__ == "__main__":
    # Monkey Patching
    Individual.get_fitness = get_fitness
    
    genetic_algorithm(select=tournament,
                      k=30, # put None, if no tournament selection
                      crossover=single_point_xo,
                      mutate=add_one_mutation,
                      gens= 500, 
                      pop_size=50, 
                      opt="min", 
                      val_set=list(range(4)), 
                      mut_prob= 0.02,
)