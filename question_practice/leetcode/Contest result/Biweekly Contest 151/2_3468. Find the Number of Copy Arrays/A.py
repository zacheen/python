# 3468. Find the Number of Copy Arrays
# https://leetcode.com/problems/find-the-number-of-copy-arrays/description/

from typing import List
from math import inf

# my 51ms Beats100.00%
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        l = -inf
        r = inf
        for ori, (b1,b2) in zip(original, bounds):
            l = max(l, b1 - ori)
            r = min(r, b2 - ori)
            if l > r :
                return 0
        return r - l + 1

s = Solution()
print("ans :",s.countArrays(original = [1,2,3,4], bounds = [[1,10],[2,9],[3,8],[4,7]])) # 4



