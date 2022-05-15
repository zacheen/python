# my 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    s_l = [c for c in w]
    
    # find the place that decline
    d_indx = None
    for i in range(len(s_l)-1, 0, -1):
        # print(s_l[i] , s_l[i-1])
        if s_l[i] > s_l[i-1] :
            d_indx = i-1
            break
    if d_indx == None :
        return "no answer"
    # print("d_indx", d_indx, s_l[d_indx])
            
    next_large = None
    next_large_i = None
    for i in range(d_indx+1, len(s_l)):
        if s_l[i] > s_l[d_indx] :
            if next_large == None or next_large > s_l[i] :
                next_large = s_l[i]
                next_large_i = i
    # print("next_large", next_large, next_large_i)
            
    s_l[d_indx] , s_l[next_large_i] = s_l[next_large_i], s_l[d_indx]
    back = s_l[d_indx+1:]
    back.sort()  # reverse ??
    # print(s_l[:d_indx+1], s_l[d_indx+1:])
    return "".join(s_l[:d_indx+1]+back)
            
if __name__ == '__main__':
    test_case = [
        "HEFG"
    ]

    for w in test_case:
        result = biggerIsGreater(w)
        print(result)

