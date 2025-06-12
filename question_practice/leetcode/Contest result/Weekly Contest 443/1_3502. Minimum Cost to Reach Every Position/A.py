# 3502. Minimum Cost to Reach Every Position
# https://leetcode.com/problems/minimum-cost-to-reach-every-position/description/

from typing import List
from math import inf

# my 0ms
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []
        pre_c = cost[0]
        for c in cost :
            if c < pre_c :
                pre_c = c
            ans.append(pre_c)
        return ans

s = Solution()
print("ans :",s.minCosts([5,3,4,1,3,2])) # [5, 3, 3, 1, 1, 1]



