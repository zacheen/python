# 827. Making A Large Island
# https://leetcode.com/problems/making-a-large-island/description

from typing import List
import functools

# my 756ms Beats84.50%
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n1_len = len(grid)
        n2_len = len(grid[0])
        dir_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cou_num = 2
        def dfs(n1, n2):
            s = grid[n1][n2] 
            grid[n1][n2] = cou_num
            for d1,d2 in dir_list: 
                nei1, nei2 = n1 + d1, n2 + d2
                if 0 <= nei1 < n1_len and 0 <= nei2 < n2_len and grid[nei1][nei2] == 1: 
                    s += dfs(nei1, nei2) 
            return s

        num_area = [0,0]
        for n1 in range(n1_len) :
            for n2 in range(n2_len) :
                if grid[n1][n2] == 1 :
                    ret = dfs(n1,n2)
                    if ret > 0 :
                        num_area.append(ret)
                        cou_num += 1

        max_sum = -1
        for n1 in range(n1_len) :
            for n2 in range(n2_len) :
                if grid[n1][n2] != 0 :
                    continue
                now_s = 0
                seen_set = set()
                for d1,d2 in dir_list :
                    nei_n1 = n1+d1
                    nei_n2 = n2+d2
                    if nei_n1 < 0 or nei_n2 < 0 or nei_n1 >= n1_len or nei_n2 >= n2_len :
                        continue
                    area_num = grid[nei_n1][nei_n2]
                    if area_num in seen_set : 
                        continue
                    seen_set.add(area_num)
                    now_s += num_area[area_num]
                max_sum = max(max_sum, now_s)
        return max_sum +1 if max_sum != -1 else n1_len*n2_len # +1 加上自己
                    
from collections import defaultdict
# given ans : 419ms Beats99.42%
    # sum area_num while dfs
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def explore_land(start): 
            queue = [start] # land cells to explore
            water = set() # all water cells connected to land
            area = 1 # total area of island

            while queue:
                i, j = queue.pop()
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj # adjacent cell to land
                    if 0 <= ni < m and 0 <= nj < n: # check if in bounds
                        if grid[ni][nj] == 1: # found land
                            grid[ni][nj] = -1 # set land to visited
                            queue.append((ni,nj)) 
                            area += 1 
                        elif grid[ni][nj] == 0: # found water
                            water.add((ni,nj))
            
            for cell in water: # add island area to water cells
                water_area[cell] += area

        m, n= len(grid), len(grid[0]) 
        water_area = defaultdict(int) # area for each water cell, (water cell): area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: # found unvisited land
                    grid[i][j] = -1 # set land to visited
                    explore_land((i,j))

        if water_area:
            return 1 + max(water_area.values()) # max land connected to water + 1 for water

        return 1 if grid[0][0] == 0 else m*n # edge case for if all cells are water or land

s = Solution()
print("ans :",s.largestIsland([[1,0],[0,1]])) # 3
print("ans :",s.largestIsland([[1,1],[1,0]])) # 4
print("ans :",s.largestIsland([[1,1],[1,1]])) # 4



