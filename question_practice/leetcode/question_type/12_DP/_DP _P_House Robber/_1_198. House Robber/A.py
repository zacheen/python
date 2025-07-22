# 198. House Robber
# https://leetcode.com/problems/house-robber/

from typing import List

# my : 0ms
class Solution:
    def rob(self, nums: List[int]) -> int:
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
            

s = Solution()
# print(s.rob([1,2,3]))
# print(s.rob([1,1,1,2,7,9,3,1]))
# print(s.rob([100,90,80,100,70,60,100,110]))
print(s.rob([100,1,2,100,3,4,100,5]))
# print(s.rob([0,0,0,0,0,0,0,0,0]))
# print(s.rob([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))