# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List
from math import inf

# my practice again 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 == 1 :
            return False

        target = total//2
        can_comb_set = {0}  # 裡面紀錄目前可以的組合
        for num in nums:
            for s in can_comb_set.copy() :
                if (new_s := s+num) <= target:
                    if new_s == target :
                        return True
                    can_comb_set.add(new_s)
        return False

s = Solution()
print(s.canPartition(nums = [1,5,11,5])) # T
print(s.canPartition(nums = [1,2,3,5])) # F


