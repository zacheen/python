# 3459. Length of Longest V-Shaped Diagonal Segment
# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/description/
    # clockwise 90-degree !! 只能向右轉

from typing import List
from math import inf
from functools import cache

# my 4652ms Beats68.56%
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # 每個點的四個方向
        dir_d = [(1,1),(1,-1),(-1,-1),(-1,1)]
        len_c1 = len(grid)
        len_c2 = len(grid[0])
        
        @cache
        def dfs(now_c1, now_c2, dire, rem_t, st):
            if 0 <= now_c1 < len_c1 and 0 <= now_c2 < len_c2 and grid[now_c1][now_c2] == st:
                # keep dir
                d1,d2 = dir_d[dire]
                next1 = now_c1 + d1
                next2 = now_c2 + d2
                ret = dfs(next1, next2, dire, rem_t, 2 if st != 2 else 0) + 1
                
                # change dir
                if rem_t :
                    # 有重疊一格 所以不用再加一
                    ret = max( ret, dfs(now_c1, now_c2, (dire+1)%4, 0, st) )
                    # ret = max( ret, dfs(now_c1, now_c2, (dire-1)%4, 0, st) ) # only clockwise !!
                return ret
            return 0
        
        ans = 0
        for c1, l in enumerate(grid):
            for c2, num in enumerate(l) :
                if num == 1 :
                    for new_di in range(4) :
                        ans = max(ans, dfs(c1,c2,new_di,1,1))
        dfs.cache_clear()
        return ans

# given ans : 4050ms Beats85.26%
# same concept different implement method
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        @cache
        def dp(row,col, dr,dc, element, hasTurned):
            if not (0 <= row < m and 0 <= col < n) or grid[row][col] != element:
                return 0
            
            ret = dp(row + dr, col + dc, dr, dc, element^2, hasTurned)
            if hasTurned: return ret + 1

            length = dp(row + dc, col - dr, dc, -dr, element^2, True)
            return max(ret,length) + 1 

        m, n = len(grid), len(grid[0])
        ans, dr, dc = 0, 1, 1
 
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    for _ in range(4):
                        dr, dc = -dc, dr
                        vee = dp(row + dr, col + dc, dr, dc, 2, False)+1
                        ans = max(ans, vee)
        return ans

s = Solution()
print("ans :",s.lenOfVDiagonal([[2,2,1,2,2],
                                [2,0,2,2,0],
                                [2,0,1,1,0],
                                [1,0,2,2,2],
                                [2,0,0,2,2]])) # 5
print("ans :",s.lenOfVDiagonal([[2,2,2,2,2],
                                [2,0,2,2,0],
                                [2,0,1,1,0],
                                [1,0,2,2,2],
                                [2,0,0,2,2]])) # 4
print("ans :",s.lenOfVDiagonal([[1,2,2,2,2],
                                [2,2,2,2,0],
                                [2,0,0,0,0],
                                [0,0,2,2,2],
                                [2,0,0,2,0]])) # 5
print("ans :",s.lenOfVDiagonal([[1]])) # 1
print("ans :",s.lenOfVDiagonal([[1,1,1,2,0,0],
                                [0,0,0,0,1,2]])) # 



