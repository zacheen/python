# 1394. Find Lucky Integer in an Array
# https://leetcode.com/problems/find-lucky-integer-in-an-array

from typing import List
from math import inf

# my 
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        return max( (n for n,c in cnt.items() if n==c), default = -1)

# given ans


s = Solution()
print("ans :",s.findLucky([2,2,3,4])) # 
print("ans :",s.findLucky([1,2,2,3,3,3])) # 
print("ans :",s.findLucky([2,2,2,3,3])) # 



