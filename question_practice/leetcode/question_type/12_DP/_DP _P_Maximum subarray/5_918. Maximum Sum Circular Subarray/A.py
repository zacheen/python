# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/

from typing import List
from math import inf

import heapq
from itertools import accumulate

# my 213ms Beats5.04%
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        len_n = len(nums)
        max_ans = -inf
        l = [(inf, 0)]
        for r_i, now_s in enumerate(accumulate(nums*2)) :
            while l[0][1] < (r_i - len_n) :
                heapq.heappop(l)
            if (s:= now_s - l[0][0]) > max_ans : 
                max_ans = s
            heapq.heappush(l, (now_s, r_i))
        return max_ans

# given ans (Kadane's Algorithm) : 97ms Beats64.59%
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadane finds max and min subarray summ, circular sub amx is either max or (sum(nums) - min)
        if max(nums) < 0:
            return max(nums)
        
        currmin = currmax = max_ans = min_ans = nums[0]
        for num in nums[1:]:
            currmax = max(num, currmax + num)
            max_ans = max(max_ans, currmax)
            currmin = min(num, currmin + num)
            min_ans = min(min_ans, currmin)
        return max(max_ans, sum(nums) - min_ans)

s = Solution()
print("ans :",s.maxSubarraySumCircular([1,-2,3,-2])) # 3
print("ans :",s.maxSubarraySumCircular([5,-3,5])) # 10
print("ans :",s.maxSubarraySumCircular([-3,-2,-3])) # -2



