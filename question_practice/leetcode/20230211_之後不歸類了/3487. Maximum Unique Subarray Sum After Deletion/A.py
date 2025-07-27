# 3487. Maximum Unique Subarray Sum After Deletion
# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion

from typing import List
from math import inf

# my 
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        pos_n = [n for n in nums if n >= 0]
        if len(pos_n) == 0 :
            return max(nums)
        else :
            return sum(set(pos_n))
        

s = Solution()
print("ans :",s.maxSum([1,2,3,4,5])) # 15
print("ans :",s.maxSum([1,1,0,1,1])) # 1
print("ans :",s.maxSum([1,2,-1,-2,1,0,-1])) # 3
print("ans :",s.maxSum([-100])) # -100



