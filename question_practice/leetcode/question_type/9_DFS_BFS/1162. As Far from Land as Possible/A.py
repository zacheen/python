# 1162. As Far from Land as Possible
# https://leetcode.com/problems/as-far-from-land-as-possible/description/

# my practice again : 193ms Beats47.27%
from itertools import pairwise
class Solution:
    def maxDistance(self, grid):
        bfs_list = []
        for i1, l in enumerate(grid):
            for i2, n in enumerate(l) :
                if n == 1 : 
                    bfs_list.append((i1,i2))
                    grid[i1][i2] = 0
        
        cou = 0
        n1_len = len(grid)
        n2_len = len(grid[0])
        dir_list = [0,1,0,-1,0]
        while bfs_list :
            new_bfs_list = []
            for n1,n2 in bfs_list :
                if n1 < 0 or n1 >= n1_len or n2 < 0 or n2 >= n2_len or grid[n1][n2] == 1:
                    continue
                grid[n1][n2] = 1
                for d1, d2 in pairwise(dir_list) :
                    new_bfs_list.append((n1+d1,n2+d2))
            bfs_list = new_bfs_list
            cou += 1
        cou -= 2
        if cou <= 0 :
            return -1
        else :
            return cou

# given ans : 145ms Beats66.41%
import collections
class Solution:
    def maxDistance(self, grid):
        m = len(grid)
        n = len(grid[0])
        dirs = [0, 1, 0, -1, 0]
        q = collections.deque()
        water = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    water += 1
                else:
                    q.append((i, j))

        if water == 0 or water == m * n:
            return -1

        ans = 0
        d = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                ans = d
                for k in range(4):
                    x = i + dirs[k]
                    y = j + dirs[k + 1]
                    if x < 0 or x == m or y < 0 or y == n:
                        continue
                    if grid[x][y] > 0:
                        continue
                    q.append((x, y))
                    grid[x][y] = 2  # Mark as visited.
            d += 1
        return ans

s = Solution()
print(s.maxDistance([[1,0,1],[0,0,0],[1,0,1]])) # 2
print(s.maxDistance([[1,0,0],[0,0,0],[0,0,0]])) # 4
print(s.maxDistance([[0,0,0],[0,0,0],[0,0,0]])) # -1
print(s.maxDistance([[1,1,1],[1,1,1],[1,1,1]])) # -1

