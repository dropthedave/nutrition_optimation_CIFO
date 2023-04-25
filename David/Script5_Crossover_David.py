from Script1_Data import nutrients, commodities
from Script2_InitialPopulation_David import Initial_Population
from Script3_Fitness_David import fitness
from Script4_SelectionProcess_David import parents
import numpy as np


def crossover(Initial_Population, parents):
    crossed_population = {}
    for i in range(len(parents)-1):
        #Define the first two parents
        parent_1, parent_2 =Initial_Population[parents[i]], Initial_Population[parents[i+1]]

        #Define a split point
        split_point=np.random.randint((len(parent_1)), size=1)[0]-1

        #Split the two parents...
        p1_1, p1_2 = parent_1[split_point:], parent_1[:split_point]
        p2_1, p2_2 = parent_2[split_point:], parent_2[:split_point]

        #....and put them back together
        child_1 = np.concatenate((p1_1, p2_2))
        child_2 = np.concatenate((p2_1, p1_2))
        crossed_population[i] = child_1
        crossed_population[i+1] = child_2
    return crossed_population
    
crossed_population = crossover(Initial_Population, parents)


### Mutation

mutation_cycles = 100
mutation_prob = 20

def mutation(crossed_population, mutation_cycles, mutation_prob):
    mutation_pop = crossed_population.copy()
    for i in range(mutation_cycles):
        for key in mutation_pop:
            #print("cycle", i, "individual", key)
            if np.random.randint(100, size=1)[0] < mutation_prob: 
                mutation_point = np.random.randint((len(mutation_pop[key])), size=1)[0]
                if mutation_pop[key][mutation_point] == 1: 
                    mutation_pop[key][mutation_point] = 0
                else: 
                    mutation_pop[key][mutation_point] = 1
    return mutation_pop
mutation_pop=mutation(crossed_population, mutation_cycles, mutation_prob)











