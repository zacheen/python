# 1400. Construct K Palindrome Strings
# https://leetcode.com/problems/construct-k-palindrome-strings/description

from typing import List
import functools

from collections import Counter
# my 30ms Beats74.89%
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k :
            return False
        
        cou = Counter(s)
        for c, n in cou.items() :
            if n%2 :
                k -= 1
                if k < 0 :
                    return False
        return True

# given ans
# same concept, but better implement method
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(freq & 1 for freq in Counter(s).values()) <= k <= len(s)
               
s = Solution()
print("ans :",s.canConstruct(s = "annabelle", k = 2)) # T
print("ans :",s.canConstruct(s = "true", k = 4)) # T
print("ans :",s.canConstruct(s = "leetcode", k = 3)) # F
print("ans :",s.canConstruct("cr", 7)) # F
print("ans :",s.canConstruct("abccde", 4)) # T
print("ans :",s.canConstruct("abccde", 5)) # T
# print("ans :",s.canConstruct()) # 



