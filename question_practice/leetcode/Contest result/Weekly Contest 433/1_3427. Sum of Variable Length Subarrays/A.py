# 3427. Sum of Variable Length Subarrays
# https://leetcode.com/problems/sum-of-variable-length-subarrays/description/

from typing import List
import functools

# my 
from itertools import accumulate
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        acc = [0]+list(accumulate(nums))
        ans = 0
        for i,n in enumerate(nums) :
            start = max(0, i - n)
            ans += acc[i+1] - acc[start]
        return ans

# given ans
# same concept, but I optimized

s = Solution()
print("ans :",s.subarraySum(nums = [1,2,3], k = 2)) # 24



