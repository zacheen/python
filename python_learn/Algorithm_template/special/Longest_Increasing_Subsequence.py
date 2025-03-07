# Longest_Increasing_Subsequence
from bisect import bisect_left, bisect_right
from math import inf

# classic # 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
def LIS(nums):
    stack = [inf]
    for n in nums :
        if n > stack[-1] :
            stack.append(n)
        else :
            stack[bisect_left(stack,n)] = n
    return len(stack)

print(LIS([10,9,2,102,2,7,101,18])) # 3

# classic # 2826. Sorting Three Groups
# https://leetcode.com/problems/sorting-three-groups/description/
def LIS_nonstrict(nums):
    stack = [inf]
    for n in nums :
        if n >= stack[-1] :
            stack.append(n)
        else :
            stack[bisect_right(stack,n)] = n
    return len(stack)

print(LIS_nonstrict([10,9,2,102,2,7,101,18])) # 4

def LIS_with_list(nums):
    stack = [inf]
    max_l = []
    for n in nums :
        if n > stack[-1] :
            stack.append(n)
            max_l = stack[:]
        else :
            stack[bisect_left(stack,n)] = n
    return len(stack), max_l

print(LIS_with_list([10,9,2,5,3,7,101,18])) # 4, [2,3,7,101]
