from Script1_Data import nutrients, commodities
from Script2_InitialPopulation import random_population
from Script3_Fitness import monetary_fitness
from Script4_SelectionProcess import roulette
# from Script5_Variation import mutation, crossover
import numpy as np

generations = 10
population_size = 20

def genetic_algorithm(nutrients, commodities, generations, population_size):

	# save progress
	fitness_progress = []

	# create initial population of size n
	population = random_population(population_size, nutrients, commodities)

	for gen in range(generations):

		# selection phase (based on fitness)
		parents_population = roulette(population, commodities)

		# apply variations (check for daily nutrients)
		offspring_population = variation(parents_population)
	
		# generational choice of survivor
		population = offspring_population

		# save best fitness value of generation
		fitness_progress.append(np.min([monetary_fitness(individual, commodities) for individual in population]))

	# calculate individual with minimum fitness (items value)
	solution = np.min([monetary_fitness(individual, commodities) for individual in population])

	return f'Min. monetary value: {solution}', fitness_progress

solution, fitness_progress = genetic_algorithm(nutrients, commodities, generations, population_size)
print(fitness_progress)