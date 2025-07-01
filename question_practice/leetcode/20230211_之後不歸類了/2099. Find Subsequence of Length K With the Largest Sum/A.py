# 2099. Find Subsequence of Length K With the Largest Sum
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum

from typing import List
from math import inf

# my 3ms Beats83.73%
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_i = [(n,i) for i, n in enumerate(nums)]
        nums_i.sort(reverse = True, key = lambda x : x[0])
        nums_i = nums_i[:k]
        nums_i.sort(key = lambda x : x[1])
        return [n for n,i in nums_i]

s = Solution()
print("ans :",s.maxSubsequence(nums = [2,1,3,3], k = 2)) # [3, 3]
print("ans :",s.maxSubsequence(nums = [-1,-2,3,4], k = 3)) # [-1, 3, 4]
print("ans :",s.maxSubsequence(nums = [3,4,3,3], k = 2)) # [3, 4] or [4, 3]



