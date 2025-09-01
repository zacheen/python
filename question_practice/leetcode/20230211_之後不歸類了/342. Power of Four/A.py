# 342. Power of Four
# https://leetcode.com/problems/power-of-four

from typing import List
from math import inf

# my 0ms
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 :
            return False
        while n > 1 :
            if n % 4 :
                return False
            n //= 4
        return True

s = Solution()
print("ans :",s.isPowerOfFour(16)) # T
print("ans :",s.isPowerOfFour(5)) # F
print("ans :",s.isPowerOfFour(1)) # T
print("ans :",s.isPowerOfFour(0)) # F



