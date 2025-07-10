# 3603. Minimum Cost Path with Alternating Directions II
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/description/

from typing import List
from math import inf

# my 334ms Beats99.96%
class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [0]+[inf]*(n)
        for i, li in enumerate(waitCost, 1) :
            for j, c in enumerate(li, 1) :
                dp[j] = min(dp[j], dp[j-1]) + c + (i*j) # min(從上面來 從左邊來)
            dp[0] = inf
        return dp[-1] - waitCost[0][0] - waitCost[-1][-1] # 減去初始 跟 最後一格的 cost

s = Solution()
print("ans :",s.minCost(m = 1, n = 2, waitCost = [[1,2]])) # 3
print("ans :",s.minCost(m = 2, n = 2, waitCost = [[3,5],[2,4]])) # 9
print("ans :",s.minCost(m = 2, n = 3, waitCost = [[6,1,4],[3,2,5]])) # 16



