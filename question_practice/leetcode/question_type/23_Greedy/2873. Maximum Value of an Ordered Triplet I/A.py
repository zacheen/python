# 2873. Maximum Value of an Ordered Triplet I
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i
# 2874. Maximum Value of an Ordered Triplet II
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

from typing import List
from math import inf

# my v2 optimized : 0ms
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_ans = 0
        n_i = nums[0]
        max_dif = 0
        for n_k in nums[1:]:
            if (new_a:=max_dif*n_k) > max_ans :
                max_ans = new_a
            if (new_d := n_i - n_k) > max_dif :
                max_dif = new_d
            if n_k > n_i :
                n_i = n_k
        return max_ans

# # my v1
# class Solution:
#     def maximumTripletValue(self, nums: List[int]) -> int:
#         max_ans = 0
#         for i in range(len(nums)):
#             n_i = nums[i]
#             for j in range(i+1, len(nums)) :
#                 n_j = nums[j]
#                 temp = (n_i-n_j)
#                 for k in range(j+1, len(nums)) :
#                     n_k = nums[k]
#                     if (new_a:=temp*n_k) > max_ans :
#                         max_ans = new_a
#         return max_ans


s = Solution()
print("ans :",s.maximumTripletValue([12,6,1,2,7])) # 77
print("ans :",s.maximumTripletValue([1,10,3,4,19])) # 133
print("ans :",s.maximumTripletValue([1,2,3])) # 0



