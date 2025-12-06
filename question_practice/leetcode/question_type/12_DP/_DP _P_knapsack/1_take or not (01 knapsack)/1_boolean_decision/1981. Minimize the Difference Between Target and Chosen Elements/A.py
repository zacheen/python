# 1981. Minimize the Difference Between Target and Chosen Elements
# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements

from typing import List
from math import inf
from bisect import bisect_right

# my 2390ms Beats66.12%
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        max_sum = target*2
        dp = {0}
        for rows in mat :
            new_dp = set()
            for n in rows :
                for pre_s in dp:
                    new_sum = pre_s + n
                    if new_sum <= max_sum :
                        new_dp.add(new_sum)
            dp = new_dp

        if len(dp) == 0 :
            min_sum = 0
            for rows in mat :
                min_sum += min(rows)
            # print("in min_sum", min_sum)
            return min_sum - target
        
        poss_sum = sorted(dp)
        mid_i = bisect_right(poss_sum, target)
        # print(poss_sum)
        # print(mid_i)
        if mid_i >= len(poss_sum) :
            return abs(poss_sum[mid_i-1]-target)
        elif mid_i == 0 :
            return abs(poss_sum[mid_i]-target)
        else :
            return min(abs(poss_sum[mid_i]-target), abs(poss_sum[mid_i-1]-target))

s = Solution()
print("ans :",s.minimizeTheDifference(mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13)) # 
print("ans :",s.minimizeTheDifference(mat = [[1],[2],[3]], target = 100)) # 94
print("ans :",s.minimizeTheDifference(mat = [[1,2,9,8,7]], target = 6)) # 1



