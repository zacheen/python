# 1594. Maximum Non Negative Product in a Matrix
# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/

from typing import List
from math import inf

# my 3ms Beats95.94%
MOD = 10**9+7
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        len_n2 = len(grid[0])
        mem = [[-1, 1] for _ in range(len_n2)] # [max, min]
        mem[0][0] = 1
        for i1, l in enumerate(grid) :
            for i2, n in enumerate(l) :
                # from top
                pre_max, pre_min = mem[i2]
                
                # from left
                if i2 != 0 :
                    pre_max = max(pre_max, mem[i2-1][0])
                    pre_min = min(pre_min, mem[i2-1][1])

                if n < 0 :
                    mem[i2] = (pre_min*n, pre_max*n)
                else :
                    mem[i2] = (pre_max*n, pre_min*n)
        if (a:=mem[-1][0]) < 0 :
            return -1
        else :
            return a%MOD

s = Solution()
print("ans :",s.maxProductPath(
    [[-1,-2,-3],
     [-2,-3,-3],
     [-3,-3,-2]])) # -1
print("ans :",s.maxProductPath(
    [[1,-2,1],
     [1,-2,1],
     [3,-4,1]])) # 8
print("ans :",s.maxProductPath(
    [[1,3],
     [0,-4]])) # 0



