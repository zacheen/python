# 2529. Maximum Count of Positive Integer and Negative Integer
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

from typing import List
from math import inf
import bisect

# my 
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = bisect.bisect_right(nums, -1)
        neg = len(nums) - bisect.bisect_right(nums, 0)
        return max(pos, neg)

s = Solution()
print("ans :",s.maximumCount([-3,-2,-1,0,0,1,2])) # 3



