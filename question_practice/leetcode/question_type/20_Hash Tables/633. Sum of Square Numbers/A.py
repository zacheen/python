# 633. Sum of Square Numbers
# https://leetcode.com/problems/sum-of-square-numbers

from typing import List
from math import inf

# my : 31ms Beats97.36%
    # Hash map
squ_l = list(i**2 for i in range(2**16))
squ_set = set(squ_l)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_c = int(c**(1/2))
        for poss_a in squ_l[:sqrt_c+1] :
            if (c - poss_a) in squ_set :
                return True
        return False

s = Solution()
print("ans :",s.judgeSquareSum(5)) # T
print("ans :",s.judgeSquareSum(3)) # F
print("ans :",s.judgeSquareSum(169)) # T



