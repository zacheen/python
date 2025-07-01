# 322. Coin Change
# https://leetcode.com/problems/coin-change/description/

from math import inf

# my practice again : 290ms Beats98.74%
class Solution:
    def coinChange(self, nums, target):
        dp = [0]
        for i in range(1,target+1):
            min_cou = inf
            for n in nums :
                if (pre_i:=i-n) >= 0 and (cou:=dp[pre_i]) < min_cou:
                    min_cou = cou
            dp.append(min_cou+1)
        # print(dp)
        return dp[-1] if dp[-1] != inf else -1
    
# this is slower, not sure why
class Solution:
    def coinChange(self, nums, target):
        dp = [0]
        for i in range(1,target+1):
            dp.append( min((dp[pre_i] for n in nums if (pre_i := i-n) >= 0), default = inf) +1)
        return dp[-1] if dp[-1] != inf else -1

s = Solution()
print(s.coinChange([1,2,5], 11))
print(s.coinChange([2,5,10,1], 27))
print(s.coinChange([1], 0))



