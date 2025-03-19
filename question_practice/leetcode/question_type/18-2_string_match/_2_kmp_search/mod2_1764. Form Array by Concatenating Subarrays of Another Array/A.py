# 1764. Form Array by Concatenating Subarrays of Another Array
# https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/description/

from typing import List
from math import inf

# my 0ms Beats100.00%
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
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        last_indx = len(groups)-1
        last_end = 0
        for cou, pattern in enumerate(groups) :
            len_p = len(pattern)

            # Precompute the LPS array
            lps = cal_LPST(pattern)
            
            # Search for the pattern in arr
            didnt_find = True
            p_i = 0
            for a_i, a_c in enumerate(nums[last_end:]):
                while p_i > 0 and a_c != pattern[p_i]: # two pointer are not the same word
                    p_i = lps[p_i - 1]
                if a_c == pattern[p_i]: # two pointer are the same word
                    p_i += 1
                    if p_i == len_p: # Match found
                        if cou == last_indx :
                            return True
                        last_end += a_i+1
                        didnt_find = False
                        break
            if didnt_find :
                return False
        return False

s = Solution()
print("ans :",s.canChoose(groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0])) # T
print("ans :",s.canChoose(groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2])) # F
print("ans :",s.canChoose(groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7])) # F
print("ans :",s.canChoose(groups = [[1,2,3,100],[3,4]], nums = [7,7,1,2,3,4,7,7])) # F



