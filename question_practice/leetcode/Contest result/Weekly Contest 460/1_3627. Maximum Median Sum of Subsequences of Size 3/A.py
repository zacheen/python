# 3627. Maximum Median Sum of Subsequences of Size 3
# https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3

from typing import List
from math import inf

# my 52ms Beats97.98%
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        # 盡量兩個大的搭配一個小的
        nums.sort(reverse = True)
        groups = len(nums)//3
        return sum(nums[1:groups*2+1:2])

s = Solution()
print("ans :",s.maximumMedianSum([2,1,3,2,1,3])) # 5
print("ans :",s.maximumMedianSum([1,1,10,10,10,10])) # 20
# print("ans :",s.maximumMedianSum()) # 

