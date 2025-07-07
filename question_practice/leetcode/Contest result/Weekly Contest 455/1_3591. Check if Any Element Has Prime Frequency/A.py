# 3591. Check if Any Element Has Prime Frequency
# https://leetcode.com/problems/check-if-any-element-has-prime-frequency/description/

from typing import List
from math import inf
from collections import Counter
import math

# my 0ms
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True  # 2 is the only even prime number
            if n % 2 == 0:
                return False  # other even numbers are not prime
            
            sqrt_n = int(math.sqrt(n)) + 1
            for i in range(3, sqrt_n, 2):  # check odd numbers only
                if n % i == 0:
                    return False
            return True
        cou = Counter(nums)
        for c in cou.values():
            if is_prime(c) :
                return True
        return False


s = Solution()
print("ans :",s.checkPrimeFrequency([1,2,3,4,5,4])) # T
print("ans :",s.checkPrimeFrequency([1,2,3,4,5])) # F
print("ans :",s.checkPrimeFrequency([2,2,2,4,4])) # T



