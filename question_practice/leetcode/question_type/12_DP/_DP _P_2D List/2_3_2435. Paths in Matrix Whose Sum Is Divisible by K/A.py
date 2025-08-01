# 2435. Paths in Matrix Whose Sum Is Divisible by K
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description/

from typing import List
from math import inf
from itertools import accumulate
from collections import Counter

# my 1673ms Beats80.43%, 49.22MB Beats91.85%
MOD = 10**9+7
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp = []
        for n in accumulate(grid[0]) :
            dp.append(Counter([n%k]))

        for each_row in grid[1:]:
            for i, n in enumerate(each_row) :
                # up
                new_cnt = Counter({ ((rem+n)%k) : c for rem, c in dp[i].items() })
                # left
                if i != 0 :
                    for rem, c in dp[i-1].items() :
                        new_rem = (rem+n)%k
                        new_cnt[new_rem] = (new_cnt[new_rem] + c) % MOD
                # update
                dp[i] = new_cnt
        return dp[-1][0]

s = Solution()
print("ans :",s.numberOfPaths(grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3)) # 2
print("ans :",s.numberOfPaths(grid = [[0,0]], k = 5)) # 1
print("ans :",s.numberOfPaths(grid = [[1,1]], k = 5)) # 0
print("ans :",s.numberOfPaths(grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1)) # 10



