# 3718. Smallest Missing Multiple of K
# https://leetcode.com/problems/smallest-missing-multiple-of-k

from typing import List
from math import inf

# my 0ms
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        set_n = set(nums)
        m = k
        while True :
            if m not in set_n :
                return m
            m += k

s = Solution()
print("ans :",s.missingMultiple(nums = [8,2,3,4,6], k = 2)) # 10
print("ans :",s.missingMultiple(nums = [1,4,7,10,15], k = 5)) # 5

