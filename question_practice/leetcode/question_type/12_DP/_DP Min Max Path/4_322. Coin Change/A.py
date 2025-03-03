import math

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

# 2022 05 21 再次練習
# 還是犯了思考邏輯的錯誤 執行時才發現錯誤
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
        
#         dp = [math.inf]*(amount+1)
#         dp[0] = 0
        
#         # coins.sort(reverse = True)
#         for c in coins :
#             for i in range(c, amount+1) :
#                 dp[i] = min(dp[i-c]+1, dp[i])
#             # print(dp)
#             # 不行 因為有可能後面的組合比較小 
#             # if dp[-1] != math.inf :
#             #     return dp[-1]
         
#         if dp[-1] != math.inf :
#             return dp[-1]
#         else :
#             return -1

# given ans 使用 math 解法
# Time Limit Exceeded ...
# https://www.cnblogs.com/grandyang/p/5138186.html
# class Solution:
#     def coinChange(self, coins, amount):
#         res = math.inf
#         n = len(coins)
#         coins.sort()

#         def helper(start, target, cur):
#             if start < 0 : return 
#             if target % coins[start] == 0 :
#                 res = min(res,cur+target//coins[start])
#                 return 
#             for i in range(target//coins[start],-1,-1):
#                 if cur+i >= res -1 : break
#                 helper(start-1, target-i*coins[start], cur+i)

#         helper(n-1,amount,0)
#         if res == math.inf :
#             return -1
#         else :
#             return res

s = Solution()
print(s.coinChange(coins = [1,2,5], amount = 11))
print(s.coinChange(coins = [2,5,10,1], amount = 27))
print(s.coinChange(coins = [1], amount = 0))



