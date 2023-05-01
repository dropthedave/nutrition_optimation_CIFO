from data import commodities, nutrients
from random import shuffle, choice, sample, random
from individual import Individual
import numpy as np
from copy import deepcopy
from operator import attrgetter
import matplotlib.pyplot as plt


class Population:
    def __init__(self, size, optim, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        self.history_fitness = []
        self.history_calories = []
        self.history_protein = []
        self.history_carbohydrates = []
        self.history_fat = []
        self.history_sodium = []
        #self.history_sugar = []
        self.history_products = []
        for _ in range(size):
            self.individuals.append(
                Individual(
                size=kwargs["sol_size"],
                replacement=kwargs["replacement"],
                valid_set=kwargs["valid_set"],
            ))

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]
    
    def __repr__(self):
        output = ""
        for individual in self.individuals:
            output = output + str(individual) + "\n"
        return output
    
    def evolve(self,
            select=None,
            tournament_k=None,
            crossover=None,
            mutate=None,
            gens= 100, 
            mut_prob = 0.2,
            mut_type = "single_bit_flip",
            mut_cycles = None,
            bit_flips = None,
            xo_prob = 0.9,
            xo_type = "one-point",
            elitism=True
    ):
        for i in range(gens): # our termination condition
            new_gen = []
                    
            while len(new_gen) < len(self):
                # select
                if tournament_k is None:
                    parent1, parent2 = select(self), select(self)
                else:
                    parent1 = select(self, k=tournament_k)
                    parent2 = select(self, k=tournament_k)
                # crossover
                if random() < xo_prob:
                    offspring1, offspring2 = crossover(parent1, parent2, xo_type)
                else: # replication
                    offspring1 = parent1
                    offspring2 = parent2
                #mutation
                if random() < mut_prob: 
                    offspring1 = mutate(offspring1, mut_type, bit_flips=bit_flips, mutation_cycles=mut_cycles, )
                if random() < mut_prob:
                    offspring2 = mutate(offspring2, mut_type)

                new_gen.append(Individual(offspring1))
                new_gen.append(Individual(offspring2))
            
            if elitism:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                    worst_new = min(new_gen, key=attrgetter("fitness"))
                    if elite.fitness > worst_new.fitness:
                        new_gen.pop(new_gen.index(worst_new))
                        new_gen.append(elite)
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))
                    worst_new = max(new_gen, key=attrgetter("fitness"))
                    if elite.fitness < worst_new.fitness:
                        new_gen.pop(new_gen.index(worst_new))
                        new_gen.append(elite)

            self.individuals = new_gen
            best = min(self, key=attrgetter("fitness"))
            # print(f'Best Individual: {best}') # take best individual wrt. attribut 'fitness'
            self.history_fitness.append(best.fitness)
            self.history_calories.append(best.totals[0])
            self.history_fat.append(best.totals[1]) 
            self.history_sodium.append(best.totals[2]) 
            self.history_carbohydrates.append(best.totals[3]) 
            self.history_protein.append(best.totals[4]) 
            #self.history_sugar.append(best.totals[5])
        # print("Products:")
        commodity_keys = list(commodities.keys())
        for i, j in zip(min(self, key=attrgetter("fitness")).representation, commodity_keys):
            if i == 1:
                self.history_products.append(j)

    def plot_fitness_curve(self):
        generations = list(range(len(self.history_calories)))
        plt.plot(generations, self.history_fitness)
        plt.xlabel("Generations")
        plt.ylabel("Fitness")
        plt.title("Fitness Curve")
        plt.show()

    def plot_nutrition_curve(self):
        generations = list(range(len(self.history_calories)))
        plt.plot(generations, self.history_calories, label='Calories (kcal)', c='r')
        plt.axhline(y = nutrients['Calories (kcal)'], linestyle = ':', c='r')
        plt.plot(generations, self.history_protein, label='Protein (g)', c='g')
        plt.axhline(y = nutrients['Protein (g)'], linestyle = ':', c='g')
        plt.plot(generations, self.history_carbohydrates, label='Carbohydrates (g)', c='b')
        plt.axhline(y = nutrients['Carbohydrates (g)'], linestyle = ':', c='b')
        plt.plot(generations, self.history_fat, label='Total Fat (g)', c='c')
        plt.axhline(y = nutrients['Total Fat (g)'], linestyle = ':', c='c')
        plt.plot(generations, self.history_sodium, label='Sodium (mg)', c='m')
        plt.axhline(y = nutrients['Sodium (mg)'], linestyle = ':', c='m')
        plt.yscale("log")
        plt.xlabel("Generations")
        plt.ylabel("Nutrition Values")
        plt.title("Nutrition Curve")
        plt.legend(loc ="best", fontsize="6")
        plt.show()