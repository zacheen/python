# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/description/

from typing import List
# 0ms
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



