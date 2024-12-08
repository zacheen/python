# 3370. Smallest Number With All Set Bits
# https://leetcode.com/problems/smallest-number-with-all-set-bits/description/

from typing import List
import functools

# my 0ms Beats100.00%
class Solution:
    def smallestNumber(self, n: int) -> int:
        now = 1
        while (now - 1) < n :
            now = 2*now
        return now - 1

s = Solution()
print("ans :",s.smallestNumber(n = 5))



