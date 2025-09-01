# 869. Reordered Power of 2
# https://leetcode.com/problems/reordered-power-of-2

from typing import List
from math import inf
from collections import Counter, defaultdict

# my 0ms
all_poss = defaultdict(list)
now_n = 1
MAX = 10**9
while now_n <= MAX :
    str_n = str(now_n)
    all_poss[len(str_n)].append(Counter(str_n))
    now_n <<= 1

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        str_n = str(n)
        cnt_n = Counter(str_n)
        for poss in all_poss[len(str_n)] :
            if poss == cnt_n :
                return True
        return False

s = Solution()
print("ans :",s.reorderedPowerOf2(1)) # T
print("ans :",s.reorderedPowerOf2(10)) # F
print("ans :",s.reorderedPowerOf2(61)) # T



