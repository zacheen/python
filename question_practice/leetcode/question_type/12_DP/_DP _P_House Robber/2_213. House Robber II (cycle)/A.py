# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/description/

from typing import List
from math import inf

# my : 0ms Beats100.00%
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :return nums[0]
        
        dp1_no1 = 0
        dp2_no1 = 0
        dp1_t1 = 0
        dp2_t1 = nums[0]
        for n in nums[1:] :
            # take 
            new_dp_no1 = n + dp1_no1
            new_dp_t1 = n + dp1_t1
            # don't take
            new_dp_no1 = max(new_dp_no1, dp2_no1)
            new_dp_t1 = max(new_dp_t1, dp2_t1)

            # update
            dp1_no1 , dp2_no1 = dp2_no1, new_dp_no1
            dp1_t1  , dp2_t1  = dp2_t1 , new_dp_t1
        return max(dp1_t1, dp2_no1)

# optimized by given ans
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :return nums[0]

        def rob_max(nums: List[int]) -> int:
            dp1 = 0
            dp2 = 0
            for n in nums :
                # take this house
                new_dp = n + dp1
                # don't take this house
                new_dp = max(new_dp, dp2)
                # update
                dp1, dp2 = dp2, new_dp
            return dp2
        return max(rob_max(nums[:-1]), rob_max(nums[1:]))


s = Solution()
print("ans :",s.rob([2,3,2])) # 3
print("ans :",s.rob([1,2,3,1])) # 4
print("ans :",s.rob([1,2,3])) # 3



