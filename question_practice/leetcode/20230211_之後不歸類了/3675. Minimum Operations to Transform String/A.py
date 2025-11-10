# 3675. Minimum Operations to Transform String
# https://leetcode.com/problems/minimum-operations-to-transform-string/description/

from typing import List
from math import inf

# my 47ms Beats94.14%
class Solution:
    def minOperations(self, s: str) -> int:
        set_all_c = set(s)
        for i in range(1,26):
            c_id = i+97
            if chr(c_id) in set_all_c :
                return 26-i
        return 0

s = Solution()
print("ans :",s.minOperations("yz")) # 2
print("ans :",s.minOperations("a")) # 0



