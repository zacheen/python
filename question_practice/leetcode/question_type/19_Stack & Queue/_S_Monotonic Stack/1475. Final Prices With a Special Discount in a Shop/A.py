# 1475. Final Prices With a Special Discount in a Shop
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/

from typing import List
import functools

# my practice again : 2ms Beats61.45%
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        for i, p in enumerate(prices) :
            while stack and prices[stack[-1]] >= p :
                prices[stack.pop()] -= p
            stack.append(i)
        return prices

s = Solution()
# print("ans :",s.finalPrices(prices = [8,4,6,2,3])) # [4,2,4,2,3]
# print("ans :",s.finalPrices(prices = [1,2,3,4,5])) # [1,2,3,4,5]
# print("ans :",s.finalPrices(prices = [6,8,4,2]))
