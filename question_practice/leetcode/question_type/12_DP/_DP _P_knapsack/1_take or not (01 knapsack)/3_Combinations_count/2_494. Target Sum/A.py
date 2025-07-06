# 494. Target Sum
# https://leetcode.com/problems/target-sum/description

from typing import List
import functools

# my using template v1: 19ms Beats95.07%
def knapsack_01_comb(nums, target):
    dp = [1]+[0]*(target)
    for num in nums:
        for fut_i in range(target, num-1, -1):
            dp[fut_i] += dp[fut_i-num]
    return dp[target]

# my using template v2: 27ms Beats87.73%
def knapsack_01_comb(nums, target):
    mem = defaultdict(int)
    mem[0] = 1
    for num in nums:
        for s, cnt in mem.copy().items() :
            mem[s+num] += cnt
    return mem[target]

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        summ = sum(nums)
        # (summ + target) = 2(A + C + D + ...)
        if summ < abs(target) or (summ + target) % 2 == 1: 
            return 0

        # if the route is (A+B-C-D+E)
        # (A+B-C-D+E) + (A+B+C+D+E)(==sum) > 2(A+B+E)
        # so just find the solution of A+B+E
        return knapsack_01_comb(nums, (summ+target) // 2)

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

s = Solution()
print("ans :",s.findTargetSumWays(nums = [1,1,1,1,1], target = 3)) # 5
print("ans :",s.findTargetSumWays(nums = [1], target = 1)) # 1
# print("ans :",s.findTargetSumWays()) # 



