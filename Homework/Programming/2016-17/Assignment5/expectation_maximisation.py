import random, sys
from math import log, exp, factorial
from logarithms import log_add, log_add_list

class GeometricDistribution(object):
    '''An implementation of the geometric distribution that whose support includes 0.'''

    def __init__(self, param=0.5):
        '''Constructor

        :param param: The parameter of this geometric distribution
        :raises: ValueError if param is not in [0,1]
        '''

        self.failure = log(1 - param)
        self.success = log(param)

    def log_prob(self, x):
        '''Compute the log-probability of an observation

        :param x: The observation
        :return: The log-probability of x under this distribution
        :raises: ValueError if x is not a non-negative integer
        '''

        if x%1 != 0 or x < 0:
            raise ValueError("x is not a non-negative integer")

        return self.success + x*self.failure

    def get_param(self):
        '''Get the parameter of this distribution

        :return: The parameter of this distribution
        '''
        return exp(self.success)


class EM(object):
    '''A geometric mixture model that can be trained using EM'''

    def __init__(self, num_components = 5, initial_mixture_weights = None, initial_geometric_parameters = None):
        '''Constructor

        :param num_components: The number of mixture components in this model
        :param initial_mixture_weights: A list of initial mixture weights (weights are initialised randomly if no list is provided)
        :param initial_geometric_parameters: A list of initial component parameters (initialised randomly if no list is provided)
        '''

        self.num_components = num_components
        # Map from components to their priors
        self.mixture_weights = list()
        # Map from components to their distributions
        self.component_distributions = list()
        # map from components to their expected number of occurrence
        self.expected_component_counts = dict()
        # map from components to expected values of observations that they generate
        self.expected_observation_counts = dict()
        self.log_likelihood = 0
        self.initialise(initial_mixture_weights, initial_geometric_parameters)

    def initialise(self, initial_mixture_weights, initial_geometric_parameters):
        '''Initialise the parameters of this model

        :param initial_mixture_weights: A list of initial mixture weights (weights are initialised randomly if no list is provided)
        :param initial_geometric_parameters: A list of initial component parameters (initialised randomly if no list is provided)
        '''

        for component in range(self.num_components):
            self.mixture_weights.append(random.random())
            self.component_distributions.append(GeometricDistribution(random.random()))
            self.expected_component_counts[component] = -float("inf")
            self.expected_observation_counts[component] = -float("inf")

        # normalise priors
        prior_sum = sum(self.mixture_weights)
        for component in range(self.num_components):
            # normalise and tranform to log-prob
            self.mixture_weights[component] = log(self.mixture_weights[component] / prior_sum)

    def train(self, data_path, iterations):
        '''Train the model on data for a fixed number of iterations. After each iteration of training, the log-likelihood,
        mixture weights and component parameters are printed out.

        :param data_path: The path to the data file
        :param iterations: The number of iterations
        '''

        for iter in range(iterations):
            self.em(data_path)

            params = list()
            priors = list()
            for component in range(self.num_components):
                params.append(self.component_distributions[component].get_param())
                priors.append(exp(self.mixture_weights[component]))

            print("Iteration {}".format(iter + 1))
            print('log-likelihood: {}'.format(self.log_likelihood))
            print("Component priors: {}".format(priors))
            print("Component parameters: {}".format(params))

            # reset log-likelihood
            self.log_likelihood = 0


    def em(self, data_path):
        '''Perform one iteration of EM on the data

        :param data_path: The path to the data file
        '''
        with open(data_path) as data:
            for line in data:
                for observation in line.split():
                    self.e_step(int(observation))

        self.m_step()


    def e_step(self, observation):
        '''Perform the E-step on a single obervation. That is, compute the posterior of mixture components
        and add the expected occurrence of each component to the running total.

        :param observation: The observation
        '''

        #TODO: Implement this. Make sure to update the log-likelihood during the E-step.

    def m_step(self):
        '''Perform the M-step'''

        #TODO: Implement this. Make sure to reset the data structures you use for counting after you have
        # updated all parameters.

def main(args):
    file_path = args[0]
    mixture_components = args[1]

    learner = EM(int(mixture_components))
    learner.train(file_path, 20)

if __name__ == "__main__":
    main(sys.argv[1:])
