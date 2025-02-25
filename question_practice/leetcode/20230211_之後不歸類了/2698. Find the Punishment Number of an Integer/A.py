# 2698. Find the Punishment Number of an Integer
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer

from typing import List
from math import inf
from functools import cache

# my 23ms Beats86.80%
def dfs(s) :
    ret_l = set([int(s)])
    for i in range(1,len(s)):
        now_n = int(s[:i])
        all_poss = dfs(s[i:])
        for poss in all_poss :
            ret_l.add(now_n + poss)
    return ret_l

@cache
def check(n) :
    sq_n = n*n
    # print(n, sq_n, dfs(str(sq_n)) )
    return sq_n if n in dfs(str(sq_n)) else 0

class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum(check(i) for i in range(1,n+1))

# given ans : 32ms Beats86.16%
# logically would be faster, because might reach accept condition previously 
@cache
def isPossible( accumulate, running, numChars, i, target):
    if i == len(numChars):
        return target == accumulate + running
    d = int(numChars[i])
    return (
            # Keep growing `running`.
            isPossible(accumulate, running * 10 + d, numChars, i + 1, target) or
            # Start a new `running`.
            isPossible(accumulate + running, d, numChars, i + 1, target)
    )
class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum(squ for i in range(1, n + 1) if isPossible(0, 0, str(squ := i*i), 0, i))
s = Solution()
print("ans :",s.punishmentNumber(10)) # 182 = 1 + 81 + 100 = 182
print("ans :",s.punishmentNumber(37)) # 1478



