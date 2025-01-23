# 1267. Count Servers that Communicate
# https://leetcode.com/problems/count-servers-that-communicate/description

from typing import List
import functools

# my 3ms Beats98.88%
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        @functools.lru_cache
        def check_str_only_one(i2):
            return 1 == sum(grid[i1][i2] for i1 in range(len(grid)))
        
        ans = 0
        for i1, l1 in enumerate(grid) :
            s = sum(l1)
            ans += s
            if s == 1 and check_str_only_one(l1.index(1)):
                ans -= 1
        return ans

# given ans : normal method
# count each row and col, if row or col count bigger than two, there must be an connection
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1

        return ans

s = Solution()
print("ans :",s.countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])) # 4



