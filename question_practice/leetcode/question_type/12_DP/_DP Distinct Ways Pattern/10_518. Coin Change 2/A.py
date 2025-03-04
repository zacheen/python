# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/description/

# my practice again : 125ms Beats79.53%
class Solution:
    def change(self, amount, coins):
        dp = [1]+[0]*(amount)

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        # print(dp)
        return dp[amount]

s = Solution()
print(s.change(amount = 5, coins = [1,2,5]))
# print(s.change(amount = 5, coins = [2]))
# print(s.change(amount = 10, coins = [10]))
# print(s.change(amount = 32, coins = [1,2,4,8,16]))
