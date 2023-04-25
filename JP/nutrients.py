from individual import Individual
from population import Population
from data import nutrients, commodities
from selection import roulette, ranked, tournament
from variation import crossover, add_one_mutation
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
    costs = fitness
    # increase fitness for every broken constraint
    for i in range(len(constraints)):
        if check[i] == False:
            fitness += 10 # arbitrary fix value rn 

    return fitness, costs, commodities_of_individual[1:]


def genetic_algorithm(select=None,
                      k=None,
                      crossover=None,
                      mutate=None,
                      gens= 100, 
                      pop_size=100, 
                      opt="min", 
                      val_set=list(range(2)), 
                      mut_prob = 0.3,
                      xo_prob = 0.9,
                      xo_type = "one-point",
                      elite=0
):
    # initialize pop
    pop = Population(size=pop_size, optim=opt, sol_size=len(commodities), valid_set=val_set, replacement=True)
    if elite > pop_size:
        print("Number of elites is too high!")
        return False

    if elite % 2 == 1:
        if elite == 1: 
            elite == 2
        else:
            elite = elite - 1
        print("Odd elite paramter changed to", str(elite))
    for i in range(gens): # our termination condition
        new_gen = []
        if elite > 0:
            # sort the list of objects by fitness value in descending order
            sorted_objects = sorted(pop, key=lambda x: x.fitness, reverse=False)
            # append objects with the best fitness value
            for i in range(elite):
                new_gen.append(Individual(sorted_objects[i]))
                print("Add elite:", sorted_objects[i])
                
        while len(new_gen) < len(pop):
            # select
            if k is None:
                parent1, parent2 = select(pop), select(pop)
            else:
                parent1 = select(pop, k=k)
                parent2 = select(pop, k=k)
            # crossover
            if random() < xo_prob:
                offspring1, offspring2 = crossover(parent1, parent2, xo_type)
            else: # replication
                offspring1 = parent1
                offspring2 = parent2
            #mutation
            if random() < mut_prob: 
                offspring1 = mutate(offspring1, mut_prob)
            if random() < mut_prob:
                offspring2 = mutate(offspring2, mut_prob)

            new_gen.append(Individual(offspring1))
            new_gen.append(Individual(offspring2))
        pop.individuals = new_gen
        print(f'Best Individual: {min(pop, key=attrgetter("fitness"))}') # take best individual wrt. attribut 'fitness'
    print("Products:")
    commodity_keys = list(commodities.keys())
    for i, j in zip(min(pop, key=attrgetter("fitness")).representation, commodity_keys):
        if i == 1:
            print(j, commodities[j][0])
    print("Total values:")
    nutrient_keys = list(nutrients.keys())
    for i, j in zip(min(pop, key=attrgetter("fitness")).totals, nutrient_keys):
        print(j, i)


if __name__ == "__main__":
    # Monkey Patching
    Individual.get_fitness = get_fitness
    
    genetic_algorithm(select=tournament,
                      k=5, # put number, if no tournament selection, and string for k-point-crossover
                      crossover=crossover,
                      mutate=add_one_mutation,
                      gens= 50, 
                      pop_size=1000, 
                      opt="min", 
                      val_set=list(range(2)), 
                      mut_prob= 0.3,
                      xo_prob = 0.8,
                      xo_type = "uniform",
                      elite=2 # number of best individuals
)