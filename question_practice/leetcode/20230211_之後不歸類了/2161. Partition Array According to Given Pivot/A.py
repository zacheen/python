# 2161. Partition Array According to Given Pivot
# https://leetcode.com/problems/partition-array-according-to-given-pivot

from typing import List
from math import inf

# my 
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        bef = []
        in_bet = []
        aft = []
        for n in nums :
            if n < pivot :
                bef.append(n)
            elif n == pivot :
                in_bet.append(n)
            else :
                aft.append(n)
        return bef + in_bet + aft

s = Solution()
print("ans :",s.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10)) # [9,5,3,10,10,12,14]



