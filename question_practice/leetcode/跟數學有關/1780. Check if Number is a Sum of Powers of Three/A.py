# 1780. Check if Number is a Sum of Powers of Three
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three

from typing import List
from math import inf

# my 
mem = [1]
def get_3_pow(n) :
    while mem[-1] < n :
        mem.append(mem[-1]*3)
    return mem[::-1]
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        l = get_3_pow(n)
        # print(l)
        for poss_n in l :
            if n >= poss_n :
                n -= poss_n
        return n == 0

# given ans
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            n, r = divmod(n, 3)
            if r == 2:
                return False
        return True

s = Solution()
print("ans :",s.checkPowersOfThree(12)) # T



