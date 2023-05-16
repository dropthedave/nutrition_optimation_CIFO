import numpy as np
import pandas as pd
from Data_f import nutrients, commodities
import random
import matplotlib.pyplot as plt


def generate_population(size):
	population = []
	for _ in range(POPULATION_SIZE):
		genes = [0, 1]
		chromosome = []
		for _ in range(len(size)):
			chromosome.append(random.choice(genes))
		population.append(chromosome)
	#print("Generated a random population of size", len(size))
	return population

def calculate_fitness(chromosome):
	fitness = 0 
	calories = 0
	total_fat = 0
	cholesterol = 0
	sodium = 0
	carbohydrates = 0
	sugar = 0
	protein = 0

	for i in range(0, len(chromosome)):
		if chromosome[i] == 1:
			fitness += commodity_values[i][0]
			calories += commodity_values[i][1]
			total_fat += commodity_values[i][2]
			sodium += commodity_values[i][4]
			carbohydrates += commodity_values[i][5]
			protein += commodity_values[i][7]
			
	if (calories        > nutrients['Calories (kcal)'] and 
        total_fat       > nutrients['Total Fat (g)'] and
        sodium          > nutrients['Sodium (mg)'] and
        carbohydrates   > nutrients['Carbohydrates (g)'] and
        protein         > nutrients['Protein (g)']):
		# print('calories =', calories)
		# print('total_fat =', total_fat)
		# print('sodium =', sodium)
		# print('carbohydrates =', carbohydrates)
		# print('protein =', protein)
		
		return fitness
	else:
		# print('calories =', calories)
		# print('total_fat =', total_fat)
		# print('sodium =', sodium)
		# print('carbohydrates =', carbohydrates)
		# print('protein =', protein)
		return 1000000

def roulette(population, commodities=commodities):
    # calculate fitness for all individuals in population
    pop_fitness = np.array([calculate_fitness(x) for x in population])
    # calculate probability for each individual
    # SMALLER FITNESS = HIGHER PROBABILITY TO BE SELECTED
    inverted_fitness = np.sum(pop_fitness) - pop_fitness
    pop_proba = inverted_fitness / np.sum(inverted_fitness)
    # create list with range of population
    pop_range = np.arange(len(population))
    # select individual based on probability via pop_range
    select = [np.random.choice(pop_range, p=pop_proba) for i in range(len(population))]
    # final selection of individuals
    select_final = [population[i] for i in select]
    return select_final

def tournament(population, k=3):
    # Select parents using tournament selection
    fitnesses = np.array([calculate_fitness(x) for x in population])
    parents = []
    for i in range(len(population)):
        tournament = random.sample(range(len(population)), k)
        tournament_fitnesses = [fitnesses[tournament[j]] for j in range(k)]
        winner = tournament[np.argmin(tournament_fitnesses)]
        parents.append(population[winner])
    return parents

def crossover(parents, k='one-point'):
    offspring = []
    for i in range(0, len(parents), 2):
        parent1, parent2 = list(parents[i]), list(parents[i+1])
        if k == 'uniform':
              offspring1 = [] 
              offspring2 = []
              for i in range(0, (len(parent1)-1)):
                    temp_list = []
                    temp_list.append(parent1[i])
                    temp_list.append(parent2[i])
                    temp_array = np.array(temp_list)
                    offspring1.append(np.random.choice(temp_array))
                    offspring2.append(np.random.choice(temp_array))
        if k == 'one-point':
            point = random.randint(1, len(parent1)-2)
            offspring1 = parent1[:point] + parent2[point:]
            offspring2 = parent2[:point] + parent1[point:]
        if k == 'five-point':
            rl = np.array(sorted(random.sample(range(1, len(parent1)-2), 5)))
            offspring1 = parent1[:rl[0]] + parent2[rl[0]:rl[1]] + parent1[rl[1]:rl[2]] + parent2[rl[2]:rl[3]] + parent1[rl[3]:rl[4]] + parent2[rl[4]:]
            offspring2 = parent2[:rl[0]] + parent1[rl[0]:rl[1]] + parent2[rl[1]:rl[2]] + parent1[rl[2]:rl[3]] + parent2[rl[3]:rl[4]] + parent1[rl[4]:]
        if k == 'ten-point':
            rl = np.array(sorted(random.sample(range(1, len(parent1)-2), 5)))
            offspring1 = parent1[:rl[0]] + parent2[rl[0]:rl[1]] + parent1[rl[1]:rl[2]] + parent2[rl[2]:rl[3]] + parent1[rl[3]:rl[4]] + parent2[rl[4]:rl[5]] + parent1[rl[5]:rl[6]] + parent2[rl[6]:rl[7]] + parent1[rl[7]:rl[8]] + parent2[rl[8]:rl[9]] + parent1[rl[9]:]
            offspring2 = parent2[:rl[0]] + parent1[rl[0]:rl[1]] + parent2[rl[1]:rl[2]] + parent1[rl[2]:rl[3]] + parent2[rl[3]:rl[4]] + parent1[rl[4]:rl[5]] + parent2[rl[5]:rl[6]] + parent1[rl[6]:rl[7]] + parent2[rl[7]:rl[8]] + parent1[rl[8]:rl[9]] + parent2[rl[9]:]

        offspring.append(offspring1)
        offspring.append(offspring2)
    return offspring

