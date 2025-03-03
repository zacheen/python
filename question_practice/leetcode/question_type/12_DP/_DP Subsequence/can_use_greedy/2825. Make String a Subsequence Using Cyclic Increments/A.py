# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/description

from typing import List
import functools

# # my 131ms Beats12.50%
# class Solution: 
#     def canMakeSubsequence(self, str1: str, str2: str) -> bool:
#         # ord("a") == 97
#         shift_c = 97 # ord("a")
#         def can_be_the_same(c1, c2):
#             n1 = ord(c1)
#             n2 = ord(c2)
#             for p_n1 in range(n1,n1+2) :
#                 if p_n1 > 122 : # ord("z") = 122
#                     p_n1 -= 26
#                 if p_n1 == n2 :
#                     return True
#             return False
        
#         # 到長度 l 當然包含愈多字愈好
#         indx_s2 = 0
#         for s1 in str1 :
#             if can_be_the_same(s1, str2[indx_s2]) :
#                 indx_s2 += 1
#                 if indx_s2 == len(str2) :
#                     return True
#         return False

# my v2 73ms Beats 65.28%
# optimize
class Solution: 
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # ord("a") == 97
        shift_c = 97 # ord("a")
        def can_be_the_same(c1, c2):
            if n1 == n2 :
                return True
            n1 = ord(c1)
            n2 = ord(c2)
            p_n1 = n1+1
            if p_n1 > 122 : # ord("z") = 122
                p_n1 -= 26
            if p_n1 == n2 :
                return True
            return False
        
        # 到長度 l 當然包含愈多字愈好
        indx_s2 = 0
        for s1 in str1 :
            if can_be_the_same(s1, str2[indx_s2]) :
                indx_s2 += 1
                if indx_s2 == len(str2) :
                    return True
        return False

# given ans 59ms Beats90.97%
# same concept but optimized
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0    # str2's index
        for c in str1:
            # print(c, chr(((ord(c) -96) % 26) + 97), str2[i])
            if c == str2[i] or chr(((ord(c) -96) % 26) + 97) == str2[i]:
                # print("fit")
                i += 1
                if i == len(str2):
                    return True
        return False

s = Solution()
print("ans :",s.canMakeSubsequence(str1 = "abc", str2 = "ad")) # True
print("ans :",s.canMakeSubsequence(str1 = "zc", str2 = "ad")) # True
print("ans :",s.canMakeSubsequence(str1 = "ab", str2 = "d")) # False
print("ans :",s.canMakeSubsequence(str1 = "d", str2 = "c")) # False



