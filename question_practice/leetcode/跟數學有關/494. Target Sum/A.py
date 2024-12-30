# 494. Target Sum
# https://leetcode.com/problems/target-sum/description

from typing import List
import functools

# my 116ms Beats78.15%
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        last_mem = {0:1}
        for n in nums :
            new_mem = defaultdict(lambda : 0)
            for last_sum, c in last_mem.items() :
                new_mem[last_sum+n] += c
                new_mem[last_sum-n] += c
            last_mem = new_mem
            # print(last_mem)
        return last_mem[target]
    
# my 35ms Beats91.49%
# sep left right version
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def get_sum_c(nums):
            last_mem = {0:1}
            for n in nums :
                new_mem = defaultdict(lambda : 0)
                for last_sum, c in last_mem.items() :
                    new_mem[last_sum+n] += c
                    new_mem[last_sum-n] += c
                last_mem = new_mem
            return last_mem
        
        mid = len(nums) // 2
        left = get_sum_c(nums[:mid])
        right = get_sum_c(nums[mid:])
        return sum( right[target-sum]*c for sum, c in left.items() )

# given ans 19ms Beats97.88%
# faster 1. only adding 2. only trace numbers between 1~(summ + target)//2
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        summ = sum(nums)
        # (summ + target) = 2(A + C + D + ...)
        if summ < abs(target) or (summ + target) % 2 == 1: 
            return 0

        # if the route is (A+B-C-D+E)
        # (A+B-C-D+E) + (A+B+C+D+E)(==sum) > 2(A+B+E)
        # so just find the solution of A+B+E
        def knapsack(nums: list[int], new_target: int) -> int:
            # dp[i] := the number of ways to sum to i by nums so far
            # 到 i 的每個數可以選擇要加或不加 (所以可以沿用原本的)
            dp = [0] * (new_target + 1)
            dp[0] = 1
            for num in nums:
                for i in range(new_target, num - 1, -1):
                    dp[i] += dp[i - num]
            return dp[new_target]
        
        return knapsack(nums, (summ + target) // 2)

s = Solution()
print("ans :",s.findTargetSumWays(nums = [1,1,1,1,1], target = 3)) # 5
print("ans :",s.findTargetSumWays(nums = [1], target = 1)) # 1
# print("ans :",s.findTargetSumWays()) # 



