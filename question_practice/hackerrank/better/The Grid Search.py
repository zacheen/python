#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here
    bound_i = len(G) - len(P)
    bound_ii = len(G[0]) - len(P[0])
    def check(start_i, start_ii):
        # if start_i >= bound_i or start_ii >= bound_ii :
        #     return False
        print("len",len(P), len(P[0]))
        for i in range(start_i, start_i+len(P)):
            for ii in range(start_ii, start_ii+len(P[0])):
                print(i,ii)
                if G[i][ii] != P[i-start_i][ii-start_ii] :
                    return False
        return True
    
    for i in range(bound_i+1) :
        for ii in range(bound_ii+1) :
            if check(i,ii) :
                return "YES" #True
    return "NO" #False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
