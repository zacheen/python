# classic
# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

from bisect import bisect_left

def LIS(nums):
    stack = []
    for n in nums :
        if not stack or n > stack[-1] :
            stack.append(n)
        stack[bisect_left(stack,n)] = n
    return len(stack)

print(LIS([10,9,2,5,3,7,101,18])) # 4, [2,3,7,101]

def LIS_with_list(nums):
    stack = []
    max_l = []
    for n in nums :
        if not stack or n > stack[-1] :
            stack.append(n)
            max_l = stack[:]
        stack[bisect_left(stack,n)] = n
    return len(stack), max_l

print(LIS_with_list([10,9,2,5,3,7,101,18])) # 4, [2,3,7,101]
