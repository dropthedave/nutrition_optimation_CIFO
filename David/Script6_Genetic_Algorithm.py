from Script1_Data import nutrients, commodities
from Script2_InitialPopulation_David import init_population
from Script3_Fitness_David import fitness
from Script4_SelectionProcess_David import tournament
from Script5_Crossover_David import crossover, mutation
import numpy as np

#How many generations are we training
Generations = 5000
#Set the number of individuals in the population
Nr_Individuals = 1000
#Set the number of tournaments to define the parents in the selection process
nr_tournaments = 500
#Set the number of mutation cycles
mutation_cycles = 2
mutation_prob = 10

champion_fitness = 10000000
#def genetic_algorithm(nutrients, commodities, generations, nr_individuals):
for i in range(1,Generations):
    print("Generation", i)
    if i == 1:
        #generate a initial population
        population=init_population(Nr_Individuals, commodities)
    else:  
        population = mutation_pop

    #Calculate Fitness and save the Individual with the lowest monetary value
    fitness_pop=fitness(commodities, nutrients, population)

    #Save the champion
    elite_key = min(fitness_pop, key=fitness_pop.get)
    elite_fitness = fitness_pop[elite_key]
    elite_binary=population[elite_key]

    if elite_fitness < champion_fitness:
        champion_binary=elite_binary
        champion_fitness=elite_fitness
        champion_generation = i
        print("New Champion, fitness:", champion_fitness)

    #Initiate a tournament in order to get to the parents
    parents = tournament(population, nutrients, commodities, nr_tournaments, fitness_pop)

    #perform crossover
    crossed_population = crossover(population, parents)
    mutation_pop = mutation(crossed_population, mutation_cycles, mutation_prob)
final_items=[]
items_list = list(commodities.keys())

for bin in range(len(champion_binary)):
    if champion_binary[bin] == 1:
     final_items.append(items_list[bin])

final_calories = 0
final_total_fat = 0
final_sodium = 0
final_carbs = 0
final_protein = 0


for p in final_items:
    final_calories += commodities[p][1]
    final_total_fat += commodities[p][2]
    final_sodium += commodities[p][3]
    final_carbs += commodities[p][4]
    final_protein += commodities[p][5]

print("Final Champion", champion_fitness, "found in generation", champion_generation)
print("Menu", final_items)
print("Calories", final_calories, "\n", "Total Fat",final_total_fat, "\n", "Sodium", 
final_sodium, "\n", "Carbohydrates", final_carbs, "\n","Protein",final_protein )