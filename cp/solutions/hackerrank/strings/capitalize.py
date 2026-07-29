#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    '''
        My solution:
        Because the input is one full string separated by whitespace,
        if it's contain a single digit in that string,
        the whole string will not be capitalize!

        Hence one test case was failed.

        Test case: "1 w 2 r 3g"
    '''
    # if s.isalnum():
    #     return s

    # return s.title()

    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
