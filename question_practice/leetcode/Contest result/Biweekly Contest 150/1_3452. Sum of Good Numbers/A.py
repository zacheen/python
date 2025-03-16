# 3452. Sum of Good Numbers
# https://leetcode.com/problems/sum-of-good-numbers/description/

from typing import List
from math import inf

# my 2ms Beats60.45%
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        len_n = len(nums)
        ans = 0
        for i, now_n in enumerate(nums):
            if (prev_i:=i-k) >= 0 :
                if nums[prev_i] >= now_n :
                    continue      
            if (back_i:=i+k) < len_n :
                if nums[back_i] >= now_n :
                    continue
            ans += now_n
        return ans

s = Solution()
print("ans :",s.sumOfGoodNumbers(nums = [1,3,2,1,5,4], k = 2)) # 
print("ans :",s.sumOfGoodNumbers(nums = [2,1], k = 1)) # 



