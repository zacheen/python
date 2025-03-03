# 2320. Count Number of Ways to Place Houses
# https://leetcode.com/problems/count-number-of-ways-to-place-houses/description/

from typing import List
from math import inf

# my 
MOD = 10**9+7
class Solution:
    def countHousePlacements(self, n: int) -> int:
        # only one side
        prev_take = 0
        prev_dont_take = 1
        for _ in range(n) :
            # take 
            new_prev_take = prev_dont_take
            # don't take
            new_prev_dont_take = (prev_dont_take + prev_take)%MOD
            # update
            prev_take, prev_dont_take = new_prev_take, new_prev_dont_take
        
        poss_cou = prev_take+prev_dont_take
        return (poss_cou*poss_cou)%MOD

s = Solution()
print("ans :",s.countHousePlacements(1)) # 4
print("ans :",s.countHousePlacements(2)) # 9



