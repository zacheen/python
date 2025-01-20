# 1818. Minimum Absolute Sum Difference
# https://leetcode.com/problems/minimum-absolute-sum-difference/description/

from typing import List
import functools

from math import inf
import bisect
# my 239ms Beats71.26%
MOD = 10**9+7
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # ori_diff
        diff = list(abs(n1-n2) for n1,n2 in zip(nums1, nums2))
        # reduce diff amount
        nums1.sort()
        max_reduce = -inf
        for ori_diff, n2 in zip(diff, nums2) :
            # find the nearest two num
            find_i = bisect.bisect_left(nums1, n2)
            min_diff = inf
            if find_i < len(nums1) :
                min_diff = nums1[find_i]-n2
            find_i -= 1
            if find_i >= 0 :
                min_diff = min(min_diff, n2-nums1[find_i])
            max_reduce = max(max_reduce, ori_diff-min_diff)
        s = 0
        for n in diff :
            s = (s + n)%MOD
        # print(s, max_reduce)
        return (s-max_reduce)%MOD

# given ans
# same concept

s = Solution()
# print("ans :",s.minAbsoluteSumDiff(nums1 = [1,7,5], nums2 = [2,3,5])) # 3
# print("ans :",s.minAbsoluteSumDiff(nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4])) # 20
print("ans :",s.minAbsoluteSumDiff([5,4,7], [10,8,10])) # 9



