# 3658. GCD of Odd and Even Sums
# https://leetcode.com/problems/gcd-of-odd-and-even-sums

from typing import List
from math import inf, gcd

# my 
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # sumOdd = n*n
        # sumEven = sumOdd + n
        # return gcd(sumOdd, sumEven)

        # since gcd(n*n, n*(n+1)) = n
        return n


s = Solution()
print("ans :",s.gcdOfOddEvenSums(4)) # 
print("ans :",s.gcdOfOddEvenSums(5)) # 

