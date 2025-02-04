# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description

from typing import List
import functools

# my 0ms Beats100.00%
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0
        inc_fin = dec_fin = nums[0]
        inc_len = dec_len = 0
        for n in nums :
            if n > inc_fin :
                inc_len += 1
            else :
                if inc_len > ans :
                    ans = inc_len
                inc_len = 1
            inc_fin = n

            if n < dec_fin :
                dec_len += 1
            else :
                if dec_len > ans :
                    ans = dec_len
                dec_len = 1
            dec_fin = n
        return max(ans, inc_len, dec_len)

# given ans
class Solution:
    # Similar to 978. Longest Turbulent Subarray
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        ans = 1
        increasing = 1
        decreasing = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing += 1
                decreasing = 1
            elif nums[i] < nums[i - 1]:
                decreasing += 1
                increasing = 1
            else:
                increasing = 1
                decreasing = 1
            ans = max(ans, increasing, decreasing)
        return ans

s = Solution()
print("ans :",s.longestMonotonicSubarray([1,4,3,3,2])) # 2
print("ans :",s.longestMonotonicSubarray([3,3,3,3])) # 1
print("ans :",s.longestMonotonicSubarray([3,2,1])) # 3
print("ans :",s.longestMonotonicSubarray([1,9,7,1])) # 3



