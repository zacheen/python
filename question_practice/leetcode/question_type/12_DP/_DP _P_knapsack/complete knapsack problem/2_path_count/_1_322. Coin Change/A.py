# 322. Coin Change
# https://leetcode.com/problems/coin-change/description/

from math import inf

# my practice again : 321ms Beats98.24%
class Solution:
    def coinChange(self, nums, target):
        dp=[0] + [inf]*target
        for n in nums:
            for i in range(n, len(dp)):
                if (t:=1+dp[i-n]) < dp[i]:
                    dp[i] = t
        if dp[target]==inf:
            return -1
        else :
            return dp[target]


s = Solution()
print(s.coinChange([1,2,5], 11))
print(s.coinChange([2,5,10,1], 27))
print(s.coinChange([1], 0))



