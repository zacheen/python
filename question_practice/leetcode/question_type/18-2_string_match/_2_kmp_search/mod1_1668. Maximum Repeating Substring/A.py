# 1668. Maximum Repeating Substring
# https://leetcode.com/problems/maximum-repeating-substring/description/
    # 是 substring !! 所以要是連續的 

from typing import List
from math import inf

# my 0ms
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

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        arr = sequence
        len_w = len(word)
        pattern = word*(len(sequence) // len_w)
        if pattern == "" :
            return 0
        len_p = len(pattern)

        # Precompute the LPS array
        lps = cal_LPST(pattern)
        
        # Search for the pattern in arr
        ans = 0
        p_i = 0
        for a_i, a_c in enumerate(arr):
            while p_i > 0 and a_c != pattern[p_i]: # two pointer are not the same word
                p_i = lps[p_i - 1]
            if a_c == pattern[p_i]: # two pointer are the same word
                p_i += 1
                ans = max(ans, p_i//len_w)
                if p_i == len_p: # full size
                    return ans
        return ans

s = Solution()
# print("ans :",s.maxRepeating(sequence = "ababc", word = "ab")) # 2
# print("ans :",s.maxRepeating(sequence = "ababc", word = "ba")) # 1
# print("ans :",s.maxRepeating(sequence = "ababc", word = "ac")) # 0
print("ans :",s.maxRepeating(sequence = "a", word = "aa")) # 0
# print("ans :",s.maxRepeating(sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba", word = "aaaba")) # 5
#                                                 # aaabaaaabaaaabaaaabaaaaba


