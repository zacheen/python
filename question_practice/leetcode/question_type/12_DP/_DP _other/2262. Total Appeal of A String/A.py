# 2262. Total Appeal of A String
# https://leetcode.com/problems/total-appeal-of-a-string/description/

from typing import List
from math import inf
from collections import defaultdict

# given ans
class Solution:
    def appealSum(self, s: str) -> int:
        res, cur, prev = 0, 0, defaultdict(lambda: -1)
        for i, ch in enumerate(s):
            cur += i - prev[ch]
            prev[ch] = i
            res += cur
        return res  

s = Solution()
print("ans :",s.appealSum("abbca")) # 28
print("ans :",s.appealSum("code")) # 20
print("ans :",s.appealSum("cooe")) # 16
print("ans :",s.appealSum("aba")) # 9
print("ans :",s.appealSum("abb")) # 8



