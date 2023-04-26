from Script1_Data import nutrients, commodities
from Script2_InitialPopulation_David import Initial_Population
from Script3_Fitness_David import monetary_fitness
import numpy as np

nr_tournaments = 100

def tournament(pop_fitness):
    parents = []
    for i in range(1,nr_tournaments+1):
        
        #Define first contender
        gladiator_1=np.random.randint(1,(len(pop_fitness)), size=1)[0]
        #Define second contender
        gladiator_2 = np.random.randint(1,(len(pop_fitness)), size=1)[0]

        #print("Tournament",i, gladiator_1, gladiator_2)
        #Let them fight. The lowest value wins
        if pop_fitness[gladiator_1] > pop_fitness[gladiator_2]: 
            parents.append(gladiator_2)

        elif pop_fitness[gladiator_2] > pop_fitness[gladiator_1]: 
             parents.append(gladiator_1)
        
        elif pop_fitness[gladiator_2] == pop_fitness[gladiator_1]: 
             parents.append(gladiator_1)    

    return parents 
    
parents=tournament(monetary_fitness)
