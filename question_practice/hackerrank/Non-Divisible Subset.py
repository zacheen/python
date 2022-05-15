#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    count = [0] * k
    for i in s:
        count[i % k] +=1
      
    ans_count = 0
    # 0
    ans_count += min(count[0], 1)
    
    # k//2
    if k % 2 == 0 :
        ans_count += min(count[k//2], 1)
        
    # other
    for i in range(1, math.ceil(k/2)):
        ans_count += max(count[i], count[k-i])
        
    return ans_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
