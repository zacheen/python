# 2465. Number of Distinct Averages
# https://leetcode.com/problems/number-of-distinct-averages/description/

from typing import List
from math import inf

# my 
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        ave_set = set()
        # print(nums[:mid], nums[:mid-1:-1])
        for n1,n2 in zip(nums[:mid], nums[:mid-1:-1]) :
            ave_set.add(n1+n2)
        # print(ave_set)
        return len(ave_set)




