# 779. K-th Symbol in Grammar
# https://leetcode.com/problems/k-th-symbol-in-grammar

from typing import List
from math import inf

# my 
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0
        # 0 | 1
        # 01 | 10
        # 0110| 1001
        # 01101001 | 10010110
        # everytime bitwise not and append at the end

        if n == 1 :
            return 0

        total_len = 1<<(n-1)
        half_len = total_len >> 1
        # print(total_len, half_len, k)
        if k > half_len :
            return 1 - self.kthGrammar(n-1, k-half_len)
        else :
            return self.kthGrammar(n-1, k)

s = Solution()
print("ans :",s.kthGrammar(n = 1, k = 1)) # 0
print("ans :",s.kthGrammar(n = 2, k = 1)) # 0
print("ans :",s.kthGrammar(n = 2, k = 2)) # 1
print("ans :",s.kthGrammar(3, 1)) # 0
print("ans :",s.kthGrammar(3, 3)) # 1



