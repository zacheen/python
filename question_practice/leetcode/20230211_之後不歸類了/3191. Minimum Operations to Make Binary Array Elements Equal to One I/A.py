# 3191. Minimum Operations to Make Binary Array Elements Equal to One I
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i

from typing import List
from math import inf

# my 87ms Beats89.20%
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cou = 0
        for i in range(len(nums)-2) :
            if nums[i] == 0 :
                # change next three, but this one actually don't have to change
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                cou += 1
        return cou if (nums[-1] and nums[-2]) else -1

# given ans 75ms Beats98.46%
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                res += 1
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
        return res if nums[-1] == 1 and nums[-2] == 1 else -1    

s = Solution()
print("ans :",s.minOperations([0,1,1,1,0,0])) # 3
print("ans :",s.minOperations([0,1,1,1])) # -1



