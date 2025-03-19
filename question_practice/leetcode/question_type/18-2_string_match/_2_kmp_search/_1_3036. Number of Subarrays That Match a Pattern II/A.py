# 3036. Number of Subarrays That Match a Pattern II
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/description/

from typing import List
from math import inf
from itertools import pairwise

# my using template : 183ms Beats96.72%
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

# 回傳 pattern 在 arr 中出現的起始位置 (要全部 pattern 符合)
def kmp_search(arr, pattern):
    if not pattern: # pattern == ""
        return range(len(arr)+1)
    len_p = len(pattern)

    # Precompute the LPS array
    lps = cal_LPST(pattern)
    
    # Search for the pattern in arr
    indices = []
    p_i = 0
    for a_i, a_c in enumerate(arr):
        while p_i > 0 and a_c != pattern[p_i]: # two pointer are not the same word
            p_i = lps[p_i - 1]
        if a_c == pattern[p_i]: # two pointer are the same word
            p_i += 1
            if p_i == len_p: # Match found
                indices.append(a_i-len_p+1) # cal front indx 
                p_i = lps[p_i - 1]
    return indices

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        pat_l = []
        for fro_n , back_n in pairwise(nums) :
            if fro_n == back_n :
                pat_l.append(0)
            elif fro_n < back_n : 
                pat_l.append(1)
            else :
                pat_l.append(-1)
        return len(kmp_search(pat_l, pattern))

s = Solution()
print("ans :",s.countMatchingSubarrays(nums = [1,2,3,4,5,6], pattern = [1,1])) # 4
print("ans :",s.countMatchingSubarrays(nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1])) # 2



