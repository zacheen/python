# 1518. Water Bottles
# https://leetcode.com/problems/water-bottles

from typing import List
from math import inf

# my 
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange :
            new_bottel = numBottles//numExchange
            numBottles -= new_bottel*numExchange
            numBottles += new_bottel
            ans += new_bottel
        return ans

s = Solution()
print("ans :",s.numWaterBottles(numBottles = 9, numExchange = 3)) # 13
print("ans :",s.numWaterBottles(numBottles = 15, numExchange = 4)) # 19
# print("ans :",s.numWaterBottles()) # 



