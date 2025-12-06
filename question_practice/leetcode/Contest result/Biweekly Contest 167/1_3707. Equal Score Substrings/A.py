# 3707. Equal Score Substrings
# https://leetcode.com/problems/equal-score-substrings/

from typing import List
from math import inf
from bisect import bisect_right

# my 0ms
class Solution:
    def scoreBalance(self, s: str) -> bool:
        # no corner case ""

        acc = []
        now_sum = 0
        diff_to_score = ord('a')-1
        for c in s :
            now_sum += ord(c)-diff_to_score
            acc.append(now_sum)
        
        total = acc[-1]
        if total & 1 :
            return False
        half = total//2
        ret_i = bisect_right(acc, half)-1
        return acc[ret_i] == half

s = Solution()
print("ans :",s.scoreBalance("adcb")) # T
print("ans :",s.scoreBalance("bace")) # F

