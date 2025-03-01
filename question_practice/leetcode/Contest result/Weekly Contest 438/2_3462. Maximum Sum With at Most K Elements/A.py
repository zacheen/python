# 3462. Maximum Sum With at Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

from typing import List
from math import inf
from heapq import merge

# my v1 355ms Beats35.94%
    # I thought merge sort would be faster, but actually not
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        if k == 0 : return 0
        poss_l = []
        for l, lim in zip(grid, limits) :
            l.sort(reverse = True)
            poss_l.append(l[:lim])
        sort_poss = merge(*poss_l, reverse=True)
        return sum(next(sort_poss) for _ in range(k))
    
# my v2 123ms Beats96.67%
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        if k == 0 : return 0
        poss_l = []
        for l, lim in zip(grid, limits) :
            l.sort(reverse = True)
            poss_l += l[:lim]
        poss_l.sort(reverse = True)
        return sum(poss_l[:k])

s = Solution()
print("ans :",s.maxSum(grid = [[1,2],[3,4]], limits = [1,2], k = 2)) # 7
print("ans :",s.maxSum(grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3)) # 21



