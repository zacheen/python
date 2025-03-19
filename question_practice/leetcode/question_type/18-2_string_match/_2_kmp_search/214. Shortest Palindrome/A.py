# 214. Shortest Palindrome
# https://leetcode.com/problems/shortest-palindrome/description/

from typing import List
from math import inf

# my 55ms Beats57.60%
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

def kmp_search_pre_l(arr, pattern):
    if not pattern: # pattern == ""
        return [0]*len(arr)
    len_a = len(arr)
    len_p = len(pattern)

    # Precompute the LPS array
    lps = cal_LPST(pattern)
    
    # Search for the pattern in arr
    pre_l = [0]*len_a
    p_i = 0
    for a_i, a_c in enumerate(arr + '*'*len_a):
        while p_i > 0 and a_c != pattern[p_i]: # two pointer are not the same word
            pre_l[a_i-p_i] = p_i
            p_i = lps[p_i - 1]
        if a_c == pattern[p_i]: # two pointer are the same word
            p_i += 1
            if p_i == len_p: # Match found
                front_indx = a_i-p_i+1
                pre_l[front_indx] = p_i
                p_i = lps[p_i - 1]
    return pre_l

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "" : return s
        pre_l = kmp_search_pre_l(s[::-1],s)
        for i, l in enumerate(pre_l) :
            if len(s)-i-l == 0 :
                return s[:l-1:-1]+s

s = Solution()
print("ans :",s.shortestPalindrome("aacecaaa")) # aaacecaaa
print("ans :",s.shortestPalindrome("abcd")) # dcbabcd
print("ans :",s.shortestPalindrome("ababbbabbaba")) 
                         # ababbabbbababbbabbaba



