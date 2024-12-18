# 2182. Construct String With Repeat Limit
# https://leetcode.com/problems/construct-string-with-repeat-limit

from typing import List
import functools

# 161ms Beats94.20%
from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        ans = []
        char_indx_f = ord("a")
        char_indx_e = ord("z")
        next_i = char_indx_e
        for i in range(char_indx_e, char_indx_f-1,-1) :
            c = chr(i)
            next_i = min(next_i, i-1)
            while count[c] > repeatLimit :
                # print("add repeatLimit",c)
                ans.append(c*repeatLimit)
                count[c] -= repeatLimit

                while next_i >= char_indx_f and count[chr(next_i)] == 0:
                    next_i -= 1
                if next_i < char_indx_f :
                    return "".join(ans)
                # print("ins", 1, chr(next_i))
                ans.append(chr(next_i))
                count[chr(next_i)] -= 1
                
            if count[c] > 0 :
                # print("add",count[c],c)
                ans.append(c*count[c])
        return "".join(ans)

# given ans
# mine is better

s = Solution()
print("ans :",s.repeatLimitedString())



