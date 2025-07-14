# 1827. Minimum Operations to Make the Array Increasing
# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/

from typing import List
from math import inf

# my 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        last_n = 0
        ans = 0
        for n in nums :
            if n > last_n :
                last_n = n
            else :
                last_n += 1
                ans += last_n-n
        return ans

s = Solution()
print("ans :",s.minOperations([1,1,1])) # 3 to [1,2,3]
print("ans :",s.minOperations([1,5,2,4,1])) # 14 to [1,5,6,7,8]
print("ans :",s.minOperations([8])) # 0



