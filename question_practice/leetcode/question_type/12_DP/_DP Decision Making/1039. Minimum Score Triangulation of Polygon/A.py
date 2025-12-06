# 1039. Minimum Score Triangulation of Polygon
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon

from typing import List
from math import inf
from functools import cache

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        len_v = len(values)
        dp = [[0] * len_v for _ in range(len_v)]
        for L in range(3, len_v+1):
            for n1 in range(len_v-L+1):
                n2 = n1+L-1
                best = inf
                for n3 in range(n1+1, n2):
                    cost = dp[n1][n3] + dp[n3][n2] + values[n1] * values[n2] * values[n3]
                    if cost < best:
                        best = cost
                dp[n1][n2] = best
        return dp[0][-1]

# my fail, this question cannot be solved by greedy
# class Solution:
#     def minScoreTriangulation(self, values: List[int]) -> int:
#         # every time find the smallest edge and connect them
#             # if there is multiple of them, they will also be connected in the next recursive, so don't worry
#         def seperate(values):
#             # base case 
#             if len(values) == 3 :
#                 return values[0]*values[1]*values[2]
            
#             # find the smallest three numbers and their index
#                 # to avoid finding the edge we have to track three values
#             min1 = inf
#             min1_i = -1
#             min2 = inf
#             min2_i = -1
#             min3 = inf
#             min3_i = -1

#             for i, now_v in enumerate(values):
#                 if now_v <= min1:
#                     min3, min3_i = min2, min2_i
#                     min2, min2_i = min1, min1_i
#                     min1, min1_i = now_v, i
#                 elif now_v <= min2:
#                     min3, min3_i = min2, min2_i
#                     min2, min2_i = now_v, i
#                 elif now_v <= min3:
#                     min3, min3_i = now_v, i

#             # to avoid the edge, we have to check if they are adjacent
#             if abs(min1_i - min2_i) != 1 and abs(min1_i - min2_i) != len(values)-1 :
#                 # connect min1 and min2
#                 if min1_i > min2_i :
#                     min1_i, min2_i = min2_i, min1_i
#                 new_values1 = values[min1_i:min2_i+1]
#                 new_values2 = values[min2_i:] + values[:min1_i+1]
#                 return seperate(new_values1) + seperate(new_values2)
#             elif abs(min1_i - min3_i) != 1 and abs(min1_i - min3_i) != len(values)-1 :
#                 # connect min1 and min3
#                 if min1_i > min3_i :
#                     min1_i, min3_i = min3_i, min1_i
#                 new_values1 = values[min1_i:min3_i+1]
#                 new_values2 = values[min3_i:] + values[:min1_i+1]
#                 return seperate(new_values1) + seperate(new_values2)
#             else :
#                 # find the next smallest multiple
#                 smallest_multiple = inf
#                 min1_i, min2_i = -1, -1
#                 for n1_i, n1 in enumerate(values):
#                     for n2_i in range(n1_i+2, len(values)):
#                         if n1_i == 0 and n2_i == len(values)-1 :
#                             continue
#                         n2 = values[n2_i]
#                         if (new_mul := n1*n2) < smallest_multiple:
#                             smallest_multiple = new_mul
#                             min1_i, min2_i = n1_i, n2_i
                
#                 new_values1 = values[min1_i:min2_i+1]
#                 new_values2 = values[min2_i:] + values[:min1_i+1]
#                 return seperate(new_values1) + seperate(new_values2)
#         return seperate(values)

s = Solution()
# print("ans :",s.minScoreTriangulation([1,2,3])) # 6
# print("ans :",s.minScoreTriangulation([3,7,4,5])) # 144
# print("ans :",s.minScoreTriangulation([1,3,1,4,1,5])) # 13
# print("ans :",s.minScoreTriangulation([3,4,4,4])) # 
# print("ans :",s.minScoreTriangulation([4,3,1,3])) # 24
# print("ans :",s.minScoreTriangulation([4,3,4,3,5])) # 132
# print("ans :",s.minScoreTriangulation([3,3,6,2,1,4])) # 24
print("ans :",s.minScoreTriangulation([3,6,2,1])) # 24



