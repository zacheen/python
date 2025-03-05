# 97. Interleaving String
# https://leetcode.com/problems/interleaving-string/description/

from typing import List
from math import inf
from functools import cache

# my 36ms Beats93.28%
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3) : return False
        @cache
        def dfs(s1_i,s2_i):
            if (s3_i := s1_i+s2_i) == len(s3) :
                return True
            if s1_i<len(s1) and s1[s1_i] == s3[s3_i] :
                if dfs(s1_i+1,s2_i) :
                    return True
            if s2_i<len(s2) and s2[s2_i] == s3[s3_i] :
                if dfs(s1_i,s2_i+1) :
                    return True
            return False
        return dfs(0,0)

# given ans


s = Solution()
print("ans :",s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")) # T
print("ans :",s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc")) # F
print("ans :",s.isInterleave(s1 = "", s2 = "", s3 = "")) # T



