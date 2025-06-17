# 3498. Reverse Degree of a String
# https://leetcode.com/problems/reverse-degree-of-a-string/description/

from typing import List
from math import inf

# my 7ms Beats76.75%
mem = {}
ord_a = ord('a')
for fro_i, rev_i in zip(range(26), range(26,0,-1)):
    mem[chr(ord_a+fro_i)] = rev_i

class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(mem[c]*(i+1) for i,c in enumerate(s))
    
s = Solution()
print("ans :",s.reverseDegree("abc")) # 26 + 50 + 72 = 148
print("ans :",s.reverseDegree("zaza")) # 1 + 52 + 3 + 104 = 160



