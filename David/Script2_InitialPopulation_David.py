from Script1_Data import nutrients, commodities
import numpy as np

#Set the number of individuals in the population
Nr_Individuals = 10

def init_population(Nr_Individuals, commodities):
    #Create an empty dictionary for the population
    Population = {}
    #Iterate through the number of set individuals
    for i in range(1, Nr_Individuals+1):
        #Generate a random individual
        Individual = np.random.randint(2, size=len(commodities))
        #Add it to the population 
        Population[i] = Individual
    return Population

#Save 1000 instances of the initial population
Initial_Population=init_population(Nr_Individuals, commodities)
