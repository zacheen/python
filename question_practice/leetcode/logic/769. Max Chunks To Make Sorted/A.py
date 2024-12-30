# 769. Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/description

from typing import List
import functools

# my 0ms Beats100.00%
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans_cou = 0
        max_num = -1
        for i,n in enumerate(arr) :
            max_num = max(max_num, n)
            if i == max_num :
                ans_cou += 1
        return ans_cou

# given ans
# the same

s = Solution()
print("ans :",s.maxChunksToSorted())



