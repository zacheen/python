# 3066. Minimum Operations to Exceed Threshold Value II
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii

from typing import List
from math import inf
import heapq

# my 187ms Beats95.38%
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans_cou = 0
        while nums[0] < k :
            heapq.heapreplace(nums, heapq.heappop(nums)*2+nums[0])
            ans_cou += 1
        return ans_cou

s = Solution()
print("ans :",s.minOperations(nums = [2,11,10,1,3], k = 10)) # 2



