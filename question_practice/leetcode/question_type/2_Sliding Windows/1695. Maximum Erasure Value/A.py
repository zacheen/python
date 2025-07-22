# 1695. Maximum Erasure Value
# https://leetcode.com/problems/maximum-erasure-value

from typing import List
from math import inf
from itertools import accumulate

# my 139ms Beats98.44%
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        acc_l = list(accumulate(nums))
        seen_n = set()
        l = -1
        max_sum = 0
        for r, r_n in enumerate(nums) :
            while r_n in seen_n :
                l += 1
                seen_n.remove(nums[l])
            seen_n.add(r_n)
            
            if l >= 0 :
                if (new_sum := acc_l[r]-acc_l[l]) > max_sum :
                    max_sum = new_sum
            else :
                max_sum = acc_l[r]
        return max_sum

s = Solution()
print("ans :",s.maximumUniqueSubarray([4,2,4,5,6])) # 17 [2,4,5,6]
print("ans :",s.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5])) # 8 [5,2,1], 其實還有 [1,2,5]
print("ans :",s.maximumUniqueSubarray([10000])) # 10000



