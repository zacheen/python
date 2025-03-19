# 1397. Find All Good Strings
# https://leetcode.com/problems/find-all-good-strings/description/

from typing import List
from math import inf
from functools import lru_cache, cache

# my 253ms Beats92.68%
MOD = 10**9 + 7
def cal_LPST(s): 
    len_s = len(s)
    lps = [0] * len_s
    pref_l = 0
    i = 1
    while i < len_s:
        if s[i] == s[pref_l]: # two pointer are the same word
            pref_l += 1
            lps[i] = pref_l
            i += 1
        else: # two pointer are not the same word
            if pref_l != 0: # find fast forward position
                pref_l = lps[pref_l - 1]
            else: # no fast forward position
                lps[i] = 0
                i += 1
    return lps

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        ord_a = ord('a')
        def str2int(s):
            return [ord(c)-ord_a for c in s]
        s1 = str2int(s1)
        s2 = str2int(s2)
        evil = str2int(evil)

        lps = cal_LPST(evil)

        len_p = len(evil)
        limit_i = n-1
        @cache
        def dp(now_i, lim_fr, lim_en, p_i) :
            ret = 0
            fr = 0
            en = 25
            if lim_fr :
                fr = s1[now_i]
            if lim_en :
                en = s2[now_i]
            for poss_n in range(fr, en+1) :
                # calculate different p_i for different poss_n
                new_pi = p_i
                while new_pi > 0 and poss_n != evil[new_pi]: # two pointer are not the same word
                    new_pi = lps[new_pi - 1]
                if poss_n == evil[new_pi]: # two pointer are the same word
                    new_pi += 1
                    if new_pi == len_p: # Match found
                        continue

                if now_i == limit_i :
                    ret += 1
                else :
                    new_f = poss_n == fr and lim_fr
                    new_e = poss_n == en and lim_en
                    ret += dp(now_i+1, new_f, new_e, new_pi)
            return ret%MOD
        return dp(0, True, True, 0)

# given ans
# (cal all comb from 'aaa...' to s2) - (all comb from 'aaa...' to s1) + (s1 res)
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        mod = 10 ** 9 + 7
        def convert_str_to_num(s: str) -> int:
            return ord(s) - ord("a")
        
        num1, num2, evil_num = list(map(convert_str_to_num, s1)), tuple(map(convert_str_to_num, s2)), tuple(map(convert_str_to_num, evil))
        def prefix_function(tup: tuple) -> List[int]:
            l = len(tup)
            lps = [0 for _ in range(l)]
            for i in range(1, l):
                j = lps[i - 1]
                while j > 0 and tup[i] != tup[j]: j = lps[j - 1]
                if tup[i] == tup[j]: j += 1
                lps[i] = j
            return lps

        kmp = prefix_function(evil_num)

        @cache
        def dp(pos: int, tight: True, match_number: int, num: tuple) -> int:
            if match_number == len(evil_num): return 0
            if pos == n: return 1
            res = 0
            bound = num[pos] if tight else 26
            for i in range(bound + 1):
                if i == 26: continue
                new_tight = i == bound
                j = match_number
                while j > 0 and evil_num[j] != i:
                    j = kmp[j - 1]
                if evil_num[j] == i: j += 1
                res += dp(pos + 1, new_tight, j, num)
            return res % mod

        i = n - 1
        while i >= 0 and num1[i] == 0:
            num1[i] = 25
            i -= 1
        if i >= 0: 
            num1[i] -= 1
        else: 
            return dp(0, True, 0, num2) % mod
        
        return (dp(0, True, 0, num2) - dp(0, True, 0, tuple(num1))) % mod

s = Solution()
# print("ans :",s.findGoodStrings(n = 2, 
#     s1 = "aa", s2 = "da", evil = "b")) # 51
# print("ans :",s.findGoodStrings(n = 8, 
#     s1 = "leetcode", s2 = "leetgoes", evil = "leet")) # 0
# print("ans :",s.findGoodStrings(n = 2, 
#     s1 = "gx", s2 = "gz", evil = "x")) # 2
# print("ans :",s.findGoodStrings(n = 3, 
#     s1 = "szc", s2 = "zyi", evil = "p")) # 4357
print("ans :",s.findGoodStrings(n = 3, 
    s1 = "abc", s2 = "abc", evil = "d")) # 4357



