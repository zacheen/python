# 3396. Minimum Number of Operations to Make Elements in Array Distinct
# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/

from typing import List
import functools

# my 0ms Beats100.00%
import math
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i, n in enumerate(nums[::-1]) :
            if n in seen :
                # print((len(nums) - i))
                return math.ceil((len(nums) - i)/3)
            seen.add(n)
        return 0

# given ans
# mine is faster
# using len(set(nums)) == len(nums) to check all value is distinct
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        while len(set(nums)) < len(nums):
            nums = nums[3:]
            ans += 1
        return ans

s = Solution()
print(s.minimumOperations(nums = [1,2,3,4,2,3,3,5,7])) #2



