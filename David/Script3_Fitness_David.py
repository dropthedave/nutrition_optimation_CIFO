from Script1_Data import nutrients, commodities
from Script2_InitialPopulation_David import Initial_Population
import numpy as np

def fitness(commodities, nutrients, Initial_Population):
    #Get the prices of the commodities
    price_list = np.array([i[0] for i in list(commodities.values())])
    items_list = list(commodities.keys())
    #Define a dictionary for the fitness
    fitness_dict={}

    #Iterate through the population
    for Individual in Initial_Population:

        #calculate fitness of the individual 
        fitness=(Initial_Population[Individual]*price_list).sum()
        #Iterate through the binary list of individuals and retrieve the product names
        product_list=[]

        for j in range(0,Initial_Population[Individual].size):
            #If the Individual has a 1, add the product to the list
            if Initial_Population[Individual][j] == 1: 
                product_list.append(items_list[j])

            #Define variables for the different nutritional keys
            calories = 0
            total_fat=0
            sodium=0
            carbs=0
            protein=0

        #Iterate through the nutrient list to check if the constraints are met
        for p in product_list:
            calories += commodities[p][1]
            total_fat += commodities[p][2]
            sodium += commodities[p][3]
            carbs += commodities[p][4]
            protein += commodities[p][5]


        #Compare with the nutritional values from the table. If insufficient give bad fitness (high)
        if (
        calories < nutrients['Calories (kcal)'] 
        or total_fat < nutrients['Total Fat (g)'] 
        or sodium < nutrients['Sodium (mg)'] 
        or carbs < nutrients['Carbohydrates (g)'] 
        or protein < nutrients['Protein (g)']) :
            #Set fitness to a very high value
            fitness = 10000
        
        fitness_dict[Individual]=fitness
    return fitness_dict


monetary_fitness=fitness(commodities, nutrients, Initial_Population)

# elite = min(monetary_fitness, key=monetary_fitness.get)
# elite_fitness = monetary_fitness[elite]
# print(elite, elite_fitness)
# elite_binary=Initial_Population[elite]
# print(elite_binary)