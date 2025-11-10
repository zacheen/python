# 2749. Minimum Operations to Make the Integer Zero
# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero

from typing import List
from math import inf

# my 0ms
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 == 0 :
            return 0
         
        # for ans in range(1,num1.bit_length()*60+1):
        # 最好的組合應該是 
            # 1. 10^9 = 2^30
                # 所以有可能會做 30 次減法
            # 2. 30次減法 的 最大數值 = 10^9-(-10^9)*30 = 10^9*31 = 2^30*31 = 2^35
            # 3. 所以 35bits 其實就能組成任何可能出現的數字了
        for ans in range(1,35+1):
            num1 -= num2
            if num1 <= 0 :
                return -1
            if num1 >= ans >= num1.bit_count() :
                return ans
        return -1

s = Solution()
print("ans :",s.makeTheIntegerZero(num1 = 3, num2 = -2)) # 3
print("ans :",s.makeTheIntegerZero(num1 = 5, num2 = 7)) # -1
print("ans :",s.makeTheIntegerZero(num1 = 85, num2 = 42)) # -1
print("ans :",s.makeTheIntegerZero(num1 = 110, num2 = 55)) # -1
