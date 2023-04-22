from typing import List
import functools

# # my 
# class Solution:
#     def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
#         max_count = 0
#         max_indx = []
#         for div in divisors  :
#             this_div_count = [n%div for n in nums].count(0)
#             if this_div_count > max_count :
#                 max_count = this_div_count
#                 max_indx = [div]
#             elif this_div_count == max_count :
#                 max_indx.append(div)
#         # print(max_indx)
#         max_indx.sort()
#         return max_indx[0]

# given ans
    # 不應該用 append 直接取 min 就好了
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_count = -1
        max_indx = 0
        for div in divisors  :
            this_div_count = [n%div for n in nums].count(0)
            if this_div_count > max_count :
                max_count = this_div_count
                max_indx = div
            elif this_div_count == max_count :
                max_indx = min(max_indx, div)
        return max_indx
    
s = Solution()
print(s.maxDivScore(nums = [4,7,9,3,9], divisors = [5,2,3]))
print(s.maxDivScore(nums = [20,14,21,10], divisors = [5,7,5]))
print(s.maxDivScore(nums = [12], divisors = [10,16]))



