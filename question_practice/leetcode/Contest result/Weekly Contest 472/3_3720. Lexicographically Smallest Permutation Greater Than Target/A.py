# 3720. Lexicographically Smallest Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/description/

from typing import List
from math import inf
from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # since the max length of s is 300, we loop through all the permutations of s
        s_cnt = Counter(s)
        ans = []
        def find_smallest(i, is_bigger):
            nonlocal ans
            if i == len(s):
                if is_bigger :
                    return True
                else :
                    return False
            st_c = 'a' if is_bigger else target[i]
            for c in list(chr(i) for i in range(ord(st_c), ord('z')+1)) :
                if s_cnt[c] :
                    s_cnt[c] -= 1
                    if find_smallest(i+1, is_bigger or c > st_c) :
                        ans.append(c)
                        return True
                    s_cnt[c] += 1
            return False
        
        if find_smallest(0, False) :
            return "".join(ans[::-1])
        else :
            return ""  
            

s = Solution()
print("ans :",s.lexGreaterPermutation(s = "abc", target = "bba")) # bca
print("ans :",s.lexGreaterPermutation(s = "leet", target = "code")) # eelt
print("ans :",s.lexGreaterPermutation(s = "baba", target = "bbaa")) # ""
print("ans :",s.lexGreaterPermutation(s = "aab", target = "abb")) # "baa"
