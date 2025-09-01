# 3021. Alice and Bob Playing Flower Game
# https://leetcode.com/problems/alice-and-bob-playing-flower-game

from typing import List
from math import inf

# my 
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        def cal_odd(n):
            return (n+1)//2
        def cal_even(n):
            return n//2
        
        # find the comb of x + y = odd (x,y can't be zero)
        # odd = odd + even or even + odd
        return cal_odd(n)*cal_even(m)+cal_even(n)*cal_odd(m)

s = Solution()
print("ans :",s.flowerGame(3,2)) # 3
print("ans :",s.flowerGame(1,1)) # 0
print("ans :",s.flowerGame(1,2)) # 1



