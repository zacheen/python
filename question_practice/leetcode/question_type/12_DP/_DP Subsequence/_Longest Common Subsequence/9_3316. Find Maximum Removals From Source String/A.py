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

# my (for version) : 1242ms Beats90.37%
from itertools import zip_longest  
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        set_tar_i = set(targetIndices)
        dp = [-inf]*len(pattern) + [0]
        for s_i in range(len(source)-1,-1,-1) :
            can_del = s_i in set_tar_i 
            s_c = source[s_i]
            for p_i, p_c in enumerate(pattern):
                if can_del :
                    dp[p_i] += 1
                if p_c == s_c :
                    dp[p_i] = max(dp[p_i], dp[p_i+1])
            if can_del :
                dp[-1] += 1
        return dp[0]

s = Solution()
print("ans :",s.maxRemovals(source = "abbaa", pattern = "aba", targetIndices = [0,1,2])) # 1
# print("ans :",s.maxRemovals(source = "babbaa", pattern = "aba", targetIndices = [0,1,2,3])) # 
# print("ans :",s.maxRemovals(source = "bcda", pattern = "d", targetIndices = [0,3])) # 2
# print("ans :",s.maxRemovals(source = "dda", pattern = "dda", targetIndices = [0,1,2])) # 0
# print("ans :",s.maxRemovals(source = "yeyeykyded", pattern = "yeyyd", targetIndices = [0,2,3,4])) # 2
# print("ans :",s.maxRemovals(source = "ordzbihwzbfsukguq", pattern = "rdzbugu", targetIndices = [0,2,3,5,6,7,8,9,10,16])) # 8



