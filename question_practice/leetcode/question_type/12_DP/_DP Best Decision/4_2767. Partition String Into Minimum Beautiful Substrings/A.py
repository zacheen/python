# 2767. Partition String Into Minimum Beautiful Substrings
# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/description/

from typing import List
from math import inf
from functools import cache

# my 6ms Beats80.86%
now_min_5 = 1
pow_5 = set([1])
def get_5_pow(n):
    global now_min_5, pow_5
    while now_min_5 < n :
        now_min_5 *= 5
        pow_5.add(now_min_5)
    return pow_5

class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        if s[0] == '0' :return -1

        @cache
        def dp(now_i) :
            min_len = inf
            now_n = 0
            for i in range(now_i, len(s)) :
                now_n = now_n*2 + int(s[i])
                if now_n in get_5_pow(now_n) :
                    if (next_i:=i+1) == len(s) :
                        return 1
                    if s[next_i] == '1':
                        min_len = min(dp(i+1) + 1, min_len)
            return min_len
        ret = dp(0)
        if ret == inf :
            return -1
        else :
            return ret

# my dp for version : 3ms Beats 91.93%
now_min_5 = 1
pow_5 = set([1])
def get_5_pow(n):
    global now_min_5, pow_5
    while now_min_5 < n :
        now_min_5 *= 5
        pow_5.add(now_min_5)
    return pow_5
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        if s[0] == '0' :return -1 

        len_s = len(s)
        s = [0 if c == '0' else 1 for c in s]
        s += ["End"]
        # dp[i] : 到 s[i-1] 之前 符不符合規則
        dp = [0] + [inf]*len_s
        for st, now_n in enumerate(s[:-1]):
            # 從前面往後做 計算num會比較順
            if now_n == 0 or dp[st] == inf: 
                continue
            num = 0 
            for back_i in range(st,len_s):
                n = s[back_i]
                num = (num<<1) + n
                fur_dp_i = back_i+1
                # 尾數要是1 : 才會是奇數 (get_5_pow 都是奇數)
                # s[back_i+1] != 0 : 下一個開頭的數字不能是0
                if n == 1 and s[back_i+1] != 0 and dp[st]<dp[fur_dp_i] and num in get_5_pow(num) :
                    dp[fur_dp_i] = dp[st]+1
        return dp[-1] if dp[-1] != inf else -1


s = Solution()
# print("ans :",s.minimumBeautifulSubstrings("1011")) # 
# print("ans :",s.minimumBeautifulSubstrings("111")) # 
# print("ans :",s.minimumBeautifulSubstrings("0")) # 
# print("ans :",s.minimumBeautifulSubstrings("00001111001111")) # 
# print("ans :",s.minimumBeautifulSubstrings("101101111101")) # 
print("ans :",s.minimumBeautifulSubstrings("100111000110111")) # 



