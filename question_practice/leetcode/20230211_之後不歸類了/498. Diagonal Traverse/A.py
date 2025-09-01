# 498. Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse

from typing import List
from math import inf

# my 
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        len_d1 = len(mat)
        len_d2 = len(mat[0])

        ans = []
        for i in range(len_d1+len_d2-1):
            if i&1 : # 左下 (-1, +1)
                exc = i-len_d2+1
                st2 = 0
                if exc > 0 :
                    i -= exc
                    st2 += exc
                for n1,n2 in zip(range(st2, len_d1),range(i, -1, -1)):
                    ans.append(mat[n1][n2])
            else :   # 右上 (+1, -1)
                exc = i-len_d1+1
                st2 = 0
                if exc > 0 :
                    i -= exc
                    st2 += exc
                for n1,n2 in zip(range(i, -1, -1),range(st2, len_d2)):
                    ans.append(mat[n1][n2])
        return ans

s = Solution()
print("ans :",s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,4,7,5,3,6,8,9]
print("ans :",s.findDiagonalOrder([[1,2],[3,4]])) # [1, 2, 3, 4]
print("ans :",s.findDiagonalOrder([[1,2,3],[4,5,6]])) # 



