# 523. Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/description/

from typing import List
from math import inf
from itertools import accumulate

# my 31ms Beats99.58%
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen_mod = set()
        temp = 0
        for acc in accumulate(nums) :
            now_mod = acc % k
            if now_mod in seen_mod :
                return True
            seen_mod.add(temp)
            temp = now_mod
        return False
            

s = Solution()
print("ans :",s.checkSubarraySum(nums = [23,2,4,6,7], k = 6)) # [2,4]
print("ans :",s.checkSubarraySum(nums = [23,2,6,4,7], k = 6)) # [23,2,6,4,7]
print("ans :",s.checkSubarraySum(nums = [23,2,6,4,7], k = 13)) # F



