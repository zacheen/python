# 2215. Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/667984107/

from typing import List
import functools

# my v1
# Beats 26.78%
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        return [[n1 for n1 in set_nums1 if n1 not in nums2] , [n2 for n2 in set_nums2 if n2 not in nums1]]

# given ans
# Beats 36.51%
class Solution:
    def findDifference(self, nums1, nums2):
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        return [list(set_nums1 - set_nums2), list(set_nums2 - set_nums1)]

# given ans

s = Solution()
print(s.findDifference())



