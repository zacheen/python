# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List
from math import inf

# my : 149ms Beats97.30%
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 :
            return False

        half = total // 2
        reach_sum = set([0])
        for n in nums :
            for s in reach_sum.copy():
                if (new_s := s+n) <= half :
                    reach_sum.add(new_s)
            if half in reach_sum :
                return True
        return False

s = Solution()
print(s.canPartition(nums = [1,5,11,5])) # T
print(s.canPartition(nums = [1,2,3,5])) # F


