# 3622. Check Divisibility by Digit Sum and Product
# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product

from typing import List
from math import inf

# my 0ms
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dig_sum = 0
        copy_n = n
        while copy_n :
            dig_sum += copy_n%10
            copy_n //= 10

        dig_pro = 1
        copy_n = n
        while copy_n :
            dig_pro *= copy_n%10
            copy_n //= 10

        # print(dig_sum)
        # print(dig_pro)
        return (n % (dig_sum+dig_pro)) == 0

s = Solution()
print("ans :",s.checkDivisibility(99)) # T
print("ans :",s.checkDivisibility(23)) # F
print("ans :",s.checkDivisibility(1)) # F

