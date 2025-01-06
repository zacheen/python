# 3411. Maximum Subarray With Equal Products
# https://leetcode.com/problems/maximum-subarray-with-equal-products/description/

from typing import List
import functools

# my 31ms Beats100.00%
# fail : math, don't know the regulation
    # I thought is greedy
import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 1
        for l_i, l_n in enumerate(nums):
            prod = l_n
            gcd_val = l_n
            lcm_val = l_n
            for r_i, r_n in enumerate(nums[l_i+1:]):
                prod *= r_n
                gcd_val = math.gcd(gcd_val, r_n)
                lcm_val = math.lcm(lcm_val, r_n)
                if prod == gcd_val*lcm_val :
                    ans = max(ans, (r_i)+2)
        return ans

# given ans

s = Solution()
print("ans :",s.maxLength([1,2,1,2,1,1,1])) # [1, 2, 1, 1, 1] : 5
print("ans :",s.maxLength([2,3,4,5,6])) # [3,4,5] : 3
print("ans :",s.maxLength([1,2,3,1,4,5,1])) # 5



