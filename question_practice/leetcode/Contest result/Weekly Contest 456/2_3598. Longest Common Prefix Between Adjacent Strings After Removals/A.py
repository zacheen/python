# 3598. Longest Common Prefix Between Adjacent Strings After Removals
# https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/description/

from typing import List
from math import inf
from itertools import pairwise

# my 417ms Beats99.76%
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        max_len = 0
        max_len_i = 0
        max_len_2 = 0
        for i, (w1, w2) in enumerate(pairwise(words)):
            if w1[:max_len_2] == w2[:max_len_2] :
                new_max_len = max_len_2
                if max_len <= len(w1) and w1[:max_len] == w2[:max_len] :
                    new_max_len = max_len
                for c1, c2 in zip(w1[new_max_len:], w2[new_max_len:]) :
                    if c1 == c2 :
                        new_max_len += 1
                    else :
                        break
                # update
                if new_max_len > max_len :
                    max_len_2 = max_len
                    max_len, max_len_i = new_max_len, i
                else :
                    max_len_2 = new_max_len
            # print(max_len, max_len_i, max_len_2, w1, w2)
        ans = []
        max_len_i_back = max_len_i+1
        end_i = len(words) - 1
        for i in range(len(words)) :
            if i == 0 or i == end_i :
                if i == max_len_i or i == max_len_i_back :
                    ans.append(max_len_2)
                else :
                    ans.append(max_len)
            else : # 左右兩邊都還有空間
                w1 = words[i-1]
                w2 = words[i+1]
                if i == max_len_i or i == max_len_i_back :
                    new_max_len = max_len_2
                else :
                    new_max_len = max_len
                if w1[:max_len] == w2[:max_len] :
                    for c1, c2 in zip(w1[max_len:], w2[max_len:]) :
                        if c1 == c2 :
                            new_max_len += 1
                        else :
                            break
                ans.append(new_max_len)
        return ans

s = Solution()
print("ans :",s.longestCommonPrefix(["jump","run","run","jump","run"])) # 3
print("ans :",s.longestCommonPrefix(["jump","run","runn","jump","runn"])) # 4
# print("ans :",s.longestCommonPrefix()) # 
# print("ans :",s.longestCommonPrefix(["dog","racer","car"])) # 0



