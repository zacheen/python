# 2200. Find All K-Distant Indices in an Array
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array

from typing import List
from math import inf

# my 2ms Beats87.05%
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        len_n = len(nums)
        ans = []
        last_i = 0
        for i,n in enumerate(nums):
            if n == key :
                endi = i+k+1
                ans += list(range(max(last_i, i-k), min(endi, len_n)))
                last_i = endi
        return ans

s = Solution()
print("ans :",s.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1)) # [1, 2, 3, 4, 5, 6]
print("ans :",s.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2)) # [0, 1, 2, 3, 4]



