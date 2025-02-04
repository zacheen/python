# 2658. Maximum Number of Fish in a Grid
# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description

from typing import List
import functools

from itertools import pairwise
# my 84ms Beats10.45%
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dir_list = [0,1,0,-1,0]
        n1_len = len(grid)
        n2_len = len(grid[0])
        def dfs(n1,n2):
            if 0 <= n1 < n1_len and 0 <= n2 < n2_len and grid[n1][n2] != 0:
                s = grid[n1][n2]
                grid[n1][n2] = 0
                return s + sum(dfs(n1+d1,n2+d2) for d1,d2 in pairwise(dir_list))
            return 0
        return max(dfs(n1,n2) for n1 in range(n1_len) for n2 in range(n2_len))

# given ans : 31ms Beats86.26%
# concept is the same, but speed varies
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n1_len = len(grid)
        n2_len = len(grid[0])
        dir_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(n1, n2):
            s = grid[n1][n2] 
            grid[n1][n2] = 0
            for d1,d2 in dir_list: 
                nei1, nei2 = n1 + d1, n2 + d2
                if 0 <= nei1 < n1_len and 0 <= nei2 < n2_len and grid[nei1][nei2] != 0: 
                    s += dfs(nei1, nei2) 
            return s
        return max([dfs(i1, i2) for i1 in range(n1_len) for i2 in range(n2_len) if grid[i1][i2] != 0] + [0])

s = Solution()
print("ans :",s.findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]])) # 7
print("ans :",s.findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])) # 1
print("ans :",s.findMaxFish([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])) # 0
