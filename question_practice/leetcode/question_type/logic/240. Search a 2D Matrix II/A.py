# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

from typing import List
from math import inf

# my 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # from the top left
        i1 = 0
        i2 = len(matrix[0])-1

        while i1 < len(matrix) and i2 >= 0 :
            now_n = matrix[i1][i2]
            if now_n == target :
                return True
            if target > now_n :
                i1 += 1
            else :
                i2 -= 1
        return False

# this only works on square shape
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         mid_n = list( matrix[i][i] for i in range(len(matrix)))
#         num_at = bisect_right(mid_n, target)-1
#         # top
#         top_row = list(matrix[i][num_at] for i in range(num_at))
#         # print(top_row)
#         if target in top_row :
#             return True
        
#         # left
#         left_row = matrix[num_at][:num_at+1] # +1 to include the [num_at][num_at] 
#         # print(left_row)
#         if target in left_row :
#             return True

#         return False

s = Solution()
print("ans :",s.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)) # 
print("ans :",s.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20)) # 
print("ans :",s.searchMatrix([[-1,3]], 3)) # 



