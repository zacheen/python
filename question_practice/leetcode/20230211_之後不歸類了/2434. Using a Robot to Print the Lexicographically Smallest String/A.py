# 2434. Using a Robot to Print the Lexicographically Smallest String
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string

from typing import List
from math import inf
from collections import Counter

# # my v1 2165ms Beats5.01%
# class Solution:
#     def robotWithString(self, s: str) -> str:
#         list_t = []
#         cou_s = Counter(s)
#         ord_a = ord('a')
#         chr_ord = tuple( chr(i) for i in range(ord_a, ord_a+26) )
#         def check_smaller(c):
#             for now_c in chr_ord :
#                 if now_c == c :
#                     return False
#                 if cou_s[now_c] > 0 :
#                     return True

#         ans = []
#         for c in s :
#             cou_s[c] -= 1
#             list_t.append(c)
#             while list_t :
#                 if check_smaller(list_t[-1]) :
#                     break
#                 else :
#                     ans.append(list_t.pop())
#         return "".join(ans)
    
# my v2 131ms Beats98.21%
# opt : mem each pos smallest num, skip mem
class Solution:
    def robotWithString(self, s: str) -> str:
        # 每個位子往右看最小的 char 是什麼
        s_c = "z"
        ri_s_i = ["a"]*len(s)
        for i in range(len(s)-1, -1, -1) :
            if s[i] < s_c :
                s_c = s[i]
                if s_c == "a" :
                    break
            ri_s_i[i] = s_c

        list_t = []
        ans = []
        for now_c, now_sm in zip(s, ri_s_i) :
            while list_t and list_t[-1] <= now_sm:
                ans.append(list_t.pop())
            list_t.append(now_c)
        return "".join(ans) + "".join(list_t[::-1])

# given ans
# same v1 concept

s = Solution()
print("ans :",s.robotWithString("zza")) # "azz"
print("ans :",s.robotWithString("bac")) # "abc"
print("ans :",s.robotWithString("bdda")) # "addb"
print("ans :",s.robotWithString("bydizfve")) # "bdevfziy"



