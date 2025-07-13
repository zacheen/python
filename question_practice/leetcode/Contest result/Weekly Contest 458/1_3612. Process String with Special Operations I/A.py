# 3612. Process String with Special Operations I
# https://leetcode.com/problems/process-string-with-special-operations-i

from typing import List
from math import inf

# my 
class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        for c in s :
            if c == "*":
                if ans :
                    ans.pop()
            elif c == "#":
                ans += ans
            elif c == "%":
                ans = ans[::-1]
            else :
                ans.append(c)
        return "".join(ans)

s = Solution()
print("ans :",s.processStr("a#b%*")) # "ba"
print("ans :",s.processStr("z*#")) # ""
# print("ans :",s.processStr()) # 



