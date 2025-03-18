# 2401. Longest Nice Subarray
# https://leetcode.com/problems/longest-nice-subarray

from typing import List
from math import inf

# my inspire by given ans : 80ms Beats89.94%
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used_bit = 0
        l = 0
        ans = 0
        for r, now_n in enumerate(nums) :
            while now_n & used_bit > 0 :
                used_bit ^= nums[l]
                l += 1
            used_bit |= now_n
            ans = max(ans, r-l)
        return ans+1

# # my 1422ms Beats10.97%
# class Solution:
#     def longestNiceSubarray(self, nums: List[int]) -> int:
#         nums = [f'{n:b}'[::-1] for n in nums]
#         used_bit = [0]*30
#         l = 0
#         ans = 0
#         for r, num_l in enumerate(nums) :
#             for cou, now_c in enumerate(num_l):
#                 if now_c == "1" :
#                     used_bit[cou] += 1
#                     while used_bit[cou] == 2 :
#                         for pop_cou, pop_c in enumerate(nums[l]):
#                             if pop_c == "1" :
#                                 used_bit[pop_cou] -= 1
#                         l += 1
#             ans = max(ans, r-l+1)
#         return ans



s = Solution()
print("ans :",s.longestNiceSubarray([1,3,8,48,10])) # [3,8,48]
print("ans :",s.longestNiceSubarray([3,1,5,11,13])) # [3]
print("ans :",s.longestNiceSubarray([338970160,525086042,19212931,213753017,321613307,553272419,190837185,548628106,793546945,243936947])) # 



