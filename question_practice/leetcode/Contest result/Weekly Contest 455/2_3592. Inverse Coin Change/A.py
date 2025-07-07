# 3592. Inverse Coin Change
# https://leetcode.com/problems/inverse-coin-change/description/

from typing import List
from math import inf
from collections import deque

# my 4ms Beats90.49%
class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        len_n = len(numWays)
        dp = [1]+[0]*(len_n)
        ans = []
        for coin, n_ways in enumerate(numWays, 1) :
            if dp[coin] != n_ways :
                for fut_i in range(coin, len(dp)):
                    dp[fut_i] += dp[fut_i-coin]
                if dp[coin] != n_ways :
                    return []
                ans.append(coin)
        return ans

s = Solution()
print("ans :",s.findCoins([0,1,0,2,0,3,0,4,0,5])) # [2, 4, 6]
print("ans :",s.findCoins([1,2,2,3,4])) # [1, 2, 5]
print("ans :",s.findCoins([1,2,3,4,15])) # []



