# 2014. Longest Subsequence Repeated k Times
# https://leetcode.com/problems/longest-subsequence-repeated-k-times

from typing import List
from math import inf

# given ans : 7230ms Beats6.50% 
    # (I thought it would exceed time limit)
    # since : n < k * 8
        # if k = 2 then n at most = 16 (the longest Subsequence is 16/2 = 8)
        # if k = 5 then n at most = 40 (the longest Subsequence is 40/5 = 8)
    # thus the answer len is almost 8
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        len_s = len(s)
        def check(new_s):
            s_i = 0
            for _ in range(k) :
                for c in new_s :
                    while s_i < len_s :
                        if c == s[s_i] :
                            s_i += 1
                            break
                        else :
                            s_i += 1
                    else :
                        return False
            return True     

        # bfs
        poss_ch = list( chr(i) for i in range(ord('a'),ord('z')+1))
        q = [""]
        ans = ""
        while q :
            new_q = []
            for poss_s in q :
                for new_c in poss_ch :
                    new_s = poss_s + new_c
                    if check(new_s) :
                        ans = new_s # 剛好愈後面的愈大 且愈長
                        new_q.append(new_s)
            q = new_q
        return ans
        # dfs 不會比較快，因為我還是得先判斷前面的組合，決定是否繼續
            # 我知道 "zzz" 是目前最長的結果，我還是得判斷 "aaa"
            # 否則我得判斷 "aaaa", "aaab" ... 這樣數量更多

# given ans opt : only consider the char that is possible
    # 1754ms Beats32.52%
from collections import Counter
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        len_s = len(s)
        def check(new_s):
            s_i = 0
            for _ in range(k) :
                for c in new_s :
                    while s_i < len_s :
                        if c == s[s_i] :
                            s_i += 1
                            break
                        else :
                            s_i += 1
                    else :
                        return False
            return True     

        # bfs
        cou = Counter(s)
        # optimized here
        poss_ch = list( chr(i) for i in range(ord('a'),ord('z')+1) if cou[chr(i)] >= k )
        q = [""]
        ans = ""
        while q :
            new_q = []
            for poss_s in q :
                for new_c in poss_ch :
                    new_s = poss_s + new_c
                    if check(new_s) :
                        ans = new_s # 剛好愈後面的愈大 且愈長
                        new_q.append(new_s)
            q = new_q
        return ans

s = Solution()
print("ans :",s.longestSubsequenceRepeatedK(s = "letsleetcode", k = 2)) # let 
print("ans :",s.longestSubsequenceRepeatedK(s = "bb", k = 2)) # b
print("ans :",s.longestSubsequenceRepeatedK(s = "ab", k = 2)) # ""



