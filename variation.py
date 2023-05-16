from data import nutrients, commodities
import numpy as np
from random import randint, random, choice, sample
from individual import Individual

def crossover(parent1, parent2, xo_type='one-point'):
    # Convert parents to lists
    parent1 = list(parent1)
    parent2 = list(parent2)

    if xo_type == 'uniform':
        # Generate random choices for each element in the parents
        random_choices = np.random.randint(2, size=len(parent1))
        # Create offspring using uniform crossover
        offspring1 = np.where(random_choices, parent1, parent2)
        offspring2 = np.where(random_choices, parent2, parent1)
    if xo_type == 'one-point':
        # Select a random crossover point
        point = randint(1, len(parent1)-1)
        # Create offspring using one-point crossover
        offspring1 = parent1[:point] + parent2[point:]
        offspring2 = parent2[:point] + parent1[point:]
    if xo_type == 'five-point':
        # Select five random crossover points
        rl = np.array(sorted(sample(range(1, len(parent1)-1), 5)))
        # Create offspring using five-point crossover
        offspring1 = parent1[:rl[0]] + parent2[rl[0]:rl[1]] + parent1[rl[1]:rl[2]] + parent2[rl[2]:rl[3]] + parent1[rl[3]:rl[4]] + parent2[rl[4]:]
        offspring2 = parent2[:rl[0]] + parent1[rl[0]:rl[1]] + parent2[rl[1]:rl[2]] + parent1[rl[2]:rl[3]] + parent2[rl[3]:rl[4]] + parent1[rl[4]:]
    if xo_type == 'ten-point':
        # Select ten random crossover points
        rl = np.array(sorted(sample(range(1, len(parent1)-1), 10)))
        # Create offspring using ten-point crossover
        offspring1 = parent1[:rl[0]] + parent2[rl[0]:rl[1]] + parent1[rl[1]:rl[2]] + parent2[rl[2]:rl[3]] + parent1[rl[3]:rl[4]] + parent2[rl[4]:rl[5]] + parent1[rl[5]:rl[6]] + parent2[rl[6]:rl[7]] + parent1[rl[7]:rl[8]] + parent2[rl[8]:rl[9]] + parent1[rl[9]:]
        offspring2 = parent2[:rl[0]] + parent1[rl[0]:rl[1]] + parent2[rl[1]:rl[2]] + parent1[rl[2]:rl[3]] + parent2[rl[3]:rl[4]] + parent1[rl[4]:rl[5]] + parent2[rl[5]:rl[6]] + parent1[rl[6]:rl[7]] + parent2[rl[7]:rl[8]] + parent1[rl[8]:rl[9]] + parent2[rl[9]:]

    # Return the resulting offspring
    return offspring1, offspring2


def mutation(
        individual,
        mutation_type="single_bit_flip",
        bit_flips=None,                                     # Number of bit flips for multiple_bit_flip_mutation
        mutation_cycles=None,
    ):
    # Single Bit Flip Mutation
    if mutation_type == "single_bit_flip":
        mutation_point = np.random.randint(len(individual), size=1)[0]
        if individual[mutation_point] == 1:
            individual[mutation_point] = 0
        elif individual[mutation_point] == 0:
            individual[mutation_point] = 1
        return individual

    # Complete Bit Flip Mutation
    # Flips all bits in the individual
    elif mutation_type == "complete_bit_flip":
        for i in range(len(individual)):
            if individual[i] == 1:
                individual[i] = 0
            elif individual[i] == 0:
                individual[i] = 1
        return individual

    # Swap Mutation (Single Bit)
    elif mutation_type == "single_swap_mutation":
        p1 = np.random.randint(len(individual), size=1)[0]
        p2 = np.random.randint(len(individual), size=1)[0]
        value_1 = individual[p1]
        value_2 = individual[p2]
        individual[p1] = value_2
        individual[p2] = value_1
        return individual

    # Multiple Bit Flip Mutation
    # Flips a specified number of bits in the individual
    # The number of bit flips is determined by the 'bit_flips' parameter
    elif mutation_type == "multiple_bit_flip_mutation":
        for _ in range(bit_flips): 
            mutation_point = np.random.randint(len(individual), size=1)[0]
            if individual[mutation_point] == 1:
                individual[mutation_point] = 0
            elif individual[mutation_point] == 0:
                individual[mutation_point] = 1
        return individual

    # Scramble Mutation 
    elif mutation_type == "scramble_mutation":
        split_point_1 = np.random.randint(len(individual), size=1)[0]
        split_point_2 = np.random.randint(low=int(split_point_1), high=len(individual), size=1)[0]
        sublist = np.random.permutation(individual[split_point_1:split_point_2])
        individual[split_point_1:split_point_2] = sublist
        return individual