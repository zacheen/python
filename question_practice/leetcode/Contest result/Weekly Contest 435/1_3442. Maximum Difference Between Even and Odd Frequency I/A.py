# 3442. Maximum Difference Between Even and Odd Frequency I
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/

from typing import List
import functools

from collections import Counter
from math import inf
# my 0ms Beats100.00%
class Solution:
    def maxDifference(self, s: str) -> int:
        cou = Counter(s)
        max_odd = -inf
        min_even = inf
        for _, n in cou.items() :
            if n % 2 :
                max_odd = max(max_odd, n)
            else :
                min_even = min(min_even, n)
        return max_odd-min_even

# given ans
# same concept

s = Solution()
print("ans :",s.maxDifference("aaaaabbc")) # 3
print("ans :",s.maxDifference("abcabcab")) # 1



