# 3180. Maximum Total Reward Using Operations I
# https://leetcode.com/problems/maximum-total-reward-using-operations-i

from typing import List
from math import inf

# my modify template knapsack_01_reach v1 : 159ms Beats95.09%
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        max_tar = (rewardValues[-1]*2)-1 # tricky 

        dp = [True] + [False]*(max_tar)
        for num in rewardValues:
            for pre_i in range(num-1, -1, -1): # 從大到小
                if dp[pre_i] :
                    dp[pre_i+num] = True

        for i in range(len(dp)-1, -1, -1):
            if dp[i] :
                return i

# my modify template knapsack_01_reach v2 : 260ms Beats92.64%
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))

        can_comb_set = {0}  # 裡面紀錄目前可以的組合
        for num in rewardValues:
            can_comb_set |= set( s+num for s in can_comb_set if s < num )

        return max(can_comb_set)

s = Solution()
print("ans :",s.maxTotalReward([1,1,3,3])) # 
print("ans :",s.maxTotalReward([1,6,4,3,2])) # 
print("ans :",s.maxTotalReward()) # 



