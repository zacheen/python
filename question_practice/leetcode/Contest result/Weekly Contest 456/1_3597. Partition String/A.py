# 3597. Partition String 
# https://leetcode.com/problems/partition-string/description/

from typing import List
from math import inf

# my 139ms : Beats95.68%
class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        ans = []
        new_s = ""
        for c in s :
            new_s += c
            if not (new_s in seen) :
                ans.append(new_s)
                seen.add(new_s)
                new_s = ""
        return ans

s = Solution()
print("ans :",s.partitionString("abbccccd")) # ['a', 'b', 'bc', 'c', 'cc', 'd']
print("ans :",s.partitionString("aaaa")) # ['a', 'aa']



