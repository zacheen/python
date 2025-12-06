# 198. House Robber
# https://leetcode.com/problems/house-robber/

from typing import List
# 0ms
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

    # return the path of robbed house          
    def rob_path(self, nums: List[int]) -> int:
        interval = 2
        dp = [0]*interval
        choice = []
        for n in nums :
            # take this house
            take = n + dp[-interval]

            # don't take this house
            dont_take = dp[-1]
            
            if take > dont_take :
                dp.append(take)
                choice.append(True)
            else :
                dp.append(dont_take)
                choice.append(False)
        
        # if there is a increase, it means that we picked this one
        now_i = len(choice)-1
        path = []
        while now_i >= 0:
            if choice[now_i] :
                path.append(now_i)
                now_i -= interval
            else:
                now_i -= 1

        if sum(nums[indx] for indx in path) != dp[-1]:
            raise Exception
        return dp[-1], path

s = Solution()
print(s.rob([1,2,3]))
print(s.rob([1,1,1,2,7,9,3,1]))
print(s.rob([100,90,80,100,70,60,100,110]))
print(s.rob([100,1,2,100,3,4,100,5]))

print(s.rob_path([1,2,3]))
print(s.rob_path([1,1,1,2,7,9,3,1]))
print(s.rob_path([100,90,80,100,70,60,100,110]))
print(s.rob_path([100,1,2,100,3,4,100,5]))