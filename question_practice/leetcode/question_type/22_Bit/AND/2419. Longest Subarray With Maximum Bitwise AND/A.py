# 2419. Longest Subarray With Maximum Bitwise AND
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and

from typing import List
from math import inf

# my 19ms Beats91.72%
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # "maximum possible bitwise AND" must be "the biggest number"
        max_n = max(nums)
        ans = 0
        cnt = 0
        for n in nums :
            if n == max_n :
                cnt += 1
                if cnt > ans :
                    ans  = cnt
            else :
                cnt = 0
        return ans 

s = Solution()
print("ans :",s.longestSubarray([1,2,3,3,2,2])) # 2
print("ans :",s.longestSubarray([1,2,3,4])) # 1



