# 778. Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water

from typing import List
from math import inf
from bisect import bisect_left

# my 
dir_list = [(1,0),(0,1),(-1,0),(0,-1)]
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        end_n1 = len(grid)-1
        end_n2 = len(grid[0])-1
        def check_can_reach(water_hei):
            # optimization
            if water_hei < max(grid[end_n1][end_n2], grid[0][0]) :
                return False
            # check corner case
            if end_n1 == 0 and end_n2 == 0 :
                return True
            
            seen_grid = [[0]*len(grid[0]) for _ in range(len(grid))]
            # 0 : not yet, 
            stack = [(0,0)]

            while stack :
                n1,n2 = stack.pop()
                if seen_grid[n1][n2] :
                    continue
                seen_grid[n1][n2] = True
                

                for d1,d2 in dir_list :
                    new1 = n1+d1
                    new2 = n2+d2
                    if new1 < 0 or new1 > end_n1 or new2 < 0 or new2 > end_n2 :
                        continue
                    if grid[new1][new2] > water_hei :
                        continue
                    if new1 == end_n1 and new2 == end_n2 :
                        return True
                    stack.append((new1,new2))
            return False

        return bisect_left(range(len(grid)**2+1), True, key=check_can_reach)


            



s = Solution()
print("ans :",s.swimInWater(grid = [[0,2],[1,3]])) # 3
print("ans :",s.swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])) # 16
print("ans :",s.swimInWater([[3,2],[0,1]])) # 3
print("ans :",s.swimInWater([[0]])) # 0



