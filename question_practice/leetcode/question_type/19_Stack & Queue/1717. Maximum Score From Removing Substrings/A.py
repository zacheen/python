# 1717. Maximum Score From Removing Substrings
# https://leetcode.com/problems/maximum-score-from-removing-substrings

from typing import List
from math import inf

# my v2 opt : 162ms Beats93.55%
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x >= y :
            high_c_1 = "a"
            high_c_2 = "b"
            high_sc = x
            low_c_1 = "b"
            low_c_2 = "a"
            low_sc = y
        else :
            high_c_1 = "b"
            high_c_2 = "a"
            high_sc = y
            low_c_1 = "a"
            low_c_2 = "b"
            low_sc = x
        
        stack = []
        ans = 0
        s += "|"
        for c in s :
            if c == high_c_2 :
                if stack and stack[-1] == high_c_1 :
                    stack.pop()
                    ans += high_sc
                else :
                    stack.append(c)
            elif c == high_c_1 :
                stack.append(c)
            else : # 其他字所以斷掉
                # given ans opt : 因為這裡只會出現 low_c 這種情況
                    # 所以只要 Count(stack)，再 min(cnt.values()) 就可以取得有幾種組合了
                new_stack_cnt = 0
                for c in stack :
                    if c == low_c_2 :
                        if new_stack_cnt :
                            new_stack_cnt -= 1
                            ans += low_sc
                    else :
                        new_stack_cnt += 1
                stack = []
        return ans

# my v1 323ms Beats23.22%
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x >= y :
            sco_big = "ab"
            big = x
            sco_sma = "ba"
            sma = y
        else :
            sco_big = "ba"
            big = y
            sco_sma = "ab"
            sma = x
        
        stack = ""
        ans = 0
        s += "|"
        for c in s :
            if c == "a" or c == "b" :
                stack += c
                if stack[-2:] == sco_big :
                    stack = stack[:-2]
                    ans += big
            else :
                # 其他字所以斷掉
                new_stack = ""
                for c in stack :
                    new_stack += c
                    if new_stack[-2:] == sco_sma :
                        new_stack = new_stack[:-2]
                        ans += sma
                stack = ""
        return ans

s = Solution()
# print("ans :",s.maximumGain(s = "cdbcbbaaabab", x = 4, y = 5)) # 19
# print("ans :",s.maximumGain(s = "aabbaaxybbaabb", x = 5, y = 4)) # 20

print("ans :",s.maximumGain(s = "aaababbb", x = 4, y = 5)) # 17
# print("ans :",s.maximumGain()) # 



