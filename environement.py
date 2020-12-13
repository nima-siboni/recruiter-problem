import numpy as np


def create_samples(N_HIRINGS, N_CANDIDATES, distribution):
    """
    creates N_HIRING samples of candidates where each hiring process has
    N_CANDIDATES. The quality of candidates are randomly deriven from the
    distribution
    """
    implemented_dist = ['uniform', 'normal', 'pareto']

    assert distribution in implemented_dist

    if (distribution == 'uniform'):
        events = np.random.random(size=(N_HIRINGS, N_CANDIDATES))
    elif distribution == 'normal':
        events = np.random.normal(loc=0, scale=1, size=(N_HIRINGS, N_CANDIDATES))
    elif (distribution == 'pareto'):
        events = np.random.pareto(a=1.1, size=(N_HIRINGS, N_CANDIDATES))
    return events

def find_the_best(input_events, n_exploring, choosing_method):
    """ finds the >>first<< qualified candidate from the input_events after
    exlporing the first n_exploring candidates.
    
    inputs:
    input_events: all the candidates for all the hiring samples
    n_exploring: exploring the candidates up to n_exploring, before choosing one
    
    output:
    output_chosen: the chosen candidates for each hiring sample
    """

    # if no candidate is found to meet the criterion:
    # the last candidate is chosen.
    output_chosen = input_events[:, -1] + 0.0

    (nr_hirings, _) = np.shape(input_events)

    # the data is divided into two nonoverlaping parts:
    # (1): the exploratory_data from which the statistics of the samples are taken
    # (2): the choosing_data from which the candidates are chosen based on the

    exploratory_data = input_events[:, :n_exploring]
    choosing_data = input_events[:, n_exploring:]
    (_, nr_remaining_candidates) = np.shape(choosing_data)

    if choosing_method == 'mean':
        criterion_exploration = np.mean(exploratory_data, axis=1)
        criterion_exploration = np.reshape(criterion_exploration, (nr_hirings, 1))

    elif choosing_method == 'max':
        criterion_exploration = np.max(exploratory_data, axis=1)
        criterion_exploration = np.reshape(criterion_exploration, (nr_hirings, 1))

    for i in range(nr_hirings):
        finished = False
        criteria_i = criterion_exploration[i]
        for j in range(nr_remaining_candidates):
            if ((finished is False) and (choosing_data[i][j] > criteria_i)):
                output_chosen[i] = choosing_data[i][j] + 0
                finished = True
    return output_chosen


def evaluations(input_chosen, input_events):
    """ evaluation of the how good were the chosen ones:
    if the best one is chosen.
    """

    ultimate_best = np.max(input_events, axis=1)
    ultimate_best = np.reshape(ultimate_best, np.shape(input_chosen))
    return np.mean(np.equal(ultimate_best, input_chosen))


def evaluations_reward(input_chosen):
    """ evaluation of the how good were the chosen ones:
    by the value of the chosen one.
    """
    return np.mean(input_chosen)
