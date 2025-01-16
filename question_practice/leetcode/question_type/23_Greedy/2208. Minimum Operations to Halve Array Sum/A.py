# 2208. Minimum Operations to Halve Array Sum
# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/description/

from typing import List
import functools

# my 239ms Beats93.49%
import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half = sum(nums)/2
        nums = [-n for n in nums]
        heapq.heapify(nums)
        ans = 0
        s = 0
        while s < half :
            biggest_h = heapq.heappop(nums) / 2
            s -= biggest_h
            heapq.heappush(nums, biggest_h)
            ans += 1
        return ans

# given ans
# exactly the same

s = Solution()
print("ans :",s.halveArray([5,19,8,1])) # 3
print("ans :",s.halveArray([3,8,20])) # 3



