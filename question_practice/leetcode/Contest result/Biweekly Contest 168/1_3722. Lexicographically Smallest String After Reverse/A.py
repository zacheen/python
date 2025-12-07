# 3722. Lexicographically Smallest String After Reverse
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/description/

from typing import List
from math import inf

# my 
class Solution:
    def lexSmallest(self, s: str) -> str:        
        ret = min(s, s[::-1])
        for rev_en in range(1,len(s)) :
            new_s = s[rev_en-1::-1] + s[rev_en:]
            # print(s[rev_en-1::-1], s[rev_en:])
            if new_s < ret :
                ret = new_s

        for rev_st in range(1,len(s)) :
            new_s = s[:rev_st] + s[:rev_st-1:-1]
            # print(s[:rev_st], s[:rev_st-1:-1])
            if new_s < ret :
                ret = new_s
    
        return ret

s = Solution()
print("ans :",s.lexSmallest("dcab")) # acdb
print("ans :",s.lexSmallest("abba")) # aabb
print("ans :",s.lexSmallest("zxy")) # xzy
print("ans :",s.lexSmallest("aacbac")) # aacabc

