# 3516. Find Closest Person
# https://leetcode.com/problems/find-closest-person

from typing import List
from math import inf

# my 0ms
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff1 = abs(x-z)
        diff2 = abs(y-z)
        if diff1 == diff2 :
            return 0
        elif diff1 < diff2 :
            return 1
        else :
            return 2

s = Solution()
print("ans :",s.findClosest(x = 2, y = 7, z = 4)) # 1
print("ans :",s.findClosest(x = 2, y = 5, z = 6)) # 2



