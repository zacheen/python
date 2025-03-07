# 2826. Sorting Three Groups
# https://leetcode.com/problems/sorting-three-groups/description/

from typing import List
from math import inf
from bisect import bisect_right

# my 
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        stack = [inf]
        for n in nums :
            if n >= stack[-1] :
                stack.append(n)
            else :
                stack[bisect_right(stack,n)] = n
        return len(nums) - len(stack)
s = Solution()
print("ans :",s.minimumOperations([2,1,3,2,1])) # 3
print("ans :",s.minimumOperations([1,3,2,1,3,3])) # 2
print("ans :",s.minimumOperations([2,2,2,2,3,3])) # 0
print("ans :",s.minimumOperations([1,3,1,2])) # 1



