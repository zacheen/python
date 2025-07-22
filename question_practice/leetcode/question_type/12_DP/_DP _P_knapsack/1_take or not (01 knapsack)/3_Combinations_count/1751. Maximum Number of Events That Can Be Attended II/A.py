# 1751. Maximum Number of Events That Can Be Attended II
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii

from typing import List
from math import inf
from functools import cache
import bisect

# my v2 (01 Knapsack) : 1213ms Beats35.71%
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x : x[1])
        
        @cache
        def far_ava(st):
            return bisect.bisect_left(events, st, key=lambda x: x[1])-1

        @cache
        def dp(now_i, rem_k):
            if rem_k == 0 or now_i < 0 : return 0
            st, _, val = events[now_i]
            # take 
            res1 = dp(far_ava(st), rem_k-1) + val
            # dont take
            res2 = dp(now_i-1, rem_k)
            return res1 if res1 > res2 else res2
        return dp(len(events)-1,k)

# # my v1 Time Limit Exceeded
# class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
#         end_i = len(events)-1
#         events.sort(key = lambda x : x[0])
#         def dp(last_i, rem_k):
#             if rem_k == 0 or last_i == end_i : return 0
            
#             if last_i == -1 :
#                 last_en = -1
#             else :
#                 _, last_en, _ = events[last_i]
            
#             ret = 0
#             for i, (st, en, val) in enumerate(events[last_i+1:], last_i+1) :
#                 if st <= last_en : continue
#                 new_s = dp(i, rem_k-1) + val
#                 if new_s > ret :
#                     ret = new_s
#             return ret
#         return dp(-1,k)

# given ans : 498ms Beats92.31%
from bisect import bisect_right
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x : x[0])
        starts = [event[0] for event in events]
        n = len(events)
        
        dp = [ [0]*(k+1) for _ in range(n+1) ]
        for i in range(n-1, -1, -1):
            next_index = bisect_right(starts, events[i][1])
            for j in range(1, k+1):
                dp[i][j] = max(dp[i+1][j], events[i][2] + dp[next_index][j-1])
        return dp[0][k]


s = Solution()
print("ans :",s.maxValue(events = [[1,2,4],[3,4,3],[2,3,1]], k = 2)) # 7
print("ans :",s.maxValue(events = [[1,2,4],[3,4,3],[2,3,10]], k = 2)) # 10
print("ans :",s.maxValue(events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3)) # 9
print("ans :",s.maxValue(events = [[1,2,4],[3,4,8],[5,6,4],[2,3,1],[4,5,10],[6,7,1]], k = 3)) # 16



