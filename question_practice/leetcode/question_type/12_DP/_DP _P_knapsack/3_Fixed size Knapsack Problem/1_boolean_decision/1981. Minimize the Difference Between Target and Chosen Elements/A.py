# 1981. Minimize the Difference Between Target and Chosen Elements
# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements

from typing import List
from math import inf

# my 3150ms Beats70.24%
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        max_target = target*2

        can_comb_set = {0}  # 裡面紀錄目前可以的組合
        for each_row in mat :
            new_comb_set = set()
            for num in each_row :
                new_comb_set |= set( new_s for s in can_comb_set if (new_s := s+num) <= max_target )
            can_comb_set = new_comb_set

        if len(can_comb_set) == 0 :
            return sum(min(each_row) for each_row in mat) - target
        else :
            return min(abs(s-target) for s in can_comb_set)
            # for diff in range(0, target):
            #     if target+diff in can_comb_set or target-diff in can_comb_set :
            #         return diff

s = Solution()
print("ans :",s.minimizeTheDifference(mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13)) # 
print("ans :",s.minimizeTheDifference(mat = [[1],[2],[3]], target = 100)) # 94
print("ans :",s.minimizeTheDifference(mat = [[1,2,9,8,7]], target = 6)) # 1



