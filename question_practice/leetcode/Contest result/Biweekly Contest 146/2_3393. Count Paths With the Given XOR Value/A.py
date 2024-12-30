# 3393. Count Paths With the Given XOR Value
# https://leetcode.com/problems/count-paths-with-the-given-xor-value/description/

from typing import List
import functools

# # my 951ms Beats99.03%
# class Solution:
#     def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
#         mod = 10**9 + 7
#         last_mem = [[0]*16 for _ in range(len(grid[0]))]
#         for D1 in range(len(grid)) :
#             new_mem = [[0]*16 for _ in range(len(grid[0]))]
#             for D2 in range(len(grid[0])) :
#                 if D2 == 0 :
#                     if D1 == 0:
#                         new_mem[0][grid[D1][D2]] = 1
#                     else :
#                         for i in range(16) :
#                             new_mem[D2][(i^grid[D1][D2])] = last_mem[D2][i]
#                             new_mem[D2][(i^grid[D1][D2])] %= mod
#                 else :
#                     for i in range(16) :
#                         new_mem[D2][(i^grid[D1][D2])] = last_mem[D2][i] + new_mem[D2-1][i]
#                         new_mem[D2][(i^grid[D1][D2])] %= mod
#             last_mem = new_mem
#         return last_mem[-1][k]

# my shorten 757ms Beats99.81%
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7
        last_mem = {indx_D2:[0]*16 for indx_D2 in range(-1,len(grid[0]))}
        last_mem[0][0] = 1 # top left init
        for D1 in range(len(grid)) :
            new_mem = {indx_D2:[0]*16 for indx_D2 in range(-1,len(grid[0]))}
            for D2 in range(len(grid[0])) :
                for i, up_pos in enumerate(last_mem[D2]) :
                    new_mem[D2][(i^grid[D1][D2])] = (up_pos + new_mem[D2-1][i]) % mod
            last_mem = new_mem
        return last_mem[len(grid[0])-1][k]

# # given ans 1011ms Beats98.33%
# # extend the 2D array to shorten the code
# MOD = 10**9+7
# class Solution:
#     def countPathsWithXorValue(self, grid: List[List[int]], tar: int) -> int:
#         m, n = len(grid), len(grid[0])
#         dp = [[[0] * 16 for _ in range(n+1)] for _ in range(m+1)]
#         dp[0][1][0] = 1
#         for i, row in enumerate(grid):
#             for j, x in enumerate(row):
#                 for k in range(16):
#                     dp[i+1][j+1][k] = (dp[i][j+1][k^x] + dp[i+1][j][k^x]) % MOD
#         return dp[m][n][tar]

s = Solution()
print("ans :",s.countPathsWithXorValue(grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11)) # 3 
print("ans :",s.countPathsWithXorValue(grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2)) # 5
print("ans :",s.countPathsWithXorValue(grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10)) # 0
# print("ans :",s.countPathsWithXorValue()) # 



