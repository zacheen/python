# 1524. Number of Sub-arrays With Odd Sum
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum

from typing import List
from math import inf

# my 54ms Beats94.35%
MOD = 10**9+7
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_c = 0
        even_c = 0
        ans_cou = 0
        for num in arr :
            if num % 2 : # odd
                even_c, odd_c = odd_c, even_c+1
            else : # even
                even_c += 1
            ans_cou += odd_c
        return ans_cou % MOD

# given ans
import math
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = s = 0
        for a in arr:
            s += a
            odd += s % 2
        return (odd + odd * (len(arr) - odd)) % (10 ** 9 + 7)

s = Solution()
print("ans :",s.numOfSubarrays([1,3,5])) # 4
print("ans :",s.numOfSubarrays([2,4,6])) # 0
print("ans :",s.numOfSubarrays([1,2,3,4,5,6,7])) # 16



