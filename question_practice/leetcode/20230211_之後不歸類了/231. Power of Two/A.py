# 231. Power of Two
# https://leetcode.com/problems/power-of-two

from typing import List
from math import inf

# my 0ms
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0 :
            return False
        while n > 1 :
            if n & 1 :
                return False
            else :
                n >>= 1
        return True


