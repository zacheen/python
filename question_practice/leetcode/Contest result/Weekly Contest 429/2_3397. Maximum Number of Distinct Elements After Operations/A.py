# 3397. Maximum Number of Distinct Elements After Operations
# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description/

from typing import List
import functools

# my 737ms Beats100.00%
import math
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_num = nums[0]-(k+1)
        ans_count = 0
        for n in nums :
            if min_num < n+k :
                ans_count += 1
                min_num = max(min_num+1, n-k)
        return ans_count
    
s = Solution()
print(s.minimumOperations())



