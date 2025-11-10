# 1716. Calculate Money in Leetcode Bank
# https://leetcode.com/problems/calculate-money-in-leetcode-bank

from typing import List
from math import inf

# my : 0ms
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        a1_week = sum(range(1,8))
        complete_weeks = ( a1_week + a1_week+((weeks-1)*7) ) * weeks // 2

        a1_day = 1+weeks
        remain_week = (a1_day + a1_day + (days-1) ) * days // 2
        # print(complete_weeks, remain_week)
        return complete_weeks + remain_week

s = Solution()
print("ans :",s.totalMoney(4)) # 10
print("ans :",s.totalMoney(10)) # 37
print("ans :",s.totalMoney(20)) # 96
    # (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96



