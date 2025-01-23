# 1572. Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/description/

from typing import List
import functools

# my v1
# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         ans_sum = 0
#         edge_max = len(mat)-1
#         for i in range(len(mat)) :
#             ans_sum += mat[i][i]
#             ans_sum += mat[i][edge_max - i]
#         if len(mat) % 2 :
#             mid = len(mat) >> 1
#             ans_sum -= mat[mid][mid]
#         return ans_sum

# my v2 
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        edge_max = len(mat)-1
        ans_sum = sum(mat[i][i] + mat[i][edge_max - i] for i in range(len(mat)))
        if len(mat) % 2 :
            mid = len(mat) >> 1
            ans_sum -= mat[mid][mid]
        return ans_sum

s = Solution()
print(s.diagonalSum())



