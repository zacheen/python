# 2661. First Completely Painted Row or Column
# https://leetcode.com/problems/first-completely-painted-row-or-column/description

from typing import List
import functools

# my 107ms Beats89.59%
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n_to_i = {}
        for n1,l in enumerate(mat) :
            for n2, this_num in enumerate(l) :
                n_to_i[this_num] = (n1,n2)

        cou_n1 = [len(mat[0]) for _ in range(len(mat))]
        cou_n2 = [len(mat) for _ in range(len(mat[0]))]

        for i, n in enumerate(arr) :
            n1,n2 = n_to_i[n]
            cou_n1[n1] -= 1
            cou_n2[n2] -= 1
            if cou_n2[n2] == 0 or cou_n1[n1] == 0:
                return i    

# given ans
    # concept is the same, but n_to_i is a list for faster speed and save space
# my ref given ans to optimize : 75ms Beats98.11%
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n_to_i = [(0,0)]*(len(mat)*len(mat[0])+1)
        for n1,l in enumerate(mat) :
            for n2, this_num in enumerate(l) :
                n_to_i[this_num] = (n1,n2)

        cou_n1 = [len(mat[0]) for _ in range(len(mat))]
        cou_n2 = [len(mat) for _ in range(len(mat[0]))]

        for i, n in enumerate(arr) :
            n1,n2 = n_to_i[n]
            cou_n1[n1] -= 1
            cou_n2[n2] -= 1
            if cou_n2[n2] == 0 or cou_n1[n1] == 0:
                return i
            

s = Solution()
print("ans :",s.firstCompleteIndex([5,6,1,3,4,2], [[1,4,5],[2,3,6]])) # 1



