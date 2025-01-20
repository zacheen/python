# 3223. Minimum Length of String After Operations
# https://leetcode.com/problems/minimum-length-of-string-after-operations/description

from typing import List
import functools

# my 
from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if n%2 else 2 for n in Counter(s).values())

# given ans
# same

s = Solution()
# print("ans :",s.minimumLength()) # 



