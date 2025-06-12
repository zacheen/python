# 3456. Find Special Substring of Length K
# https://leetcode.com/problems/find-special-substring-of-length-k/description/

from typing import List
from math import inf

# my 0ms
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        cou = 0
        prev_c = s[0]
        for c in s :
            if c == prev_c :
                cou += 1
            else :
                if cou == k :
                    return True
                cou = 1
            prev_c = c
        if cou == k :
            return True
        else :
            return False

s = Solution()
print("ans :",s.hasSpecialSubstring(s = "aaabaaa", k = 3)) # T
print("ans :",s.hasSpecialSubstring(s = "aaab", k = 3)) # T
print("ans :",s.hasSpecialSubstring(s = "baaa", k = 3)) # T
print("ans :",s.hasSpecialSubstring(s = "aaa", k = 3)) # T
print("ans :",s.hasSpecialSubstring(s = "abc", k = 2)) # F
print("ans :",s.hasSpecialSubstring(s = "aa", k = 1)) # F
print("ans :",s.hasSpecialSubstring(s = "aabcb", k = 1)) # T
# print("ans :",s.hasSpecialSubstring()) # 



