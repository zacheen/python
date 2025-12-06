# 3708. Longest Fibonacci Subarray
# https://leetcode.com/problems/longest-fibonacci-subarray/description/

from typing import List
from math import inf

# my 47ms Beats98.19%
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 2 # since len(nums) >= 3
        cnt = 2
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1] == nums[i+2] :
                cnt += 1
                if cnt > max_len :
                    max_len = cnt
            else :
                cnt = 2
        return max_len

s = Solution()
print("ans :",s.longestSubarray([1,1,1,1,2,3,5,1])) # nums[2..6] = [1, 1, 2, 3, 5]
print("ans :",s.longestSubarray([5,2,7,9,16])) # nums[0..4] = [5, 2, 7, 9, 16]

