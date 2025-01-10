# 3407. Substring Matching Pattern
# https://leetcode.com/problems/substring-matching-pattern/description/

from typing import List
import functools

# my opt 7ms Beats100.00%
from math import inf
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        fro,back = p.split("*")
        
        fro_i = inf
        if fro == "" :
            fro_i = -inf
        else :
            for i in range(len(s)) :
                if s[i:i+len(fro)] == fro :
                    fro_i = i
                    break
        if fro_i == inf :
            return False
        
        if back == "":
            return True
        for i in range(len(s)-1, max(-1, fro_i+len(fro)-1), -1) :
            if s[i:i+len(back)] == back :
                return True
        return False 

# given ans
# same concept, but using library : find,rfind
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        l, r = p.split('*')
        n = len(s)
        pl, pr = s.find(l), s.rfind(r)
        if pl == -1 or pr == -1:
            return False
        return pr - pl >= len(l)

s = Solution()
print("ans :",s.hasMatch(s = "leetcode", p = "ee*e")) # T
print("ans :",s.hasMatch(s = "car", p = "c*v")) # F
print("ans :",s.hasMatch(s = "luck", p = "u*")) # T
print("ans :",s.hasMatch("cvc", "cv*vc")) # F
print("ans :",s.hasMatch("", "*")) # T
print("ans :",s.hasMatch("l", "l*")) # T
print("ans :",s.hasMatch("r", "*r")) # T
print("ans :",s.hasMatch("nrnrs", "*nn")) # F



