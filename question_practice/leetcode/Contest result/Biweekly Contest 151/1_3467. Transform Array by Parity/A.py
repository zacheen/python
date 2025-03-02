# 3467. Transform Array by Parity
# https://leetcode.com/problems/transform-array-by-parity/description/

from typing import List
from math import inf
from collections import Counter

# my 0ms Beats100.00%
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # method one
        # cou = Counter(n%2 for n in nums)

        # method two (optimized)
        cou = [0,0]
        for n in nums :
            cou[n%2] += 1
        return [0]*cou[0]+[1]*cou[1]

s = Solution()
print("ans :",s.transformArray([4,3,2,1])) # [0,0,1,1]



