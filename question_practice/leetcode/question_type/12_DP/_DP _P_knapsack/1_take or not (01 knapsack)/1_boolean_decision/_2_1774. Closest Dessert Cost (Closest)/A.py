# 1774. Closest Dessert Cost
# https://leetcode.com/problems/closest-dessert-cost/description/

from typing import List
from math import inf
from bisect import bisect_left

# my using template knapsack_01_reach v2 : 2ms Beats99%
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        max_target = target*2 # since the number bigger than target*2 have a higher diff than 0 to target
        can_comb_set = set(baseCosts)  # 裡面紀錄目前可以的組合
        for num in toppingCosts:
            for _ in range(2) :
                can_comb_set |= set( new_s for s in can_comb_set if (new_s := s+num) <= max_target )
                if target in can_comb_set:
                    return target
        return min((abs(target-n), n) for n in can_comb_set)[1]

from functools import cache
# given ans : 10ms
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        close = min(baseCosts)

        @cache
        def dfs(index, curr):
            nonlocal close
            if abs(target - close) >= abs(target - curr):
                if curr > close and abs(target - close) == abs(target - curr):
                    return
                close = curr

            if curr > target:
                return

            if index >= len(toppingCosts):
                return

            dfs(index + 1, curr)
            dfs(index + 1, curr + toppingCosts[index])
            dfs(index + 1, curr + toppingCosts[index] * 2)

        for baseCost in baseCosts:
            dfs(0, baseCost)
        return close

s = Solution()
print("ans :",s.closestCost(baseCosts = [1,7], toppingCosts = [3,4], target = 10)) # 10
print("ans :",s.closestCost(baseCosts = [2,3], toppingCosts = [4,5,100], target = 18)) # 17
print("ans :",s.closestCost(baseCosts = [3,10], toppingCosts = [2,5], target = 9)) # 8



