# 1800. Maximum Ascending Subarray Sum
# https://leetcode.com/problems/maximum-ascending-subarray-sum/description

from typing import List
import functools

from math import inf
# my 0ms Beats100.00%
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = 0
        ans = 0
        prev = inf
        for n in nums :
            if n > prev :
                s += n
            else :
                ans = max(ans, s)
                s = n
            prev = n
        return max(ans, s)




