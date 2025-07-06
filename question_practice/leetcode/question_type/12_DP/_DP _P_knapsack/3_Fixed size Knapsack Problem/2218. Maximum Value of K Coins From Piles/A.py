# 2218. Maximum Value of K Coins From Piles
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

from typing import List
from math import inf
from functools import cache, lru_cache

# my modify from Fixed_Knap : 1424ms Beats99.14%
from itertools import accumulate
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0]+[0]*k # dp[i] 到現在取 i 個，最多可以拿多少
        for pile in piles :
            new_dp = dp.copy()
            for take_amo, total_coin in enumerate(accumulate(pile), 1) :
                for pre_i in range(k-take_amo, -1, -1) :
                    if (new_s := dp[pre_i]+total_coin) > new_dp[pre_i+take_amo] :
                        new_dp[pre_i+take_amo] = new_s
            dp = new_dp
        return dp[-1]

# my recursive : 3787ms Beats83.43%
from itertools import accumulate
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        piles = [list(accumulate(p, initial=0)) for p in piles]
        
        @lru_cache(None)
        def dp(pile_i, rem):
            if pile_i >= len(piles):
                return 0
            
            max_ret = 0
            now_acc = piles[pile_i]
            for take_n in range(min(len(now_acc)-1, rem),-1,-1) :
                max_ret = max(max_ret, dp(pile_i+1, rem-take_n) + now_acc[take_n] )
            return max_ret
    
        return dp(0, k)



s = Solution()
print(s.maxValueOfCoins(piles = [[1,100,3],[7,8,9]], k = 2))
print(s.maxValueOfCoins(piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7))
print(s.maxValueOfCoins(piles = [[1,1,1,1,1,1,700],[100],[100],[100],[100],[100],[100]], k = 7))
print(s.maxValueOfCoins(piles = [[100],[1,1,1,1,1,700],[100],[100],[100],[100],[100]], k = 7))
print(s.maxValueOfCoins([[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]],9))
print(s.maxValueOfCoins([[1,2,3],[1,2,3],[1,2,3]],3))

