# 3360. Stone Removal Game
# https://leetcode.com/problems/stone-removal-game/description/

from typing import List
import functools

# my 0ms Beats100.00%
class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans = False
        for i in range(10,-1,-1) :
            if n < i :
                return ans
            n = n-i
            ans = not ans
        return None

s = Solution()
print("ans :",s.canAliceWin())



