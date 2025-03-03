# 1931. Painting a Grid With Three Different Colors
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/description/

from typing import List
from functools import lru_cache

# given ans
class Solution:  # 812 ms, faster than 66.67%
    def colorTheGrid(self, m: int, n: int) -> int:
        def getColor(mask, pos):  # Get color of the `mask` at `pos`, use 2 bits to store a color
            return (mask >> (2 * pos)) & 3
        
        def setColor(mask, pos, color):  # Set `color` to the `mask` at `pos`, use 2 bits to store a color
            return mask | (color << (2 * pos))

        def dfs(r, curColMask, prevColMask, out):
            if r == m:  # Filled full color for this column
                out.append(curColMask)
                return
            for i in [1, 2, 3]:  # Try colors i in [1=RED, 2=GREEN, 3=BLUE]
                if getColor(prevColMask, r) != i and (r == 0 or getColor(curColMask, r - 1) != i):
                    dfs(r + 1, setColor(curColMask, r, i), prevColMask, out)

        @lru_cache(None)
        def neighbor(prevColMask):  # Generate all possible columns we can draw, if the previous col is `prevColMask`
            out = []
            dfs(0, 0, prevColMask, out)
            return out

        @lru_cache(None)
        def dp(c, prevColMask):
            if c == n: return 1  # Found a valid way
            ans = 0
            for nei in neighbor(prevColMask):
                ans = (ans + dp(c + 1, nei)) % 1_000_000_007
            return ans
        return dp(0, 0)

s = Solution()
print("ans :",s.colorTheGrid(m = 1, n = 2)) # 6
print("ans :",s.colorTheGrid(m = 2, n = 2)) # 18



