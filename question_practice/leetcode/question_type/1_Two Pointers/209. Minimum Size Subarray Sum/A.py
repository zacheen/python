# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/

from typing import List
from math import inf

# my 6ms Beats95.59%
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        min_l = inf
        for r_i, r_n in enumerate(nums) :
            s += r_n
            while s >= target :
                min_l = min(min_l, r_i-l)
                s -= nums[l]
                l += 1
        return 0 if min_l == inf else min_l+1

# given ans
# same concept, but "inf" can change to "len(nums)+1"

s = Solution()
print("ans :",s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])) # 2



