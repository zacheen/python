# 3392. Count Subarrays of Length Three With a Condition
# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/

from typing import List
import functools

# my 
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            if (nums[i]+nums[i+2])*2 == nums[i+1] :
                ans += 1
        return ans

# given ans

s = Solution()
print("ans :",s.countSubarrays(nums = [1,2,1,4,1])) # 



