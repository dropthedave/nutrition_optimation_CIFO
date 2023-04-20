from Script1_Data import nutrients, commodities
from Script2_InitialPopulation import random_population
from Script3_Fitness import monetary_fitness
from Script4_SelectionProcess import roulette
# from Script5_Variation import mutation, crossover
import numpy as np

generations = 100
population_size = 100

def genetic_algorithm(generations, population_size, nutrients=nutrients, commodities=commodities, mutation_rate=0.1, crossover_rate=0.8):

	# save progress
	fitness_progress = []

	# create initial population of size n
	population = random_population(population_size, nutrients, commodities)

	for gen in range(generations):
		
		# selection phase (based on fitness)
		parents_population = roulette(population, commodities)
		
		# apply variations (check for daily nutrients)
		# offspring_population = variation(parents_population)
	
		# generational choice of survivor
		# population = offspring_population
		population = parents_population

		# calculate minimum fitness of each population
		print(min(monetary_fitness(parents_population, commodities)))
		# fitness_progress.append(min(monetary_fitness(population, commodities)))
	
	return #fitness_progress

print(genetic_algorithm(generations, population_size))