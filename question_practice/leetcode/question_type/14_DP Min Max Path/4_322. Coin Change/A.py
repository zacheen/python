# my 
# Runtime: 1710 ms, faster than 65.17% of Python3
# class Solution:
#     def coinChange(self, coins, amount):
#         if amount == 0 :
#             return 0
        
#         mem = [0]+[math.inf]*amount
#         coins.sort(reverse = True)  # 原本是因為想要省略 min  但失敗了  所以也不用sort
#         for coin in coins :
#             # print(coin)
#             for i in range(coin,len(mem)):
#                 # print(i, mem[i], mem[i] == None)
#                 if mem[i-coin] != math.inf :
#                     mem[i] = min(mem[i-coin]+1, mem[i])
#                 # 因為這些一定前面也會算過 (算過5寫入後 10就會被上面包含)
#                 # 所以 elif 其實可以省略
#                 elif (mem[i] == math.inf) and (i % coin == 0) :
#                     mem[i] = i // coin
        
#             # print(mem)
#         if mem[-1] == math.inf :
#             return -1
#         else :
#             return mem[amount]

# given ans
class Solution:
    def coinChange(self, coins, amount):
        # dp[i] := fewest # of coins to make up i
        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]

s = Solution()
print(s.coinChange(coins = [1,2,5], amount = 11))
print(s.coinChange(coins = [2,5,10,1], amount = 27))
print(s.coinChange(coins = [1], amount = 0))



