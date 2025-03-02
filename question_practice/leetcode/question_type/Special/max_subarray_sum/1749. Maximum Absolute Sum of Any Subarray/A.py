# 1749. Maximum Absolute Sum of Any Subarray
# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray

from typing import List
from math import inf
from itertools import accumulate
# my 23ms Beats90.24%
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_s = min_s = ans = 0
        for acc in accumulate(nums) :
            if acc > max_s :
                max_s = acc
            elif acc < min_s :
                min_s = acc

            if acc > 0 :
                if (t:=acc-min_s) > ans :
                    ans = t
            else :
                if (t:=max_s-acc) > ans :
                    ans = t
        return ans
        
# given ans 8ms Beats99.27%
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        preSum = [0]+list(accumulate(nums))
        return max(preSum) - min(preSum)
        # abs ??
            # == abs( min(preSum)-max(preSum) ) == -( min(preSum)-max(preSum) )
        # front - back ??
            # max(preSum) there is no other bigger number, so it can be the maximum

s = Solution()
print("ans :",s.maxAbsoluteSum([1,-3,2,3,-4])) # 2,3 > 5
print("ans :",s.maxAbsoluteSum([2,-5,1,-4,3,-2])) # -5,1,-4 > 8
print("ans :",s.maxAbsoluteSum([3,4,-1,-4,-3]))



