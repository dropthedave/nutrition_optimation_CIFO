from Script1_Data import nutrients, commodities
from Script2_InitialPopulation import initial_population
from Script3_Fitness import monetary_fitness
from Script4_SelectionProcess import roulette
from Script5_VariationProcess import crossover
import numpy as np

generations = 500
population_size = 100

def genetic_algorithm(generations, population_size, nutrients=nutrients, commodities=commodities, mutation_rate=0.1, crossover_rate=0.8):

	# save progress
	fitness_progress = []

	# create initial population of size n
	population = initial_population(population_size, nutrients, commodities)

	for gen in range(generations):
		
		# selection phase (based on fitness)
		parents_population = roulette(population, nutrients, commodities)

		# apply variations (check for daily nutrients)
		offspring_population = crossover(parents_population)
	
		# generational choice of survivor
		population = offspring_population

		# calculate minimum fitness of each population
		print(max(monetary_fitness(parents_population, nutrients, commodities)))
		# fitness_progress.append(min(monetary_fitness(population, commodities)))
	
	return -1 

print(genetic_algorithm(generations, population_size))