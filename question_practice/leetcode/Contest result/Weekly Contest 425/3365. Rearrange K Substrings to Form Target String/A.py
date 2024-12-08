# 3365. Rearrange K Substrings to Form Target String
# https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/description/

from typing import List
import functools

# my 164ms Beats89.81%
from collections import Counter
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        l = len(s)//k
        c1 = Counter([s[i:i + l] for i in range(0, len(s), l)])
        c2 = Counter([t[i:i + l] for i in range(0, len(t), l)])
        return c1 == c2

# given ans

s = Solution()
print("ans :",s.())



