# 2566. Maximum Difference by Remapping a Digit
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit

from typing import List
from math import inf

# fail : forgot to break
# fail : didn't consider the case when all digits are same EX:99999

# my : 0ms
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_s = str(num)
        max_n = int('9'*len(num_s))
        for c in num_s:
            if c != '9' :
                max_n = int("".join('9' if n == c else n for n in num_s))
                break
        
        min_n = 0
        for c in num_s:
            if c != '0' :
                min_n = int("".join('0' if n == c else n for n in num_s))
                break

        # print(max_n, min_n)
        return max_n - min_n

s = Solution()
print("ans :",s.minMaxDifference(11891)) # 99009 = 99899 - 890
print("ans :",s.minMaxDifference(90)) # 99
print("ans :",s.minMaxDifference(456)) # 900
print("ans :",s.minMaxDifference(99999)) # 99999



