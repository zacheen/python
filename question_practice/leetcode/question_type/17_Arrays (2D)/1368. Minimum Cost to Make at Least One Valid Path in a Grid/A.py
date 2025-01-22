# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description

from typing import List
from itertools import pairwise

# my (using seen to mem last round) : 91ms Beats90.58%
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        max_1D = len(grid)
        max_2D = len(grid[0])
        four_dir = [0,-1,0,1,0]
        def dfs(i1, i2):
            if i1 < 0 or i1 >= max_1D or i2 < 0 or i2 >= max_2D :
                return 
            while grid[i1][i2] > 0 :
                direct = grid[i1][i2]
                grid[i1][i2] = 0
                for d1,d2 in pairwise(four_dir) :
                    next_seen.add((i1+d1,i2+d2))
                if direct == 1 :
                    i2 += 1
                    if i2 == max_2D :
                        return
                elif direct == 2 :
                    i2 -= 1
                    if i2 == -1 :
                        return
                elif direct == 3 :
                    i1 += 1
                    if i1 == max_1D :
                        return
                elif direct == 4 :
                    i1 -= 1
                    if i1 == -1 :
                        return
        
        seen = {(0,0)}
        cou = 0
        while True :
            next_seen = set()
            for i1, i2 in seen :
                dfs(i1, i2)
            if grid[-1][-1] <= 0 :
                return cou
            seen = next_seen
            cou += 1

# # my (using cou to mem last round) : 567ms Beats5.19%
# class Solution:
#     def minCost(self, grid: List[List[int]]) -> int:
#         max_1D = len(grid)
#         max_2D = len(grid[0])
#         max_1D_m1 = max_1D-1
#         max_2D_m1 = max_2D-1
#         cou = 0
#         def dfs(i1, i2):
#             while grid[i1][i2] > 0 :
#                 direct = grid[i1][i2]
#                 grid[i1][i2] = cou-1
#                 if direct == 1 :
#                     i2 += 1
#                     if i2 == max_2D :
#                         return
#                 elif direct == 2 :
#                     i2 -= 1
#                     if i2 == -1 :
#                         return
#                 elif direct == 3 :
#                     i1 += 1
#                     if i1 == max_1D :
#                         return
#                 elif direct == 4 :
#                     i1 -= 1
#                     if i1 == -1 :
#                         return

#         def check_nearby(i1, i2):
#             # up
#             if i1 > 0 :
#                 if grid[i1-1][i2] == cou :
#                     return True
#             # down
#             if i1 < max_1D_m1 :
#                 if grid[i1+1][i2] == cou :
#                     return True
#             # left
#             if i2 > 0 :
#                 if grid[i1][i2-1] == cou :
#                     return True
#             # right
#             if i2 < max_2D_m1 :
#                 if grid[i1][i2+1] == cou :
#                     return True
#             return False    

#         dfs(0,0)
        
#         while True :
#             if grid[-1][-1] <= 0 :
#                 return -cou
#             cou-=1
#             for i1 in range(max_1D) :
#                 for i2 in range(max_2D) :
#                     if grid[i1][i2] > 0 and check_nearby(i1, i2):
#                         dfs(i1, i2)


# given ans
# same as "seen" concept

s = Solution()
print("ans :",s.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])) # 3
print("ans :",s.minCost([[1,1,3],[3,2,2],[1,1,4]])) # 0
print("ans :",s.minCost([[1,2],[4,3]])) # 1