def plot_fitness_curve(generations, fitness):
    plt.plot(generations, fitness)
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.title("Fitness Curve")
    plt.show()

def plot_nutrition_curve(generations, history_calories, history_protein, history_carbohydrates, history_fat, history_sodium, history_sugar):
    plt.plot(generations, history_calories, label='Calories (kcal)', c='r')
    plt.axhline(y = nutrients['Calories (kcal)'], linestyle = ':', c='r')
    plt.plot(generations, history_protein, label='Protein (g)', c='g')
    plt.axhline(y = nutrients['Protein (g)'], linestyle = ':', c='g')
    plt.plot(generations, history_carbohydrates, label='Carbohydrates (g)', c='b')
    plt.axhline(y = nutrients['Carbohydrates (g)'], linestyle = ':', c='b')
    plt.plot(generations, history_fat, label='Total Fat (g)', c='c')
    plt.axhline(y = nutrients['Total Fat (g)'], linestyle = ':', c='c')
    plt.plot(generations, history_sodium, label='Sodium (mg)', c='m')
    plt.axhline(y = nutrients['Sodium (mg)'], linestyle = ':', c='m')
    plt.yscale("log")
    plt.xlabel("Generations")
    plt.ylabel("Nutrition Values")
    plt.title("Nutrition Curve")
    plt.legend(loc ="best", fontsize="6")
    plt.show()


#########################################

POPULATION_SIZE = 1000
GENERATIONS = 40
commodity_values = list(commodities.values())
commodity_keys = list(commodities.keys())

##########################################

if __name__ == '__main__':
        
    population = generate_population(commodities)

    fitness_history = []
    history_calories = []
    history_protein = []
    history_carbohydrates = []
    history_fat = []
    history_sodium = []
    history_sugar = []

    for i in range(GENERATIONS):

        parents = tournament(population)
        mutations = crossover(parents, k='one-point')
        population = mutations
        fitness = min(np.array([calculate_fitness(x) for x in mutations]))
        fitness_index = np.argmin(np.array([calculate_fitness(x) for x in mutations]))
        x = population[fitness_index]
        fitness_history.append(fitness)
        print(fitness)
        food = []
        total_calories = 0
        total_protein = 0
        total_carbohydrates = 0
        total_fat = 0
        total_sodium = 0
        total_sugar = 0

        for i, j, h in zip(x, commodity_keys, commodity_values):
            if i == 1:
                    total_calories += h[1]  
                    total_protein += h[7] 
                    total_carbohydrates += h[5] 
                    total_fat += h[2] 
                    total_sodium += h[4] 
                    total_sugar += h[6]
                    food.append(j)

        history_calories.append(total_calories)  
        history_protein.append(total_protein) 
        history_carbohydrates.append(total_carbohydrates) 
        history_fat.append(total_fat) 
        history_sodium.append(total_sodium) 
        history_sugar.append(total_sugar)



    print(food)
    print('Calories (kcal) ', total_calories)
    print('Total Fat (g) ', total_fat)
    print('Sodium (mg) ', total_sodium)
    print('Carbohydrates (g) ',total_carbohydrates )
    print('Protein (g) ', total_protein)
    print('Sugars (g) ', total_sugar)
            
    #plot_fitness_curve(list(range(GENERATIONS)), fitness_history)
    plot_nutrition_curve(list(range(GENERATIONS)), history_calories, history_protein, history_carbohydrates, history_fat, history_sodium, history_sugar)




######## notes 
# Uniform crossover - second offspring invertion of offsping one 