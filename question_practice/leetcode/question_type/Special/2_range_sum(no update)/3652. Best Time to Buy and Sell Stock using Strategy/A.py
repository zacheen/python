# 3652. Best Time to Buy and Sell Stock using Strategy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy

from typing import List
from math import inf

# my 191ms Beats98.67%
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        ori_acc = [0]
        ori_sum = 0

        sell_acc = [0]
        sell_sum = 0
        
        for p, s in zip(prices, strategy) :
            ori_sum += p*s
            ori_acc.append(ori_sum)

            sell_sum += p
            sell_acc.append(sell_sum)

        diff = 0
        for st in range(len(prices)) :
            en = st + k # not include
            if en > len(prices) :
                break
            
            half = st + (k//2)
            # print(ori_acc[en], ori_acc[st], sell_acc[en], sell_acc[half])
            new_diff = -(ori_acc[en]-ori_acc[st]) + (sell_acc[en]-sell_acc[half])
            if new_diff > diff :
                diff = new_diff
        return ori_sum + diff

s = Solution()
print("ans :",s.maxProfit(prices = [4,2,8], strategy = [-1,0,1], k = 2)) # 10
print("ans :",s.maxProfit(prices = [5,4,3], strategy = [1,1,0], k = 2)) # 9
print("ans :",s.maxProfit([5,8], [-1,-1], 2)) # 8



