# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive

from typing import List
from math import inf

# my 47ms Beats48.40%
    # (the faster ones use extra space, so violates the constraint)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)
        for i in range(n):
            now_n = nums[i]
            while now_n != None and 0 <= now_n <= n :
                # temp_n = nums[now_n]
                # nums[now_n] = None
                # now_n = temp_n
                nums[now_n], now_n = None, nums[now_n]
        
        for i, v in enumerate(nums) :
            if v != None :
                if i != 0 :
                    return i
        return len(nums)

s = Solution()
print("ans :",s.firstMissingPositive([1,2,0])) # 3
print("ans :",s.firstMissingPositive([3,4,-1,1])) # 2
print("ans :",s.firstMissingPositive([7,8,9,11,12])) # 1
print("ans :",s.firstMissingPositive([1,2,3])) # 4



