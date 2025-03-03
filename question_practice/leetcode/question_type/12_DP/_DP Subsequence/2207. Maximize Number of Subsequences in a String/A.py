# 2207. Maximize Number of Subsequences in a String
# https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/description/

from typing import List
import functools

# my 250ms Beats21.05%
from collections import Counter 
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        cou = Counter()
        ans = 0
        first_p = pattern[0]
        second_p = pattern[1]
        for c in text :
            if c == second_p :
                ans += cou[first_p]
            cou[c] += 1
        return ans + max(cou[pattern[0]], cou[pattern[1]])

# my opt 66ms Beats95.49%
from math import comb
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # two pattern char is the same
        if pattern[0] == pattern[1] :
            cou = text.count(pattern[0])
            return comb(cou+1,2)
        
        cou_f = 0
        cou_s = 0
        ans = 0
        first_p = pattern[0]
        second_p = pattern[1]
        for c in text :
            if c == first_p :
                cou_f += 1
            if c == second_p :
                ans += cou_f
                cou_s += 1
        return ans + max(cou_f, cou_s)
    
# given ans
# same

s = Solution()
print("ans :",s.maximumSubsequenceCount(text = "abdcdbc", pattern = "ac")) # 4
print("ans :",s.maximumSubsequenceCount(text = "aabb", pattern = "ab")) # 6
print("ans :",s.maximumSubsequenceCount("y","yy")) # 1
# print("ans :",s.maximumSubsequenceCount()) # 



