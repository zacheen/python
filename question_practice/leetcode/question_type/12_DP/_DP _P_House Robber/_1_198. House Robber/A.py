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
            

from functools import lru_cache
# class Solution:
def open(A):
    def dp(i):
        if i < 0 : # (base case) If the previous block doesn’t exist then regard it as 0 
            return (0, set([]))
        
        new_rev = A[i] # get the new revenue at this position

        dp_4_blocks_earlier_rev, dp_4_blocks_earlier_set = dp(i-4)
        # calculate the optimal revenue if open at this position
        open_rev = new_rev + dp_4_blocks_earlier_rev

        # calculate the optimal revenue if don't open at this position
        dp_prev_block = dp(i-1)
        dont_open_rev = dp_prev_block[0]

        if open_rev > dont_open_rev : # compare two possibilities
            # return both the revenue and the set of opened positions
            return (open_rev, dp_4_blocks_earlier_set | set([i]))
        else :
            return dp_prev_block
    return dp(len(A)-1)


print(open([1,1,1,9,9,0,0,1,1,1,9,9,9,0,0,0,0]))

s = Solution()
# print(s.rob([1,2,3]))
# print(s.rob([1,1,1,2,7,9,3,1]))
# print(s.rob([100,90,80,100,70,60,100,110]))
# print(s.rob([100,1,2,100,3,4,100,5]))