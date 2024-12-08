# 3371. Identify the Largest Outlier in an Array
# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/description/

from typing import List
import functools

# my 1369ms Beats93.22%
import bisect
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        sum_n = sum(nums) #2Spe+Oout
        nums.sort()
        for i in range(len(nums)-1,-1,-1) :
            Spe2 = sum_n-nums[i]
            if Spe2%2 != 0 :
                continue
            Spe = Spe2//2
            ret = bisect.bisect_left(nums, Spe)
            if nums[ret] == nums[i] : # !! avoid finding Out
                ret += 1
                if ret == len(nums) :
                    continue
            if nums[ret] == Spe :
                return nums[i]

# given ans 1465ms Beats74.71%
# using Counter to determine whether Spe inside
import math
from collections import Counter
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        ans = -math.inf
        summ = sum(nums)
        count = Counter(nums)

        for num in nums:
            withoutNum = summ - num
            if withoutNum % 2 == 0:
                specialSum = withoutNum // 2    # the sum of special numbers
                if count[specialSum] > (1 if num == specialSum else 0):
                    ans = max(ans, num)
        return ans

s = Solution()
print("ans :",s.getLargestOutlier(nums = [2,3,5,10])) # 10
print("ans :",s.getLargestOutlier(nums = [-2,-1,-3,-6,4])) # 4
print("ans :",s.getLargestOutlier(nums = [1,1,1,1,1,5,5])) # 5
print("ans :",s.getLargestOutlier(nums = [6,-31,50,-35,41,37,-42,13])) # -35
    # sum(6,-31,50,-35,41,37,-42) = 26 但是/2之後是Outlier



