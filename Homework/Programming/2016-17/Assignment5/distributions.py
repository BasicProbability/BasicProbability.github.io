from math import log, exp

class GeometricDistribution(object):
    '''An implementation of the geometric distribution that whose support includes 0.'''

    def __init__(self, param=0.5):
        '''Constructor

        :param param: The parameter of this geometric distribution
        :raises: ValueError if param is not in [0,1]
        '''
        if param < 0 or param > 1:
            raise ValueError("The parameter {} is invalid for the geometric distribution".format(param))

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