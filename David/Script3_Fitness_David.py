from Script1_Data import nutrients, commodities
from Script2_InitialPopulation_David import Initial_Population
import numpy as np

#Get the prices of the commodities
price_list = np.array([i[0] for i in list(commodities.values())])
items_list = list(commodities.keys())
product_dict = {}
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

    #Add the product list to a dictionary 
    product_dict[Individual]=product_list
    



        
        



    
            





