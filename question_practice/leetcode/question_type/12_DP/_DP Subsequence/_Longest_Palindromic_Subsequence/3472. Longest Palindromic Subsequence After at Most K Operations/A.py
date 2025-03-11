# 3472. Longest Palindromic Subsequence After at Most K Operations
# https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/description/

from typing import List
from math import inf
from functools import cache

# my 4703ms Beats92.68%
@cache
def cal_diff(c1,c2):
    o1 = ord(c1)
    o2 = ord(c2)
    diff = abs(o1-o2)
    return min(diff, 26-diff)

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        @cache
        def dp(l, r, remain_k):
            if l == r : 
                return 1
            elif l > r : 
                return 0
        
            ret = 0
            # let l == r
            if (need_diff := cal_diff(s[l], s[r])) <= remain_k :
                ret = dp(l+1, r-1, remain_k-need_diff) + 2
            # skip l
            if (re:= dp(l+1, r, remain_k)) > ret :
                ret = re
            # skip r
            if (re:= dp(l, r-1, remain_k)) > ret :
                ret = re
            return ret
        ans = dp(0, len(s)-1, k)
        dp.cache_clear() # needed to prevent memory limited exceed
        return ans

s = Solution()
print("ans :",s.longestPalindromicSubsequence(s = "abced", k = 2)) # 3
print("ans :",s.longestPalindromicSubsequence(s = "aaazzz", k = 4)) # 6



