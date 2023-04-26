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

mutation_list =["single_bit_flip","complete_bit_flip", 
                "single_swap_mutation", "multiple_bit_flip_mutation", 
                "cycle_mutation", "scramble_mutation" ]


bit_flips = 2 #mult_single_mutation
mutation_prob = 20
mutation_cycles = 100 # Cycle Mutation


def mutation (
crossed_population,
mutation_prob, 
bit_flips, #mult_single_mutation
mutation_cycles, 
mutation_type = "single_bit_flip"):

    if mutation_type =="single_bit_flip":
    #Single Bit Flip Mutation
        mutation_pop = crossed_population.copy()
        for key in mutation_pop:
            if np.random.randint(100, size=1)[0] < mutation_prob: 
                mutation_point = np.random.randint((len(mutation_pop[key])), size=1)[0]
                if mutation_pop[key][mutation_point] == 1: 
                    mutation_pop[key][mutation_point] = 0
                elif mutation_pop[key][mutation_point] == 0:
                    mutation_pop[key][mutation_point] = 1
        return mutation_pop


#Complete Bit Flip Mutation
    elif mutation_type =="complete_bit_flip":
        mutation_pop = crossed_population.copy()
        for key in mutation_pop:
            if np.random.randint(100, size=1)[0] < mutation_prob: 
                for value in mutation_pop[key]:
                    if mutation_pop[key][value] == 1: 
                        mutation_pop[key][value] = 0
                    elif mutation_pop[key][value] == 0:
                        mutation_pop[key][value] = 1
        return mutation_pop


#Swap Mutation (Single Bit)
    elif mutation_type =="single_swap_mutation":

        mutation_pop = crossed_population.copy()
        for key in mutation_pop:
            if np.random.randint(100, size=1)[0] < mutation_prob: 
                p1=np.random.randint((len(mutation_pop[key])), size=1)[0]
                p2=np.random.randint((len(mutation_pop[key])), size=1)[0]
                value_1 = mutation_pop[key][p1]
                value_2 = mutation_pop[key][p2]
                mutation_pop[key][p1] = value_2
                mutation_pop[key][p2] = value_1
        return mutation_pop


#Multiple Bit Flip Mutation
    elif mutation_type =="multiple_bit_flip_mutation":

        mutation_pop = crossed_population.copy()
        for key in mutation_pop:
            if np.random.randint(100, size=1)[0] < mutation_prob: 
                bit_flips = 2 #np.random.randint(len(mutation_pop[key]), size=1)[0]
                for flips in range(1,bit_flips):
                    mutation_point = np.random.randint((len(mutation_pop[key])), size=1)[0]
                    if mutation_pop[key][mutation_point] == 1: 
                        mutation_pop[key][mutation_point] = 0
                    elif mutation_pop[key][mutation_point] == 0:
                        mutation_pop[key][mutation_point] = 1
        return mutation_pop


# Cycle mutation (free)

    elif mutation_type =="cycle_mutation":
        mutation_pop = crossed_population.copy()
        for i in range(mutation_cycles):
            for key in mutation_pop:
                if np.random.randint(100, size=1)[0] < mutation_prob: 
                    mutation_point = np.random.randint((len(mutation_pop[key])), size=1)[0]
                    if mutation_pop[key][mutation_point] == 1: 
                        mutation_pop[key][mutation_point] = 0
                    else: 
                        mutation_pop[key][mutation_point] = 1
        return mutation_pop

#Scramble Mutation 
    elif mutation_type =="scramble_mutation":
        mutation_pop = crossed_population.copy()
        if np.random.randint(100, size=1)[0] < mutation_prob: 

            for key in mutation_pop:
                split_point_1=np.random.randint((len(mutation_pop[key])), size=1)[0]
                split_point_2=np.random.randint(low= int(split_point_1), high=len(mutation_pop[key]), size=1)[0]
                sublist = np.random.permutation(mutation_pop[key][split_point_1:split_point_2])
                mutation_pop[key][split_point_1:split_point_2] = sublist
        return mutation_pop
    

mutation (
crossed_population,
mutation_prob, 
bit_flips, #mult_single_mutation
mutation_cycles, 
mutation_type = "single_bit_flip")











