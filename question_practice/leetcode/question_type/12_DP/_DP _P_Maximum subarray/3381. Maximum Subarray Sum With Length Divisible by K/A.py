# 3381. Maximum Subarray Sum With Length Divisible by K
# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/description/

from typing import List
import functools

# my 
import math
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        max_ans = -math.inf
        min_pre_sum = [math.inf]*(k-1) + [0] # 剛好被k整除是可以不取的
        now_sum = 0
        for i, num in enumerate(nums):
            now_sum += num
            i_mod_k = i%k
            # 最大的 subarray_sum = now_sum - 相對位置的最小 subarray_sum
            max_ans = max(max_ans, now_sum-min_pre_sum[i_mod_k])
            min_pre_sum[i_mod_k] = min(min_pre_sum[i_mod_k], now_sum)
        return max_ans

s = Solution()
# print(s.maxSubarraySum(nums = [1,2], k = 1)) # 3
print(s.maxSubarraySum(nums = [-1,-2,-3,-4,-5], k = 4)) # -10
# print(s.maxSubarraySum(nums = [-5,1,2,-3,4], k = 2)) # 4



