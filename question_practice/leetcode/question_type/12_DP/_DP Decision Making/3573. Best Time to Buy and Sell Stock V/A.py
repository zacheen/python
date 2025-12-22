# 3573. Best Time to Buy and Sell Stock V
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v

from typing import List
from math import inf
from functools import cache

# given ans
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [0] * n
        for _ in range(k):
            nrml, shrt = -prices[0], prices[0]
            for idx, (pre_dp, price) in enumerate(zip(dp.copy(), prices[1:])):
                # comp 1. not take this, 2. take normal, 3. take short sell
                dp[idx+1] = max(dp[idx], nrml+price, shrt-price)
                # nrml, shrt are the price to buy at
                nrml = max(nrml, pre_dp - price)
                shrt = max(shrt, pre_dp + price)
        return dp[-1]

# # my Time Limit Exceeded
# class Solution:
#     def maximumProfit(self, prices: List[int], k: int) -> int:
#         @cache
#         def dp(end_i, take_k):
#             if end_i <= 0 or take_k == 0 :
#                 return 0
            
#             # return the max profit of taking k from 0-now_i
#             ret = 0
#             end_p = prices[end_i]
#             for st_i, st_p in enumerate(prices[:end_i+1]):
#                 new_interval_rev = abs(st_p - end_p)
#                 new_best_total_rev = new_interval_rev + dp(st_i-1, take_k-1)
#                 if new_best_total_rev > ret :
#                     ret = new_best_total_rev
            
#             ret = max(ret, dp(end_i-1, take_k))
#             return ret
    
#         return dp(len(prices)-1, k)

# fail : since only one transaction each time      
# class Solution:
#     def maximumProfit(self, prices: List[int], k: int) -> int:
        # prices.sort()
        # print(prices[-k:], prices[:k])
        # return sum(prices[-k:]) - sum(prices[:k])

s = Solution()
print("ans :",s.maximumProfit(prices = [1,7,9,8,2], k = 2)) # 14
print("ans :",s.maximumProfit(prices = [12,16,19,19,8,1,19,13,9], k = 3)) # 36
print("ans :",s.maximumProfit([1,2,5,2,1], 2)) # 5
print("ans :",s.maximumProfit([8,4,15,7,4,7,2,14,15], 3)) # 28



