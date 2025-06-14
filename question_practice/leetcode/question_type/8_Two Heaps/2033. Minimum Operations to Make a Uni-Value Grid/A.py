# 2033. Minimum Operations to Make a Uni-Value Grid
# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid

from typing import List
from math import inf
from functools import reduce
from itertools import pairwise

# my v1_2 (sort) : 71ms Beats100.00%
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        mod_val = grid[0][0] % x
        for l in grid :
            for n in l :
                if n%x != mod_val :
                    return -1
        
        # reduce take so much time : 7697ms Beats5.26%  
        # all_num = reduce(operator.add, grid)
        all_num = []
        for l in grid:
            all_num += l
        all_num.sort()
        
        mid_i = len(all_num) // 2
        mid_num = all_num[mid_i]
        return (mid_num*mid_i - sum(all_num[:mid_i]))//x + (sum(all_num[mid_i+1:]) - mid_num*(len(all_num)-mid_i-1) )//x         

# # my v1 (sort) : 7905ms Beats5.26% 
# class Solution:
#     def minOperations(self, grid: List[List[int]], x: int) -> int:
#         all_num = reduce(lambda n1,n2 : n1+n2, grid)
#         all_num.sort()
        
#         mid_i = len(all_num) // 2
#         ans_cou = 0
#         for i, (n1,n2) in enumerate(pairwise(all_num[:mid_i+1])) :
#             if (diff := n2-n1) % x :
#                 return -1
#             ans_cou += (diff//x)*(i+1)
#         for i, (n1,n2) in enumerate(pairwise(all_num[:mid_i-1:-1])) :
#             if (diff := n1-n2) % x :
#                 return -1
#             ans_cou += (diff//x)*(i+1)
#         return ans_cou

# my v2 (two heap) : 245ms Beats22.37%
# 如果 median 不會變動的話，用 sort 會比較快
from heapq import heappushpop, heappush
class MedianFinder:
    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num):
        if len(self.heap1) > len(self.heap2) :
            # need to put into heap2
            if self.heap1 and num > self.heap1[0] :
                num = heappushpop(self.heap1, num)
            heappush(self.heap2, -num)
        else :
            # need to put into heap1
            if self.heap2 and num < -self.heap2[0] :
                num = -heappushpop(self.heap2, -num)
            heappush(self.heap1, num)

    def findmid(self):
        return self.heap1[0]

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        mid = MedianFinder()
        check_n = grid[0][0]
        for l in grid :
            for n in l :
                if (check_n - n)%x :
                    return -1
                mid.addNum(n)

        mid_num = mid.findmid()
        return (sum(mid.heap1)-mid_num*len(mid.heap1))//x + (mid_num*len(mid.heap2)+sum(mid.heap2))//x

s = Solution()
print("ans :",s.minOperations(grid = [[2,4],[6,8]], x = 2)) # 4
print("ans :",s.minOperations(grid = [[1,5],[2,3]], x = 1)) # 5
print("ans :",s.minOperations(grid = [[1,2],[3,4]], x = 2)) # -1



