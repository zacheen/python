# 1254. Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands

from typing import List
from math import inf

# my 11ms Beats94.87%
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        i1_len = len(grid)-1
        i2_len = len(grid[0])-1

        dir_l = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i1,i2) :
            nonlocal res
            for d1,d2 in dir_l :
                nei1 = i1+d1
                nei2 = i2+d2
                if grid[nei1][nei2] == 0 :
                    if nei1 == 0 or nei1 == i1_len or nei2 == 0 or nei2 == i2_len :
                        res = 0
                    else :
                        grid[nei1][nei2] = 1
                        dfs(nei1,nei2)

        ans = 0
        for i1 in range(1,i1_len) :
            for i2 in range(1,i2_len) :
                if grid[i1][i2] == 0 :
                    res = 1
                    grid[i1][i2] = 1
                    dfs(i1,i2)
                    ans += res
        return ans



# given ans


s = Solution()
print("ans :",s.closedIsland([
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]])) # 
# print("ans :",s.closedIsland([
#                [1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]])) # 



