# 3661. Maximum Walls Destroyed by Robots
# https://leetcode.com/problems/maximum-walls-destroyed-by-robots

from typing import List
from math import inf
from bisect import bisect_left, bisect_right
from functools import cache

# my v2 (for version) 815ms Beats90.73%
max = lambda x, y : x if x > y else y
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        s_wall = set(walls)
        def_wall = set(robots) & s_wall
        rem_wall = sorted(s_wall - def_wall)

        def query_cnt(left, right): 
            if left >= right :
                return 0
            # count walls in [left, right]
            return bisect_right(rem_wall, right) - bisect_left(rem_wall, left)
        
        robots_list = sorted( list((r,d) for r,d in zip(robots, distance)) )
        robots_list.insert(0, (-10**9-2, 0)) # dummy
        robots_list.append((10**9+2, 0)) # dummy
        robots = list(n1 for n1,n2 in robots_list)

        final_r = 0
        max_left = 0  # 此點若是向左射 最多面牆的結果
        max_right = 0 # 此點若是向右射 最多面牆的結果
        
        for i in range(1, len(robots_list)-1):
            r,d = robots_list[i]
            min_left = r-d
            new_final_r = r+d
            add_wall = query_cnt(r, min(new_final_r, robots[i+1]))
            max_left, max_right = \
            max(
                max_left + query_cnt(max(robots[i-1], min_left), r),
                max_right + query_cnt(max(final_r, min_left), r)
            ), \
            max(max_left, max_right) + add_wall
            final_r = new_final_r+1
        return max(max_left, max_right) + len(def_wall)

# my 1417ms Beats30.58%
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        s_wall = set(walls)
        def_wall = set(robots) & s_wall
        rem_wall = list(s_wall - def_wall)
        rem_wall.sort()
        
        robots_list = sorted( list((r,d) for r,d in zip(robots, distance)) )
        robots_list.insert(0, (-10**9-2, 0)) # dummy
        robots_list.append((10**9+2, 0)) # dummy
        robots_list.append((10**9+2, 0)) # dummy

        def query_cnt(left, right): 
            if left >= right :
                return 0
            # count walls in [left, right]
            return bisect_right(rem_wall, right) - bisect_left(rem_wall, left)
        
        @cache
        def dp(r_i, dir): # dir 0-left, 1-right
            if r_i == 0 :
                return 0
            
            if dir == 0 :
                min_left = robots_list[r_i][0]-robots_list[r_i][1]
                return max(
                    dp(r_i-1, 0) + query_cnt(max(robots_list[r_i-1][0]+1                       , min_left), robots_list[r_i][0]),
                    dp(r_i-1, 1) + query_cnt(max(robots_list[r_i-1][0]+robots_list[r_i-1][1]+1 , min_left), robots_list[r_i][0])
                )
            else :
                add_wall = query_cnt(robots_list[r_i][0], min(robots_list[r_i][0]+robots_list[r_i][1], robots_list[r_i+1][0]))
                return max(dp(r_i-1, 0), dp(r_i-1, 1)) + add_wall
        
        return max(dp(len(robots_list)-2, 0), dp(len(robots_list)-2, 1)) + len(def_wall)

s = Solution()
print("ans :",s.maxWalls(robots = [4], distance = [3], walls = [1,10])) # 1
print("ans :",s.maxWalls(robots = [10,2], distance = [5,1], walls = [5,2,7])) # 3
print("ans :",s.maxWalls(robots = [1,2], distance = [100,1], walls = [10])) # 0
print("ans :",s.maxWalls(robots = [3, 4, 8, 9, 10, 11], 
                         distance = [5, 9, 3, 5, 3, 5], 
                         walls = [6, 9])) # 2
print("ans :",s.maxWalls(robots = [3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 17, 23, 26, 30, 32, 34, 36, 37, 39, 40, 42, 43, 44, 45, 53, 55, 56, 57, 58, 60, 61, 63, 66, 69, 70, 72, 73, 74], 
                         distance = [5, 9, 3, 5, 3, 5, 5, 8, 3, 9, 4, 7, 2, 6, 4, 2, 9, 7, 3, 4, 1, 5, 2, 8, 5, 5, 7, 1, 8, 9, 7, 8, 4, 4, 5, 7, 6, 6], 
                         walls = [6, 20, 21, 22, 28, 41, 50, 52, 75])) # 9

