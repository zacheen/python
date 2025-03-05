# 44. Wildcard Matching
# https://leetcode.com/problems/wildcard-matching/description/

from typing import List
from math import inf
from functools import cache

# my 1354ms Beats5.01%
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(s_i, p_i) :
            if s_i == len(s) and p_i == len(p):
                return True
            if p_i >= len(p) :
                return False
            
            p_c = p[p_i]
            if s_i < len(s) and p_c == s[s_i] :
                if dp(s_i+1, p_i+1) :
                    return True
            elif p_c == "?" :
                if dp(s_i+1, p_i+1) :
                    return True
            elif p_c == "*" :
                if any(dp(poss_s_i, p_i+1) for poss_s_i in range(s_i, len(s)+1)) :
                    return True
            return False
        return dp(0,0)

# given ans
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
    
        last_match = 0
        star = -1
    
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                last_match = i
                star = j
                j += 1
            elif star != -1:
                j = star + 1
                i = last_match + 1
                last_match += 1
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

s = Solution()
print("ans :",s.isMatch(s = "aa", p = "a")) # F
print("ans :",s.isMatch(s = "aa", p = "*")) # T
print("ans :",s.isMatch(s = "cb", p = "?a")) # F



