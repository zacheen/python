# 3584. Maximum Product of First and Last Elements of a Subsequence
# https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

from typing import List
from math import inf

# my 168ms Beats96.05%
class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        if m == 1 : 
            return max(max(nums), -min(nums))**2
        
        max1 = nums[0]
        min1 = nums[0]
        ans = -inf
        for pre_n, now_n in zip(nums, nums[m-1:]) :
            max1 = max(max1, pre_n)
            min1 = min(min1, pre_n)
            if now_n >= 0 :
                ans = max(ans, now_n*max1)
            else :
                ans = max(ans, now_n*min1)
        return ans

s = Solution()
print("ans :",s.maximumProduct(nums = [-1,-9,2,3,-2,-3,1], m = 1)) # 81
print("ans :",s.maximumProduct(nums = [1,3,-5,5,6,-4], m = 3)) # 20 (5*6 太近無法)
print("ans :",s.maximumProduct(nums = [2,-1,2,-6,5,2,-5,7], m = 2)) # 35



