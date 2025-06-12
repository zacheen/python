# 3457. Eat Pizzas!
# https://leetcode.com/problems/eat-pizzas/description/

from typing import List
from math import inf, ceil

# my 147ms Beats97.19%
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        len_p = len(pizzas)
        odd_days = ceil(len_p/8)
        odd_s = sum(pizzas[-odd_days:])
        # print("odd", pizzas[-odd_days:])
        even_days = len_p//8
        even_s = sum(pizzas[-(even_days*2+odd_days):-odd_days:2])
        # print("even", pizzas[-(even_days*2+odd_days):-odd_days:2])
        return odd_s + even_s

s = Solution()
print("ans :",s.maxWeight([1,2,3,4,5,6,7,8])) # 14
print("ans :",s.maxWeight([2,1,1,1,1,1,1,1])) # 3



