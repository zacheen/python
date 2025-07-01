# 639. Decode Ways II
# https://leetcode.com/problems/decode-ways-ii/description/
    # '*' 不可以是0

from typing import List
from math import inf
from functools import cache

# my using template C_Knap_perm : 253ms Beats74.77%
MOD = 10**9+7
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1]
        if s[0] == '0' :
            dp.append(0)
        elif s[0] == '*' :
            dp.append(9)
        else :
            dp.append(1)

        for end_i in range(1,len(s)) :
            d1,d2 = s[end_i-1], s[end_i]
            cou = 0
            # single digit
            if '1' <= d2 <= '9' :
                cou = dp[-1]
            elif d2 == "*" :
                cou = dp[-1]*9
            
            # two digit
            if d1 == "*" :
                if d2 == "*" :
                    cou += dp[-2]*15 # 11~26 (20X)
                elif '0' <= d2 <= '6' :
                    cou += dp[-2]*2 # 1X or 2X 
                else :
                    cou += dp[-2] # 1X
            else :
                if d2 == "*" :
                    if d1 == "1" :
                        cou += dp[-2]*9 # 11~19 # 10 不能拆成 1, 0
                    elif d1 == "2" :
                        cou += dp[-2]*6 # 21~26 # 20 不能拆成 2, 0
                elif '10' <= s[end_i-1:end_i+1] <= '26' :
                    cou += dp[-2]
            dp.append(cou % MOD)
        return dp[-1]

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



