# 2017. Grid Game
# https://leetcode.com/problems/grid-game/description

from typing import List
import functools

# my 80ms Beats86.56%
from math import inf
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # 如果 robot1 在 indx i 往下走 
            # robot2 就得要從 第二行0~i 和 第一行 i+1~最後選一個走
        s1 = sum(grid[0])
        s2 = 0
        ans = inf
        for n1,n2 in zip(grid[0], grid[1]) :
            s1 -= n1
            ans = min(ans, max(s1, s2))
            s2 += n2
        return ans


# given ans
# same

s = Solution()
print("ans :",s.gridGame(grid = [[2,5,4],[1,5,1]])) # 4
print("ans :",s.gridGame(grid = [[3,3,1],[8,5,2]])) # 4
print("ans :",s.gridGame(grid = [[1,3,1,15],[1,3,3,1]])) # 7



