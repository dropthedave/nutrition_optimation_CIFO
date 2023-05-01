from data import nutrients, commodities
import numpy as np
from random import uniform, choice
from operator import attrgetter


def roulette(pop):
    # # inverted with 1/ -> probably not good, bc. fitness is often too high in beginning
    # total_inverted_fitness = sum([(1/individual.fitness) for individual in pop])
    # mark = uniform(0,total_inverted_fitness)
    # position = 0
    # for individual in pop:
    #     position += (1/individual.fitness)
    #     if position > mark:
    #         return individual
    
    fitness = [individual.fitness for individual in pop]
    sum_fitness_in_pop = sum(fitness)
    inverted_fitness = sum_fitness_in_pop - np.array(fitness)
    probability = inverted_fitness / sum(inverted_fitness)
    # create list with range of population
    pop_range = np.arange(len(pop))
    # select individual based on probability via pop_range
    select = np.random.choice(pop_range, p=probability)
    individual = pop[select]
    return individual
    
    # fitness = [individual.fitness for individual in pop]
    # sum_fitness_in_pop = sum(fitness)
    # inverted_prob = 1 - np.array(fitness/sum_fitness_in_pop)
    # index = np.random.choice(list(range(len(sorted_pop))), p=inverted_prob)
    # return sorted_pop[index]

def ranked(pop):
    sorted_pop = sorted(pop, key=lambda individual: individual.fitness, reverse=True)
    denominator = sum(list(range(len(sorted_pop)+1)))
    dist = [i/denominator for i in list(range(1,len(sorted_pop)+1))]
    index = np.random.choice(list(range(len(sorted_pop))), p=dist)
    return sorted_pop[index]

def tournament(pop,k):
    tournament = []
    for _ in range(k):
        tournament.append(choice(pop))
    return min(tournament, key=attrgetter("fitness"))