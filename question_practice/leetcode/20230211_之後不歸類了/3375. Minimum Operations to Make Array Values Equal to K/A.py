# 3375. Minimum Operations to Make Array Values Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k

from typing import List
from math import inf

# my v3 optimized by given ans : 58ms Beats93.87%
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(n<k for n in nums) :
            return -1
        seen = set(nums)
        if k in seen :
            return len(seen)-1
        else :
            return len(seen)

# my v2 64ms Beats74.53%
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        for n in nums :
            if n >= k :
                seen.add(n)
            else :
                return -1
        if k in seen :
            return len(seen)-1
        else :
            return len(seen)

# my v1 70ms Beats35.38%
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        dist_nums = sorted(set(nums))
        if dist_nums[0] < k :
            return -1
        for i, n in enumerate(dist_nums) :
            if n > k :
                return len(dist_nums) - i
        return 0

s = Solution()
print("ans :",s.minOperations(nums = [5,2,5,4,5], k = 2)) # 2
print("ans :",s.minOperations(nums = [2,1,2], k = 2)) # -1
print("ans :",s.minOperations(nums = [9,7,5,3], k = 1)) # 4
print("ans :",s.minOperations(nums = [1], k = 1)) # 0



