# 1774. Closest Dessert Cost
# https://leetcode.com/problems/closest-dessert-cost/description/

from typing import List
from math import inf
from bisect import bisect_left

# my 51ms Beats71.11%
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        can_comb_set = {0}  # 裡面紀錄目前可以的組合
        for num in toppingCosts*2:
            can_comb_set |= set( s + num for s in can_comb_set )
        
        poss_top = list(can_comb_set)
        poss_top.sort()
        poss_top = [-inf] + poss_top + [inf]
        min_diff = inf
        act_cost = inf
        for cup in baseCosts :
            t = target-cup
            ret_i = bisect_left(poss_top, t)
            # right num
            di = poss_top[ret_i]-t
            if di < min_diff :
                min_diff = di
                act_cost = target + di
            # left num
            di = poss_top[ret_i-1]-t
            if abs(di) <= min_diff :
                min_diff = abs(di)
                act_cost = target + di

            if act_cost == target :
                return target

        return act_cost

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



