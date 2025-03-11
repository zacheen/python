# 3474. Lexicographically Smallest Generated String
# https://leetcode.com/problems/lexicographically-smallest-generated-string/description/

from typing import List
from math import inf

# my 302ms Beats45.22%
    # 問題是要如何證明，每次都修改最後一個問號成"b"不會違反規則
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        len_s1 = len(str1)
        len_s2 = len(str2)
        ans = ["?"] * (len_s1+len_s2-1)
        for st_i, c1 in enumerate(str1):
            if c1 == "T" :
                for now_i, c2 in zip(range(st_i, st_i+len_s2), str2) :
                    if (now_c := ans[now_i]) == "?" or now_c == c2 :
                        ans[now_i] = c2
                    else :
                        return ""
        # print(ans)
        ans2 = ["a" if c == "?" else c for c in ans]
        for st_i, c1 in enumerate(str1):
            if c1 == "F" :
                last_qu = -1
                for now_i, c2 in zip(range(st_i, st_i+len_s2), str2) :
                    if c2 != ans2[now_i] :
                        last_qu = -2
                        break
                    elif ans[now_i] == "?" :
                        last_qu = now_i
                if last_qu == -1 :
                    return ""
                elif last_qu != -2 : # all the same
                    ans2[last_qu] = "b"
        return "".join(ans2)


# given ans


s = Solution()
print("ans :",s.generateString(str1 = "TFTF", str2 = "ab")) # "ababa"
print("ans :",s.generateString(str1 = "TFTF", str2 = "abc")) # ""
print("ans :",s.generateString(str1 = "F", str2 = "d")) # "a"
print("ans :",s.generateString("TFFFT", "bab")) # 
# print("ans :",s.generateString()) # 



