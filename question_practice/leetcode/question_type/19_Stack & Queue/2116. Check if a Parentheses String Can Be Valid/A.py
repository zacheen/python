# 2116. Check if a Parentheses String Can Be Valid
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description

from typing import List
import functools

# my 79ms Beats78.96%
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 :
            return False
        
        def check(s_in, locked_in, check_c):
            stack = []
            for c, l in zip(s_in, locked_in) :
                if l == "1" :
                    if c == check_c :
                        stack.append(c)
                    elif not stack or c == stack.pop() :
                        return False
                else : # l == '0'
                    stack.append(l)
            return True
        
        return check(s, locked, "(") and check(s[::-1], locked[::-1], ")")  

# # given ans (much slower) 136ms Beats20.46%
# # same logic different implement method
# class Solution:
#     def canBeValid(self, s: str, locked: str) -> bool:
#         if len(s) % 2 == 1:
#             return False
#         def check(s: str, locked: str, isForward: bool) -> bool:
#             changeable = l = r = 0
#             for c, lock in zip(s, locked):
#                 if lock == '0':
#                     changeable += 1
#                 elif c == '(':
#                     l += 1
#                 else:    # c == ')'
#                     r += 1
#                 if isForward and changeable + l - r < 0:
#                     return False
#                 if not isForward and changeable + r - l < 0:
#                     return False
#             return True
#         return check(s, locked, True) and check(s[::-1], locked[::-1], False)

s = Solution()
print("ans :",s.canBeValid(s = "))()))", locked = "010100")) # T
print("ans :",s.canBeValid(s = "()()", locked = "0000")) # T
print("ans :",s.canBeValid(s = ")", locked = "0")) # F
print("ans :",s.canBeValid(s = "()", locked = "11")) # T
print("ans :",s.canBeValid(s = ")(", locked = "01")) # F
print("ans :",s.canBeValid(s = "(())", locked = "0101")) # T
# print("ans :",s.canBeValid(
#     "())))()(()(((())(()()))))((((()())(())",
#     "10101100010001001011000000110010100101"
# )) # T



