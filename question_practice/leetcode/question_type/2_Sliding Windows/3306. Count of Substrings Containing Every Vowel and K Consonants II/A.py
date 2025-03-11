# 3306. Count of Substrings Containing Every Vowel and K Consonants II
# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii

from typing import List
from math import inf

# my 1148ms Beats90.75%
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vow_l = ['a','e','i','o','u']
        v_cout = {vow:0 for vow in vow_l}

        next_con_len = [0]
        cou = 0
        for c in word[::-1] : 
            if c in vow_l :
                cou += 1
            else :
                cou = 0
            next_con_len.append(cou)
        next_con_len.reverse()

        cou_acc = 0
        con_cou = 0
        r = -1
        ans_c = 0
        for l_c in word :
            while cou_acc < 5 or con_cou < k:
                r += 1
                if r == len(word) :
                    return ans_c
                now_r = word[r]
                if now_r in v_cout :
                    v_cout[now_r] += 1
                    if v_cout[now_r] == 1 :
                        cou_acc += 1
                else :
                    con_cou += 1
                
            if con_cou == k :
                ans_c += 1
                ans_c += next_con_len[r+1]
            
            if l_c in v_cout :
                v_cout[l_c] -= 1
                if v_cout[l_c] == 0 :
                    cou_acc -= 1
            else :
                con_cou -= 1

s = Solution()
print("ans :",s.countOfSubstrings(word = "aeioqq", k = 1)) # 0
print("ans :",s.countOfSubstrings(word = "aeiou", k = 0)) # 1
print("ans :",s.countOfSubstrings(word = "ieaouqqieaouqq", k = 1)) # 3
print("ans :",s.countOfSubstrings(word = "iqeaouqi", k = 2)) # 3




