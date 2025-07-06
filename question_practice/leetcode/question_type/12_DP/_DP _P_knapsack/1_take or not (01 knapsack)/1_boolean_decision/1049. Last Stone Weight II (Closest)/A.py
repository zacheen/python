# 1049. Last Stone Weight II
# https://leetcode.com/problems/last-stone-weight-ii/description/

from typing import List
from math import inf
from bisect import bisect_right

# my using template knapsack_01_reach v2 : 4ms Beats89.53%
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ = sum(stones)
        target = summ//2
        can_comb_set = {0}  # 裡面紀錄目前可以的組合
        for num in stones:
            can_comb_set |= set( new_s for s in can_comb_set if (new_s := s+num) <= target )
        max_comb = max(can_comb_set)
        return (summ-max_comb)-max_comb
    
# my using template knapsack_01_reach v1 : 5ms
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ = sum(stones)
        target = summ//2
        dp = [True] + [False]*(target)
        for num in stones:
            for pre_i in range(target-num, -1, -1): # 從大到小
                if dp[pre_i] :
                    dp[pre_i+num] = True
        for i in range(len(dp)-1, -1, -1) :
            if dp[i] :
                max_comb = i
                return (summ-max_comb)-max_comb

s = Solution()
print("ans :",s.lastStoneWeightII([2,7,4,1,8,1])) # 1
print("ans :",s.lastStoneWeightII([31,26,33,21,40])) # 5



