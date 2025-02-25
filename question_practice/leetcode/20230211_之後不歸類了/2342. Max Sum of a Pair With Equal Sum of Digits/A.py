# 2342. Max Sum of a Pair With Equal Sum of Digits
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits

from typing import List
from math import inf

# my 230ms Beats99.38%
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_of_d = {}
        max_ans = -1
        for n in nums :
            # cal sum digit
            cal = n
            s = 0
            while cal :
                s += cal%10
                cal = cal//10
            # check ans
            prev_max_n = sum_of_d.get(s, -inf)
            new_sum = prev_max_n + n
            if new_sum > max_ans :
                max_ans = new_sum
            # update
            if n > prev_max_n :
                sum_of_d[s] = n
        return max_ans

s = Solution()
print("ans :",s.maximumSum([18,43,36,13,7])) # 54
print("ans :",s.maximumSum([10,12,19,14])) # -1



