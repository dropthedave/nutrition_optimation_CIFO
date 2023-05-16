from data import nutrients, commodities
import numpy as np
from random import randint, random, choice, sample
from individual import Individual

# def add_one_mutation(individual, mut_prob):
#     mut_index = choice(range(91))
#     #if random() < mut_prob:
#     if individual[mut_index] == 0:
#         individual[mut_index] = 1
#     elif individual[mut_index] == 1:
#         individual[mut_index] = 0
#     return individual



# def swap_mutation(population, commodities=commodities, mutation_rate=0.1):
#     # if np.random.random() < mutation_rate:
        
        
#     return


# def single_point_xo(p1, p2):
#     xo_point = randint(1, len(p1) - 1)
#     offspring1 = np.concatenate((p1[:xo_point],p2[xo_point:]))
#     offspring2 = np.concatenate((p2[:xo_point],p1[xo_point:]))
#     return offspring1, offspring2

def crossover(parent1, parent2, xo_type ='one-point'):
    parent1 = list(parent1)
    parent2 = list(parent2)
    
    if xo_type == 'uniform':
            offspring1 = [] 
            offspring2 = []
            for i in range(0, (len(parent1))):
                temp_list = []
                temp_list.append(parent1[i])
                temp_list.append(parent2[i])
                temp_array = np.array(temp_list)
                offspring1.append(np.random.choice(temp_array))
                offspring2.append(np.random.choice(temp_array))
    if xo_type == 'one-point':
        point = randint(1, len(parent1)-1)
        offspring1 = parent1[:point] + parent2[point:]
        offspring2 = parent2[:point] + parent1[point:]
    if xo_type == 'five-point':
        rl = np.array(sorted(sample(range(1, len(parent1)-1), 5)))
        offspring1 = parent1[:rl[0]] + parent2[rl[0]:rl[1]] + parent1[rl[1]:rl[2]] + parent2[rl[2]:rl[3]] + parent1[rl[3]:rl[4]] + parent2[rl[4]:]
        offspring2 = parent2[:rl[0]] + parent1[rl[0]:rl[1]] + parent2[rl[1]:rl[2]] + parent1[rl[2]:rl[3]] + parent2[rl[3]:rl[4]] + parent1[rl[4]:]
    if xo_type == 'ten-point':
        rl = np.array(sorted(sample(range(1, len(parent1)-1), 10)))
        offspring1 = parent1[:rl[0]] + parent2[rl[0]:rl[1]] + parent1[rl[1]:rl[2]] + parent2[rl[2]:rl[3]] + parent1[rl[3]:rl[4]] + parent2[rl[4]:rl[5]] + parent1[rl[5]:rl[6]] + parent2[rl[6]:rl[7]] + parent1[rl[7]:rl[8]] + parent2[rl[8]:rl[9]] + parent1[rl[9]:]
        offspring2 = parent2[:rl[0]] + parent1[rl[0]:rl[1]] + parent2[rl[1]:rl[2]] + parent1[rl[2]:rl[3]] + parent2[rl[3]:rl[4]] + parent1[rl[4]:rl[5]] + parent2[rl[5]:rl[6]] + parent1[rl[6]:rl[7]] + parent2[rl[7]:rl[8]] + parent1[rl[8]:rl[9]] + parent2[rl[9]:]

    return offspring1, offspring2


def mutation(
        individual,
        mutation_type = "single_bit_flip",
        bit_flips=None, #mult_single_mutation
        mutation_cycles=None, 
    ):
    #Single Bit Flip Mutation
    if mutation_type =="single_bit_flip":
        mutation_point = np.random.randint((len(individual)), size=1)[0]
        if individual[mutation_point] == 1: 
            individual[mutation_point] = 0
        elif individual[mutation_point] == 0:
            individual[mutation_point] = 1
        return individual

    # Complete Bit Flip Mutation
    ######### hier hab ich das geändert, dass alle bits geflipt werden?!?
    elif mutation_type =="complete_bit_flip":
        for i in range(len(individual)):
            if individual[i] == 1: 
                individual[i] = 0
            elif individual[i] == 0:
                individual[i] = 1
        return individual

    #Swap Mutation (Single Bit)
    elif mutation_type =="single_swap_mutation":
        p1=np.random.randint((len(individual)), size=1)[0]
        p2=np.random.randint((len(individual)), size=1)[0]
        value_1 = individual[p1]
        value_2 = individual[p2]
        individual[p1] = value_2
        individual[p2] = value_1
        return individual

    #Multiple Bit Flip Mutation
    #### Wir haben oben einen Parameter mit bit_flips, der wird aber hier immer überschrieben
    #### Ich glaube so werden nur bit_flips - 1 flips durchgeführt 
    elif mutation_type =="multiple_bit_flip_mutation":
        bit_flips = 2 #np.random.randint(len(individual), size=1)[0]
        for _ in range(1,bit_flips): 
            mutation_point = np.random.randint((len(individual)), size=1)[0]
            if individual[mutation_point] == 1: 
                individual[mutation_point] = 0
            elif individual[mutation_point] == 0:
                individual[mutation_point] = 1
        return individual

    # Cycle mutation (free)
    #### Das ist anders als in Vorlesung, und eigentlich das gleiche wie multiple bit flip?
    elif mutation_type =="cycle_mutation":
        for _ in range(mutation_cycles):
            mutation_point = np.random.randint((len(individual)), size=1)[0]
            if individual[mutation_point] == 1: 
                individual[mutation_point] = 0
            else: 
                individual[mutation_point] = 1
        return individual

    #Scramble Mutation 
    elif mutation_type =="scramble_mutation":
        split_point_1=np.random.randint((len(individual)), size=1)[0]
        split_point_2=np.random.randint(low= int(split_point_1), high=len(individual), size=1)[0]
        sublist = np.random.permutation(individual[split_point_1:split_point_2])
        individual[split_point_1:split_point_2] = sublist
        return individual

if __name__ == "__main__":
    # Monkey Patching
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
                fitness += 100000 # arbitrary fix value rn 

        return fitness
    Individual.get_fitness = get_fitness
    p1, p2 = Individual([0]*91), Individual([1]*91)
    # print(single_point_xo(p1, p2))
    #print(add_one_mutation(np.array([1,0,3,1,0,2,1]),0.333))