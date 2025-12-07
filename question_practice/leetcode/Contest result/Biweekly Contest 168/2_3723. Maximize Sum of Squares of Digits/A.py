# 3723. Maximize Sum of Squares of Digits
# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/description/

from typing import List
from math import inf

# my : 4ms Beats100.00%
class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        if sum_val > (num*9) :
            return ""
        
        cnt_9 = sum_val//9
        cnt_0 = num - cnt_9 - 1
        if cnt_0 < 0 :
            return "9"*cnt_9
        else :
            return "9"*cnt_9 + str(sum_val%9) + "0"*cnt_0

s = Solution()
print("ans :",s.maxSumOfSquares(num = 2, sum_val = 3)) # "30"
print("ans :",s.maxSumOfSquares(num = 2, sum_val = 17)) # "98"
print("ans :",s.maxSumOfSquares(num = 1, sum_val = 10)) # ""
print("ans :",s.maxSumOfSquares(num = 2, sum_val = 18)) # "99"
print("ans :",s.maxSumOfSquares(num = 2, sum_val = 1)) # "10"

