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

    max_fitness_in_pop = max([individual.fitness for individual in pop]) + 0.01 # + cent, bc. individual with highest fitness should still have a small chance to be selected
    total_inverted_fitness = sum([(max_fitness_in_pop - individual.fitness) for individual in pop])
    mark = uniform(0,total_inverted_fitness)
    position = 0
    for individual in pop:
        position += (max_fitness_in_pop - individual.fitness)
        if position > mark:
            return individual

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
    return min(pop, key=attrgetter("fitness"))