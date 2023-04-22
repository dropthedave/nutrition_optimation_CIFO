from random import shuffle, choice, sample
from individual import Individual
import numpy as np

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
