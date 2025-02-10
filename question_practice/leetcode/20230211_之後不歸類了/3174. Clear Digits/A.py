# 3174. Clear Digits
# https://leetcode.com/problems/clear-digits/description

from typing import List
from math import inf

# my
class Solution:
    def clearDigits(self, s: str) -> str:
        mem = [1]*len(s)
        char_indx_stack = []
        ord_0 = ord("0")
        ord_9 = ord("9")
        for i,c in enumerate(s) :
            if ord_9 >= ord(c) >= ord_0 :
                mem[i] = 0
                mem[char_indx_stack.pop()] = 0
            else :
                char_indx_stack.append(i)
        return "".join(c for show,c in zip(mem,s) if show)

# given ans : optimized directly stack c
class Solution:
    def clearDigits(self, s: str) -> str:
        char_stack = []
        for c in s :
            if c.isalpha() :
                char_stack.append(c)
            else :
                char_stack.pop()
        return "".join(char_stack)


s = Solution()
print("ans :",s.clearDigits("abc")) # "abc"
print("ans :",s.clearDigits("cb34")) # ""



