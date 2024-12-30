# 3379. Transformed Array
# https://leetcode.com/problems/transformed-array/description/

from typing import List
import functools

# my 36ms Beats99.81%
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for i, n in enumerate(nums) :
            tar = i+n
            while tar < 0 :
                tar += len(nums)
            while tar >= len(nums) :
                tar -= len(nums)
            ans[i] = nums[tar]
        return ans

# my opt, shorter but slower
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [ nums[(i+n)%len(nums)] for i, n in enumerate(nums) ]

# given ans
# same

s = Solution()
print(s.constructTransformedArray(nums = [3,-2,1,1]))
print(s.constructTransformedArray(nums = [-1,4,-1]))



