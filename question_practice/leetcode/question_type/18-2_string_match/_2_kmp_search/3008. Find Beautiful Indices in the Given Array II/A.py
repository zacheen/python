# 3008. Find Beautiful Indices in the Given Array II
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/description/

from typing import List
from math import inf
from bisect import bisect_right

# my 657ms Beats86.52%
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
                indices.append(a_i-p_i+1) # cal front indx 
                p_i = lps[p_i - 1]
    return indices

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_i = kmp_search(s, a)
        b_i = kmp_search(s, b)

        ans = []
        bp, bp_lim = 0, len(b_i)
        for each_a in a_i:
            while bp < bp_lim and b_i[bp]+k < each_a:
                bp += 1
            if bp < bp_lim and b_i[bp] <= each_a+k:
                ans.append(each_a)
        return ans

        # # using bisect to find position might be faster if a_i have less results
        # ans = []
        # for each_a in a_i :
        #     ins_r = bisect_right(b_i, each_a)
        #     if ins_r < len(b_i) :
        #         poss_b_i = b_i[ins_r]
        #         if poss_b_i - each_a <= k :
        #             ans.append(each_a)
        #             continue

        #     ins_l = ins_r-1
        #     if ins_l >= 0 :
        #         poss_b_i = b_i[ins_l]
        #         if each_a - poss_b_i <= k :
        #             ans.append(each_a)
        # return ans

# given ans : 39ms Beats99.44%
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # work around for test case specifically used to require KMP
        if len(set(a))==len(set(b))==len(set(s))==1:
            return [i for i in range(max(0,len(s)-(len(a)-1)))]

        i = s.find(a)
        j = s.find(b)
        res = []

        while i != -1 and j != -1:
            if abs(i - j) <= k:
                res.append(i)
                i = s.find(a, i + 1)
            elif i < j:
                i = s.find(a, i + 1)
            else:
                j = s.find(b, j + 1)
        return res

s = Solution()
print("ans :",s.beautifulIndices(
    s = "isawsquirrelnearmysquirrelhouseohmy", 
    a = "my", b = "squirrel", k = 15)) # [16,33]
print("ans :",s.beautifulIndices( s = "abcd", a = "a", b = "a", k = 4)) # 0



