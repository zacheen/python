# classic
# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

from bisect import bisect_left
def lengthOfLIS(nums):
    stack = []
    for n in nums :
        if not stack or n > stack[-1] :
            stack.append(n)
        stack[bisect_left(stack,n)] = n
    return len(stack)

print(lengthOfLIS([10,9,2,5,3,7,101,18])) # [2,3,7,101]