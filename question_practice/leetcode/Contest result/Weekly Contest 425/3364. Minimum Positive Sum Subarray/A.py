# 3364. Minimum Positive Sum Subarray 
# https://leetcode.com/problems/minimum-positive-sum-subarray/

from typing import List
import functools

# my 15ms Beats96.77%
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        max_sum = 10000001
        min_sum = max_sum
        len_nums = len(nums)
        for sta in range(len_nums):
            en = sta+l
            if en > len_nums :
                break
            now_sum = sum(nums[sta:en])
            if now_sum > 0 :
                min_sum = min(min_sum, now_sum)
            for nex in nums[en: min(sta+r, len_nums)]:
                now_sum += nex
                if now_sum > 0 :
                    min_sum = min(min_sum, now_sum)
        if min_sum == max_sum :
            return -1
        return min_sum

# given ans

s = Solution()
print("ans :",s.minimumSumSubarray(nums = [3, -2, 1, 4], l = 2, r = 3)) # 1
print("ans :",s.minimumSumSubarray(nums = [-2, 2, -3, 1], l = 2, r = 3)) # -1
print("ans :",s.minimumSumSubarray(nums = [1, 2, 3, 4], l = 2, r = 4)) # 3



