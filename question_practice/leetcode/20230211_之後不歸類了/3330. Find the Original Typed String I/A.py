# 3330. Find the Original Typed String I
# https://leetcode.com/problems/find-the-original-typed-string-i

from typing import List
from math import inf
from itertools import pairwise, groupby

# my 27ms Beats98.87%
class Solution:
    def possibleStringCount(self, word: str) -> int:
        return sum( c1 == c2 for c1, c2 in pairwise(word) ) +1 
        
        # 45ms Beats18.31%
        # return sum(len(list(group))-1 for key_value, group in groupby(word)) + 1

s = Solution()
print("ans :",s.possibleStringCount("abbcccc")) # 5
print("ans :",s.possibleStringCount("abcd")) # 1
print("ans :",s.possibleStringCount("aaaa")) # 4
print("ans :",s.possibleStringCount("ebe")) # 1



