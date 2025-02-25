# 327. Count of Range Sum
# https://leetcode.com/problems/count-of-range-sum/description

from typing import List
from math import inf

from bisect import bisect_left, bisect_right
from itertools import accumulate
from sortedcontainers import SortedList
# my 821ms Beats86.51%
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sorted_s = SortedList([0])
        ans_cou = 0
        for s in accumulate(nums) :
            left = s-upper
            right = s-lower
            ans_cou += sorted_s.bisect_right(right) - sorted_s.bisect_left(left)
            sorted_s.add(s)
        return ans_cou
    
# my 7092ms Beats5.10% (don't know why the speed varies from above version)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sorted_s = SortedList([0])
        ans_cou = 0
        for s in accumulate(nums) :
            left = s-upper
            right = s-lower
            ans_cou += bisect_right(sorted_s, right) - bisect_left(sorted_s, left)
            sorted_s.add(s)
        return ans_cou

# given ans 2
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumsum = [0] + list(accumulate(nums))
        # inclusive
        def mergesort(l,r):
            if l == r:
                return 0
            mid = (l+r)//2
            cnt = mergesort(l,mid) + mergesort(mid+1,r)
            print(l,r)
            
            i = j = mid+1
            _ = cumsum[l:mid+1]
            # O(n)
            for left in cumsum[l:mid+1]:
                while i <= r and cumsum[i] - left < lower:
                    i+=1
                while j <= r and cumsum[j] - left <= upper:
                    j+=1
                cnt += j-i
            cumsum[l:r+1] = sorted(cumsum[l:r+1])
            return cnt
        return mergesort(0,len(cumsum)-1)


s = Solution()
# print("ans :",s.countRangeSum(nums = [-2,5,-1], lower = -2, upper = 2)) # 3
print("ans :",s.countRangeSum(nums = [-2,5,-1,-2,5,-2,5], lower = -2, upper = 2)) # 3
# print("ans :",s.countRangeSum(nums = [0], lower = 0, upper = 0)) # 1



