# 3463. Check If Digits Are Equal in String After Operations II
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/description/
    # related to math

from typing import List
from math import inf, comb

# given ans (lucas theorem)
class Solution:
    def lucas(self,n, k):
        res = 1
        while n or k:
            (n, n_i), (k, k_i) = divmod(n,5),divmod(k,5)
            res = (res * (comb(n_i, k_i)%5)) % 5
        return res

    def crt(self,n, k):
        r2 = n & k == k
        r5 = self.lucas(n, k)  
        
        for c in range(10):
            if c%2 == r2 and c%5 == r5:
                return c

    def hasSameDigits(self, s: str) -> bool:
        mods = [self.crt(len(s)-2,i) for i in range(len(s)-1)]
        return sum(int(c)*mods[i] for i,c in enumerate(s[:-1]))%10 == sum(int(c)*mods[i] for i,c in enumerate(s[1:]))%10

s = Solution()
print("ans :",s.hasSameDigits("3902")) # T "11"
print("ans :",s.hasSameDigits("34789")) # F "48"



