# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays

from typing import List
from math import inf

# my 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

s = Solution()
print("ans :",s.intersection([1,2,2,1],[2,2])) # [2]
print("ans :",s.intersection([4,9,5],[9,4,9,8,4])) # [9,4]



