# reduce
    # 使用 operator : 比較快
    # 使用 lambda   : 比較慢

import time
from random import randint
from bisect import bisect_left
max_n = 5000000
nums = list(randint(0,max_n) for _ in range(max_n))

start = time.time()
def lengthOfLIS(nums):
    stack = []
    for n in nums :
        if not stack or n > stack[-1] :
            stack.append(n)
        else :
            stack[bisect_left(stack,n)] = n
    return len(stack)
ret = lengthOfLIS(nums)
end = time.time()
print("1 :", ret, end - start) # 


start = time.time()
def lengthOfLIS(nums):
    stack = []
    for n in nums :
        if not stack or n > stack[-1] :
            stack.append(n)
        stack[bisect_left(stack,n)] = n
    return len(stack)
ret = lengthOfLIS(nums)
end = time.time()
print("2 :", ret, end - start) # 

start = time.time()
def lengthOfLIS(nums):
    stack = []
    for n in nums :
        ret_indx = bisect_left(stack,n)
        if ret_indx == len(stack) :
            stack.append(n)
        else :
            stack[ret_indx] = n
    return len(stack)
ret = lengthOfLIS(nums)
end = time.time()
print("3 :", ret, end - start) # 