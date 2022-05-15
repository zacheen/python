#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    
    # up and down
    total = len(A)*len(A[0])*2
    
    for i in range(len(A)) :
        now_height = None
        for ii in range(len(A[0])) :
            if now_height == None :
                now_height = A[i][ii]
                total += now_height
            else :
                new_h = A[i][ii]
                total += abs(new_h-now_height)
                now_height = new_h
        # print("last height", now_height)
        total += now_height
                
    for ii in range(len(A[0])) :        
        now_height = None
        for i in range(len(A)) :
            if now_height == None :
                now_height = A[i][ii]
                total += now_height
            else :
                new_h = A[i][ii]
                total += abs(new_h-now_height)
                now_height = new_h
        # print("last height", now_height)
        total += now_height
            
    return total
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
