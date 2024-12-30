# 3402. Minimum Operations to Make Columns Strictly Increasing
# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/description/

from typing import List
import functools

# my 3ms Beats100.00%
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        mem_last = [-1]*len(grid[0])
        ans_cou = 0
        for each_1D in grid :
            for i_2D, each_2D in enumerate(each_1D):
                if each_2D > mem_last[i_2D] :
                    mem_last[i_2D] = each_2D
                else :
                    mem_last[i_2D] += 1
                    ans_cou += mem_last[i_2D] - each_2D
        return ans_cou

# given ans
# change dir, so don't have to mem, but pulling val slower
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans_cou = 0
        for each_2D in range(len(grid[0])) :
            mem_last = -1
            for each_1D in range(len(grid)):
                mem_last = max(mem_last+1, grid[each_1D][each_2D])
                ans_cou += mem_last - grid[each_1D][each_2D]
        return ans_cou

s = Solution()
print("ans :",s.minimumOperations()) # 



