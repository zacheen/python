# 1957. Delete Characters to Make Fancy String
# https://leetcode.com/problems/delete-characters-to-make-fancy-string

from typing import List
from math import inf

# my 147ms Beats99.80%
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        cnt = 0
        last_c = ""
        for c in s :
            if c == last_c :
                cnt += 1
                if cnt < 3 :
                    ans.append(c)
            else :
                last_c = c
                cnt = 1
                ans.append(c)
        return "".join(ans)

s = Solution()
print("ans :",s.makeFancyString("leeetcode")) # leetcode
print("ans :",s.makeFancyString("aaabaaaa")) # aabaa
print("ans :",s.makeFancyString("aab")) # aab



