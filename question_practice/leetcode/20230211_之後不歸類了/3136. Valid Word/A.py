# 3136. Valid Word
# https://leetcode.com/problems/valid-word

from typing import List
from math import inf

# my 0ms
vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 : 
            return False
        vow_f = False
        con_f = False
        for c in word :
            if c.isalpha() :
                if c in vowels :
                    vow_f = True
                else :
                    con_f = True
            elif c.isnumeric():
                pass
            else :
                return False
        return vow_f and con_f

s = Solution()
print("ans :",s.isValid("234Adas")) # T
print("ans :",s.isValid("Ba")) # F
print("ans :",s.isValid("A3$e")) # F
print("ans :",s.isValid("aaae")) # F



