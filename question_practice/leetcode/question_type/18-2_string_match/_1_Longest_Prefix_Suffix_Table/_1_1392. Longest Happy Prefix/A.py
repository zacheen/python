# 1392. Longest Happy Prefix
# https://leetcode.com/problems/longest-happy-prefix/description/

from typing import List
from math import inf

# my using template
def cal_LPST(s): 
    len_s = len(s)
    lps = [0] * len_s
    pref_l = 0
    i = 1
    while i < len_s:
        if s[i] == s[pref_l]: # two pointer are the same word
            pref_l += 1
            lps[i] = pref_l
            i += 1
        else: # two pointer are not the same word
            if pref_l != 0: # find fast forward position
                pref_l = lps[pref_l - 1]
            else: # no fast forward position
                lps[i] = 0
                i += 1
    return lps

class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = cal_LPST(s)
        return s[:lps[-1]]

s = Solution()
print("ans :",s.longestPrefix("level")) # l
print("ans :",s.longestPrefix("ababab")) # abab
print("ans :",s.longestPrefix("abcba")) # 



