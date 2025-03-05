# 3316. Find Maximum Removals From Source String
# https://leetcode.com/problems/find-maximum-removals-from-source-string/description/

from typing import List
from math import inf
from bisect import bisect_left
from functools import cache

# my 2549ms Beats45.33%
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        set_tar_i = set(targetIndices)
        @cache
        def dfs(s_i, p_i):
            if p_i == len(pattern) :
                return len(targetIndices) - bisect_left(targetIndices, s_i)
            if s_i == len(source) :
                return -inf
            
            # dont del s_i
            if source[s_i] == pattern[p_i] :
                # can using source to fit pattern
                ret = dfs(s_i+1, p_i+1)
            else :
                # but p_i can't forward
                ret = dfs(s_i+1, p_i)

            # del s_i, and return res +1
            if s_i in set_tar_i :
                if (r := dfs(s_i+1, p_i) + 1) > ret :
                    ret = r
                
            return ret
        return dfs(0,0)

# # my optimized ??
# class Solution:
#     def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
#         set_tar_i = set(targetIndices)
#         dp = [0]*(len(source)+1) # dp[到這個位置] = 最多可以刪除幾個項目
#         dp[0] = 0
#         for c1 in pattern :
#             new_dp = [-inf] # 通常可以跳過某個項目用 0, 若不要跳過用 -inf
#             for j, c2 in enumerate(source) :
#                 # dont del s_i
#                 if c1 == c2 :
#                     new_dp.append(dp[j])
#                 else :
#                     new_dp.append(dp[j+1])
#                 # del s_i
#                 if j in set_tar_i :
#                     new_dp[-1] = max(new_dp[-1], new_dp[j+1]+1)
#             dp = new_dp
#         return dp[-1]

s = Solution()
print("ans :",s.maxRemovals(source = "abbaa", pattern = "aba", targetIndices = [0,1,2])) # 1
# print("ans :",s.maxRemovals(source = "babbaa", pattern = "aba", targetIndices = [0,1,2,3])) # 
# print("ans :",s.maxRemovals(source = "bcda", pattern = "d", targetIndices = [0,3])) # 2
# print("ans :",s.maxRemovals(source = "dda", pattern = "dda", targetIndices = [0,1,2])) # 0
# print("ans :",s.maxRemovals(source = "yeyeykyded", pattern = "yeyyd", targetIndices = [0,2,3,4])) # 2
# print("ans :",s.maxRemovals(source = "ordzbihwzbfsukguq", pattern = "rdzbugu", targetIndices = [0,2,3,5,6,7,8,9,10,16])) # 8



