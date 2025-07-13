# 3614. Process String with Special Operations II
# https://leetcode.com/problems/process-string-with-special-operations-ii

from typing import List
from math import inf

# my 328ms Beats94.24%
class Solution:
    def processStr(self, s: str, k: int) -> str:
        total_len = 0
        for c in s :
            if c == "*":
                if total_len >= 1 :
                    total_len -= 1
            elif c == "#":
                total_len *= 2
            elif c == "%":
                pass
            else :
                total_len += 1

        if k >= total_len :
            return "."
        
        for c in s[::-1] :
            if c == "*":
                total_len += 1
            elif c == "#":
                # if total_len&1 :
                #     raise Exception
                total_len //= 2
                if k >= total_len :
                    k -= total_len
            elif c == "%":
                k = total_len -k -1
            else :
                if total_len-1 == k :
                    return c
                else :
                    total_len -= 1

s = Solution()
print("ans :",s.processStr(s = "a#b%*", k = 1)) # "a"
print("ans :",s.processStr(s = "cd%#*#", k = 3)) # "d"
print("ans :",s.processStr(s = "z*#", k = 0)) # "."

# 不夠扣
print("ans :",s.processStr(s = "*a", k = 0)) # "a"

