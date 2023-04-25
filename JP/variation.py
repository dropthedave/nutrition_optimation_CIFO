from data import nutrients, commodities
import numpy as np
from random import randint,random, choice, sample
from individual import Individual

def add_one_mutation(individual, mut_prob):
    mut_index = choice(range(91))
    #if random() < mut_prob:
    if individual[mut_index] == 0:
        individual[mut_index] = 1
    elif individual[mut_index] == 1:
        individual[mut_index] = 0
    return individual



def swap_mutation(population, commodities=commodities, mutation_rate=0.1):
    # if np.random.random() < mutation_rate:
        
        
    return


def single_point_xo(p1, p2):
    xo_point = randint(1, len(p1) - 1)
    offspring1 = np.concatenate((p1[:xo_point],p2[xo_point:]))
    offspring2 = np.concatenate((p2[:xo_point],p1[xo_point:]))
    return offspring1, offspring2

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
    print(single_point_xo(p1, p2))
    #print(add_one_mutation(np.array([1,0,3,1,0,2,1]),0.333))