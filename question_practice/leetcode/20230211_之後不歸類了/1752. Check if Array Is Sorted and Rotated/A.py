# 1752. Check if Array Is Sorted and Rotated
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description

from typing import List
import functools

# my 
class Solution:
    def check(self, nums: List[int]) -> bool:
        use_rotate = False
        last_num = nums[-1]
        for n in nums :
            if n < last_num :
                if use_rotate :
                    return False
                else :
                    use_rotate = True
            last_num = n
        return True



