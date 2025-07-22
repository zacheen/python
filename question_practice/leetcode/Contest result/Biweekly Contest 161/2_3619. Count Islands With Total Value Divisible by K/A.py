# 3619. Count Islands With Total Value Divisible by K
# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/description/

from typing import List
from math import inf

# my 317ms Beats61.95%
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        dir_list = [(0,1),(1,0),(0,-1),(-1,0)]
        max_i1 = len(grid)
        max_i2 = len(grid[0])
        def dfs(i1,i2) :
            ret_sum = grid[i1][i2]
            if ret_sum == 0 :
                return 0
            grid[i1][i2] = 0
            for d1, d2 in dir_list :
                new_i1 = i1 + d1
                if 0 > new_i1 or new_i1 >= max_i1 :
                    continue
                new_i2 = i2 + d2
                if 0 > new_i2 or new_i2 >= max_i2 :
                    continue
                ret_sum += dfs(new_i1, new_i2)
            return ret_sum

        ans_cnt = 0
        for i1 in range(max_i1) :
            for i2 in range(max_i2) :
                if grid[i1][i2] :
                    if dfs(i1,i2) % k == 0 :
                        ans_cnt += 1
        return ans_cnt

s = Solution()
print("ans :",s.countIslands(grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5)) # 2
print("ans :",s.countIslands(grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3)) # 6

