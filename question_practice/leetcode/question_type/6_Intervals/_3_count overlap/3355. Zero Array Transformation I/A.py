# 3355. Zero Array Transformation I
# https://leetcode.com/problems/zero-array-transformation-i/

from typing import List
import functools

# # my 
# class Solution:
#     def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
#         cou = [0]*len(nums)
#         for sta, end in queries :
#             for i in range(sta, end+1) :
#                 cou[i] += 1
#         return all(s >= n for n, s in zip(nums, cou))

# given ans v1 74ms Beats81.11%
# algorithm <Line Sweep> : calculating interval overlaps (same concept from above)
from itertools import accumulate
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        interval = [0]*(len(nums) + 1)
        for sta, end in queries :
            interval[sta] += 1
            interval[end+1] -= 1
        # print("interval 1:",interval)
        return all(aff >= n for n, aff in zip(nums, accumulate(interval)))
        
        # # much slower, but is correct
        # for indx, n in enumerate(nums) :
        #     interval[indx] -= n
        #     interval[indx+1] += n
        # print("interval 2:",interval)
        # return all(each_s>=0 for each_s in accumulate(interval))

s = Solution()
print("ans :",s.isZeroArray(nums = [1,0,1], queries = [[0,2]]))
print("ans :",s.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]]))
print("ans :",s.isZeroArray([8,6],[[0,0],[1,1],[0,0],[0,0],[1,1],[0,1],[0,0],[0,0],[1,1],[0,1],[1,1],[0,1],[0,0],[0,0],[0,1]]))



