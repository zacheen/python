# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/description/

from typing import List
from math import inf

# my 15ms Beats89.31%
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num :
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        if k > 0 :
            stack = stack[:-k]
        for i, c in enumerate(stack):
            if c == '0' :
                continue
            return "".join(stack[i:])
        # all zero or empty
        return "0"

s = Solution()
print("ans :",s.removeKdigits(num = "1432219", k = 3)) # 1219
print("ans :",s.removeKdigits(num = "10200", k = 1)) # 200
print("ans :",s.removeKdigits(num = "10", k = 2)) # 0
print("ans :",s.removeKdigits(num = "100", k = 1)) # 0
print("ans :",s.removeKdigits(num = "52660469", k = 2)) # 260469
