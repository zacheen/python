# 796. Rotate String
# https://leetcode.com/problems/rotate-string/description/

from typing import List
from math import inf

# my using template : 0ms
def cal_LPST(s): 
    len_s = len(s)
    lps = [0] * len_s
    pref_l = 0
    for i in range(1, len_s):
        while pref_l > 0 and s[i] != s[pref_l]: # two pointer are not the same word
            pref_l = lps[pref_l-1]
        if s[i] == s[pref_l]: # two pointer are the same word
            pref_l += 1
            lps[i] = pref_l
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
                front_indx = a_i-len_p+1
                pre_l[front_indx] = p_i
                p_i = lps[p_i - 1]
    return pre_l

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        pre_l = kmp_search_pre_l(s, goal)

        for i, l in enumerate(pre_l) :
            if i+l == len(s) :
                if s[:i] == goal[l:] :
                    return True
        return False   

# given ans : 0ms
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal+goal    

s = Solution()
print("ans :",s.rotateString(s = "abcde", goal = "cdeab")) # T
print("ans :",s.rotateString(s = "abcde", goal = "abced")) # F



