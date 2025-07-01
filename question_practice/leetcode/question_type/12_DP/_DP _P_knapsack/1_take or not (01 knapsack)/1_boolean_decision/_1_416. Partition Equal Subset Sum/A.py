# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List
from math import inf

# my using template knapsack_01_reach (sparse) : 175ms Beats95.19%
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 :
            return False

        target = total // 2
        can_comb_set = {0}  # 裡面紀錄目前可以的組合
        for num in nums:
            can_comb_set |= set( new_s for s in can_comb_set if (new_s := s + num) <= target )
            if target in can_comb_set : return True
        return False

# my using template knapsack_01_reach v1 : 241ms Beats90.33%
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 :
            return False

        target = total // 2
        dp = [True] + [False]*(target)
        for num in nums:
            for pre_i in range(target-num, -1, -1): # 從大到小
                if dp[pre_i] :
                    dp[pre_i+num] = True
            if dp[-1] :
                return True
        return False

s = Solution()
print(s.canPartition(nums = [1,5,11,5])) # T
print(s.canPartition(nums = [1,2,3,5])) # F


