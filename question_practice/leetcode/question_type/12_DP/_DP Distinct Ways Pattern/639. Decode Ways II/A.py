# 639. Decode Ways II
# https://leetcode.com/problems/decode-ways-ii/description/
    # '*' 不可以是0

from typing import List
from math import inf
from functools import cache

# my 230ms Beats84.21%
MOD = 10**9 + 7
class Solution:
    def numDecodings(self, s: str) -> int:
        len_s = len(s)
        @cache
        def dp(now_i):
            if now_i == len_s :
                return 1
            now_c = s[now_i]
            next_i = now_i+1
            if now_c == '0' :
                return 0
            elif now_c == '*' :
                ret = 0
                # as a first digit of two digit
                if next_i < len_s :
                    next_c = s[next_i]
                    if next_c == '*' : # include 0
                        ret = 15*dp(now_i+2)
                    elif next_c <= '6' : # include 0
                        # can be 1,2
                        ret = 2*dp(now_i+2)
                    else :
                        # can only be 1
                        ret = dp(now_i+2)
                # as a single digit
                # can be 1~9
                ret += 9*dp(now_i+1)
            else : # 1~9
                # as a first digit of two digit
                ret = 0
                if next_i < len_s :
                    next_c = s[next_i]
                    if next_c == "*" :
                        if now_c == '1' :
                            ret = 9*dp(now_i+2)
                        elif now_c == '2' :
                            ret = 6*dp(now_i+2)
                    else :
                        merge_num = now_c + s[next_i]
                        if merge_num <= '26' :
                            ret = dp(now_i+2)
                # as a single digit
                ret += dp(now_i+1)
            return ret%MOD
        return dp(0)

s = Solution()
print("ans :",s.numDecodings("*")) # 9
print("ans :",s.numDecodings("1*")) # 18
print("ans :",s.numDecodings("2*")) # 15
print("ans :",s.numDecodings("*1")) # 11
print("ans :",s.numDecodings("*2")) # 11

print("ans :",s.numDecodings("**")) # 



