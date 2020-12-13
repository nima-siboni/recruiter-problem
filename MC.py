"""
Solves the secretary problem

1 - creates events: which includes N_HIRING samples each having N_CANDIDATES
2 - loops over the whole events, each time changing when to stop exploring data 
(and start choosing the candidate). For each stopping point, the results are 
evaluted in the form of the probability of successfully finding the best 
candidate for that stopping point
3 - finally the results are plotted and saved.

Keyword arguments:

N_HIRINGS -- number of samples (number of hirings)

N_CANDIDATES -- number of candidates per each samplec

CHOOSING_METHOD -- the method by which the candidates are chosen
['max', 'mean']

DISTRIBUTION -- the random distribution from which the samples are drawn.
"""

import random
import numpy as np
from environement import create_samples
from environement import evaluations, evaluations_reward
from environement import find_the_best
from plotter import plot

N_HIRINGS = 5_000
N_CANDIDATES = 20
CHOOSING_METHOD = 'max'
DISTRIBUTION = 'random'

random.seed(1)

# 1

events = create_samples(N_HIRINGS, N_CANDIDATES, 'uniform')
results = np.zeros((N_CANDIDATES - 1, 2))

# 2

for stopping_id in range(1, N_CANDIDATES):
    chosen = find_the_best(events, stopping_id, choosing_method=CHOOSING_METHOD)
    results[stopping_id - 1] = [stopping_id, evaluations_reward(chosen)]

# 3

np.savetxt('results.dat', results)
plot(results,
     title="average score of the hired candidates vs. stopping point",
     xlabel="Stopping point",
     ylabel="(ave.) Score",
     xtics=1,
     filename="./results.png")
