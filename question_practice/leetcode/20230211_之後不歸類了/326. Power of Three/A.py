# 326. Power of Three
# https://leetcode.com/problems/power-of-three

from typing import List
from math import inf

# my 4ms Beats87.54%
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 :
            return False
        while n > 1 :
            if n % 3 :
                return False
            n //= 3
        return True

s = Solution()
print("ans :",s.isPowerOfThree(27)) # T
print("ans :",s.isPowerOfThree(0)) # F
print("ans :",s.isPowerOfThree(-1)) # F
print("ans :",s.isPowerOfThree(1)) # T



