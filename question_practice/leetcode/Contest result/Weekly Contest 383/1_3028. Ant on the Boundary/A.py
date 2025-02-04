# 3028. Ant on the Boundary
# https://leetcode.com/problems/ant-on-the-boundary/description/

from typing import List
import functools

# my 
from itertools import accumulate
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        return sum(1 for now_s in accumulate(nums) if now_s == 0)

