from Script1_Data import nutrients, commodities
from Script3_Fitness import monetary_fitness
import numpy as np

def roulette(population, commodities):
    # calculate fitness for all individuals in population
    pop_fitness = monetary_fitness(population, commodities)
    # calculate probability for each individual
    pop_proba = pop_fitness / sum(pop_fitness)
    # create list with range of population
    pop_range = np.arange(len(population))
    # select individual based on probability via pop_range
    select = [np.random.choice(pop_range, p=pop_proba) for i in range(len(population))]
    # final selection of individuals
    select_final = [population[i] for i in select]
    return select_final

def ranked():
    return

def tournament():
    return