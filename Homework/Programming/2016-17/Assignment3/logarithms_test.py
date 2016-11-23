'''
Created on Sep 19, 2015

@author: philip
'''
import unittest
from random import Random
from math import log, exp

# imports the functions from logarithms module from the src folder
from logarithms_solution import log_add, log_add_list, log_subtract, log_subtract_list

class LogarithmsTest(unittest.TestCase):
    # Random number generator to generate test cases
    random_generator = Random()

    def test_log_add(self):
        '''
        Test the log_add function by using it to add the logs of 10.000 randomly 
        generated numbers in [0,1)
        '''
        
        for i in range(10000):
            first_num = self.random_generator.random()
            second_num = self.random_generator.random()
            first_log = log(first_num)
            second_log = log(second_num)
            
            result = first_num + second_num
            
            # allow for numerical imprecision up to 1/10000
            self.assertTrue(abs(result - exp(log_add(first_log, second_log))) < 0.0001)

    def test_log_add_works_with_infinity(self):
        '''
        Test that log addtition works if -infinity is supplied as an argument.
        '''

        first_num = log(self.random_generator.random())
        second_num = log(self.random_generator.random())

        self.assertEqual(first_num, log_add(first_num, -float("inf")))
        self.assertEqual(first_num, log_add(-float("inf"), second_num))

    def test_log_difference(self):
        '''
        Test the log_difference function by using it to add the logs of 10.000 randomly 
        generated numbers in [0,1)
        '''
    
        for i in range(10000):
            first_num = self.random_generator.random()
            second_num = self.random_generator.random()
            
            first_log = log(first_num)
            second_log = log(second_num)
            
            # make sure the first argument is always bigger than the second
            if (first_num >= second_num):
                result = first_num - second_num
                # allow for numerical imprecision up to 1/10000
                self.assertTrue(abs(result - exp(log_subtract(first_log, second_log))) < 0.0001)
            else:
                result = second_num - first_num
                # allow for numerical imprecision up to 1/10000
                self.assertTrue(abs(result - exp(log_subtract(second_log, first_log))) < 0.0001)

if __name__ == "__main__":
    unittest.main()