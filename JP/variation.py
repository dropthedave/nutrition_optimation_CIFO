from data import nutrients, commodities
import numpy as np
from random import randint,random

def add_one_mutation(individual, mut_prob):
    for mut_index in range(len(individual)):
        if random() < mut_prob:
            if individual[mut_index] == 0:
                individual[mut_index] = 1
            elif individual[mut_index] > 0:
                if random() < 0.5:
                    individual[mut_index] = individual[mut_index] + 1
                else:
                    individual[mut_index] = individual[mut_index] - 1
    return individual



def swap_mutation(population, commodities=commodities, mutation_rate=0.1):
    # if np.random.random() < mutation_rate:
        
        
    return


def single_point_xo(p1, p2):
    xo_point = randint(1, len(p1) - 1)
    offspring1 = np.concatenate((p1[:xo_point],p2[xo_point:]))
    offspring2 = np.concatenate((p2[:xo_point],p1[xo_point:]))

    return offspring1, offspring2


if __name__ == "__main__":
    p1, p2 = np.array([0,0,0,0,0]), np.array([1,1,1,1,1])
    print(single_point_xo(p1, p2))
    print(add_one_mutation(np.array([1,0,3,1,0,2,1]),0.333))