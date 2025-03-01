# 3461. Check If Digits Are Equal in String After Operations I
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

from typing import List
from math import inf
from itertools import pairwise

# my 27ms Beats86.55%
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(c) for c in s]
        while len(s) > 2 :
            s = [(n1+n2)%10 for n1,n2 in pairwise(s)]
            # print(s)
        return s[0] == s[1]

s = Solution()
print("ans :",s.hasSameDigits("3902")) # T "11"
print("ans :",s.hasSameDigits("34789")) # F "48"



