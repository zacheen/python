# 3429. Paint House IV
# https://leetcode.com/problems/paint-house-iv/description/

from typing import List
import functools

# my 1997ms Beats100.00%
from math import inf
class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        l = 0
        r = n-1
        dp = [[0]*3 for _ in range(3)]
        while r >= l :
            # move l : only have to follow adjacent : if i2 != dp_i
            new_dp = [[inf]*3 for _ in range(3)]
            for dp_i in range(3):
                for i1 in range(3):
                    min_cost = min(dp[i1][i2] for i2 in range(3) if i2 != dp_i)
                    new_dp[dp_i][i1] = min_cost + cost[l][dp_i]
            dp = new_dp
            l += 1
            if l > r :
                break

            # move r : have to follow adjacent and equidistant
            new_dp = [[inf]*3 for _ in range(3)]
            for dp_i in range(3):
                for i1 in range(3):
                    if i1 == dp_i : # follow equidistant
                        continue
                    for i2 in range(3):
                        if i2 == dp_i :
                            continue
                    min_cost = min(dp[i1][i2] for i2 in range(3) if i2 != dp_i)
                    new_dp[dp_i][i1] = min_cost + cost[r][dp_i]
            dp = new_dp
            r -= 1
        return min(dp[i][i2] for i in range(3) for i2 in range(3))

# given ans
# compare to No.1 mine is better

s = Solution()
print("ans :",s.minCost(n = 4, cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]])) # 9
print("ans :",s.minCost(n = 6, cost = [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]])) # 18



