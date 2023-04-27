from data import commodities, nutrients
from random import shuffle, choice, sample, random
from individual import Individual
import numpy as np
from copy import deepcopy
from operator import attrgetter

class Population:
    def __init__(self, size, optim, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
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
            print(f'Best Individual: {min(self, key=attrgetter("fitness"))}') # take best individual wrt. attribut 'fitness'
        print("Products:")
        commodity_keys = list(commodities.keys())
        for i, j in zip(min(self, key=attrgetter("fitness")).representation, commodity_keys):
            if i == 1:
                print(j, commodities[j][0])
        print("Total values:")
        nutrient_keys = list(nutrients.keys())
        nutrient_values = list(nutrients.values())
        for i, j, k in zip(min(self, key=attrgetter("fitness")).totals, nutrient_keys, nutrient_values):
            print(j,":", i, "(min:", str(k) + ")")
