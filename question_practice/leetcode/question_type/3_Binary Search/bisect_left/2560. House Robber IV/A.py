# 2560. House Robber IV
# https://leetcode.com/problems/house-robber-iv

from typing import List
from math import inf
from bisect import bisect_left

# inspire by given ans : 203ms Beats81.72%
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(mid: int) -> bool:
            cou = 0
            prev_take = False
            for n in nums :
                if prev_take :
                    prev_take = False
                    continue
                elif n <= mid :
                    prev_take = True
                    cou += 1
                    continue
            return cou >= k
        return bisect_left(range(max(nums)+1), True, key=check)

# # my : Time Limit Exceeded
# class Solution:
#     def minCapability(self, nums: List[int], k: int) -> int:
#         dp_past = [0] + [inf]*(k)
#         dp_nei = dp_past.copy()
#         for n in nums :
#             # dont take
#             new_dp = dp_nei.copy()
#             # take
#             for i, past_max in enumerate(dp_past[:-1]) :
#                 new_dp[i+1] = min(new_dp[i+1], max(past_max, n))
#             # update
#             dp_past, dp_nei = dp_nei, new_dp
#         return dp_nei[k]

# from functools import cache
# # my : Memory Limit Exceeded
# class Solution:
#     def minCapability(self, nums: List[int], k: int) -> int:
#         len_n = len(nums)
        
#         @cache
#         def dp(now_i, remain_k, prev_rob) :
#             if remain_k == 0 :
#                 return 0
#             if now_i == len_n :
#                 return inf

#             # dont rob
#             ret = dp(now_i+1, remain_k, False)
            
#             # rob this
#             if not prev_rob :
#                 r = max(dp(now_i+1, remain_k-1, True), nums[now_i])
#                 if r < ret :
#                     ret = r
            
#             return ret
        
#         ans = dp(0, k, False)
#         dp.cache_clear()
#         return ans


s = Solution()
print("ans :",s.minCapability(nums = [2,3,5,9], k = 2)) # 5
print("ans :",s.minCapability(nums = [2,7,9,3,1], k = 2)) # 2



