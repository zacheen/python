# 2787. Ways to Express an Integer as Sum of Powers
# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers

from typing import List
from math import inf
from collections import defaultdict
MOD = 10**9+7

# my using template knapsack_01_comb v1 : 234ms Beats94.49%
def knapsack_01_comb(nums, target):
    dp = [1]+[0]*(target)
    for num in nums:
        for fut_i in range(target, num-1, -1):
            dp[fut_i] += dp[fut_i-num]
    return dp[target]

# my using template knapsack_01_comb v2 : 507ms Beats61.81%
def knapsack_01_comb(nums, target):
    mem = defaultdict(int)
    mem[0] = 1
    for num in nums:
        for s, cnt in mem.copy().items() :
            if (new_s := s+num) <= target :
                mem[new_s] += cnt
    return mem[target]

class Solution:
    def numberOfWays(self, target: int, x: int) -> int:
        nums = []
        now_n = 1
        while (poss_n := now_n**x) <= target :
            nums.append(poss_n)
            now_n += 1
        return knapsack_01_comb(nums, target) % MOD

s = Solution()
print("ans :",s.numberOfWays(10, 2)) # 1
print("ans :",s.numberOfWays(4, 1)) # 2
# print("ans :",s.numberOfWays()) # 



