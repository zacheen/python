# 2966. Divide Array Into Arrays With Max Difference
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference

from typing import List
from math import inf

# my 74ms Beats88.61%
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        for i in range(0, len(nums), 3) :
            if (nums[i+2]-nums[i]) > k :
                return []
        return list( nums[i:i+3] for i in range(0, len(nums), 3) )

s = Solution()
print("ans :",s.divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2)) # [[1,1,3],[3,4,5],[7,8,9]]
print("ans :",s.divideArray(nums = [2,4,2,2,5,2], k = 2)) # []
print("ans :",s.divideArray(nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14)) # OK
print("ans :",s.divideArray([2,2,2,10,20,30], 10)) # [2,2,2],[10,20,30]
# print("ans :",s.divideArray([])) # 



