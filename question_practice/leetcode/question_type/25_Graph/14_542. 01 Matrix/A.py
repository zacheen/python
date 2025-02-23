# 542. 01 Matrix
# https://leetcode.com/problems/01-matrix

from typing import List
from math import inf

import copy
# 112ms Beats85.26%
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 0 BFS out
        q = []
        for i1, l in enumerate(mat):
            for i2, num in enumerate(l):
                if num == 0 :
                    q.append((i1,i2))
        
        i1_len = len(mat)
        i2_len = len(mat[0])
        dir_list = [(0,1),(1,0),(0,-1),(-1,0)]
        ans = [[0]*i2_len for _ in range(i1_len)]
        ans_cou = 1
        while q :
            new_q = []
            for i1,i2 in q : 
                for d1,d2 in dir_list :
                    nei1 = i1+d1
                    nei2 = i2+d2
                    if 0 <= nei1 < i1_len and 0 <= nei2 < i2_len and mat[nei1][nei2] == 1:
                        new_q.append((nei1,nei2))
                        mat[nei1][nei2] = 0
                        ans[nei1][nei2] = ans_cou
            ans_cou += 1
            q = new_q
        return ans


# given ans

s = Solution()
print("ans :",s.updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]])) # 



