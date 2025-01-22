# 2683. Neighboring Bitwise XOR
# https://leetcode.com/problems/neighboring-bitwise-xor/description

from typing import List
import functools
import operator

# my optimize 33ms Beats83.94%
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return 0 ^ functools.reduce(operator.xor, derived) == 0

# # my initial
# class Solution:
#     def doesValidArrayExist(self, derived: List[int]) -> bool:
#         # start from 0
#         prev = 0
#         for d in derived :
#             if 0 ^ prev == d :
#                 prev = 0
#             else :
#                 prev = 1
#         return prev == 0


# given ans
# same as optimize

s = Solution()
print("ans :",s.doesValidArrayExist([1,1,0])) # T
print("ans :",s.doesValidArrayExist([1,1])) # T
print("ans :",s.doesValidArrayExist([1,0])) # F



