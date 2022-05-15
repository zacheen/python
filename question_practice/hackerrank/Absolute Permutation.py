#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Write your code here
    if k == 0 :
        return list(range(1,n+1))
    
    # fast
    if n % (2*k) != 0 or n == k :
        return [-1]
    
    ans = list(range(1,n+1))
    for i in range(0,n,2*k):
        # i_k = i + k
        # i_kk = i + k + k
        # ans = ans[:i] + ans[i_k:i_kk] + ans[i:i_k] + ans[i_kk:]
        for ii in range(i,i+k):
            ans[ii], ans[ii+k] = ans[ii+k], ans[ii]
    return ans
    
    ## out of limit ##
    # bound = n+1
    # used = [True]*(bound+1)
    # def dp(now):
    #     nonlocal used
    #     if now == bound :
    #         return []
        
    #     # small num
    #     s = now - k
    #     if s > 0 and used[s] :
    #         used[s] = False
    #         ret = dp(now+1)
    #         if ret != -1 :
    #             return [s] + ret
    #         used[s] = False
        
    #     s = now + k
    #     if s <= n and used[s] :
    #         used[s] = False
    #         ret = dp(now+1)
    #         if ret != -1 :
    #             return [s] + ret
    #         used[s] = False
    #     return -1
    # ret = dp(1)
    # if ret == -1 :
    #     return [-1]
    # else :
    #     return ret
    #     # return "".join(str(x) for x in ret) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
