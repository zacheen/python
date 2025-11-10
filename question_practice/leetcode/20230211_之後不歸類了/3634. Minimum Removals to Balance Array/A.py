# 3634. Minimum Removals to Balance Array
# https://leetcode.com/problems/minimum-removals-to-balance-array/description/

from typing import List
from math import inf
from collections import Counter
from bisect import bisect_right

# Optimized solution
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # Only keep one elements left
        len_nums = len(nums)
        ans = len_nums - 1

        # find the available indx
        nums.sort()
        right = 0
        for left, n in enumerate(nums):
            target = n*k
            while right < len_nums and nums[right] <= target :
                right += 1
            # now right is not included in the range
            include_items = right - left
            # print(include_items)
            if (new_ans := len_nums - include_items) < ans :
                ans = new_ans
        return ans

# my 195ms Beats27.52%
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # Only keep one elements left
        len_nums = len(nums)
        ans = len_nums - 1

        # find the available indx
        nums.sort()
        for left, n in enumerate(nums):
            right = bisect_right(nums, n*k)-1
            include_items = right - left + 1
            # print(include_items)
            if (new_ans := len_nums - include_items) < ans :
                ans = new_ans
        return ans

s = Solution()
print("ans :",s.minRemoval(nums = [2,1,5], k = 2)) # 1
print("ans :",s.minRemoval(nums = [1,6,2,9], k = 3)) # 2
print("ans :",s.minRemoval(nums = [4,6], k = 2)) # 0



