#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
sol = [
        [4,9,2,3,5,7,8,1,6],
        [4,3,8,9,5,1,2,7,6],
        [6,7,2,1,5,9,8,3,4],
        [8,1,6,3,5,7,4,9,2],
        [6,1,8,7,5,3,2,9,4],
        [2,9,4,7,5,3,6,1,8],
        [8,3,4,1,5,9,6,7,2],
        [2,7,6,9,5,1,4,3,8],
    ]
def formingMagicSquare(s):
    # Write your code here
    # one_dim = s[0]+s[1]+s[2]
    
    mini_cost = math.inf
    for each_sol in sol :
        diff = 0
        for i,ii in zip(each_sol, s):
            diff += abs(i-ii)
        mini_cost = min(mini_cost, diff)
    return mini_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s = s + list(map(int, input().split(" ")))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
