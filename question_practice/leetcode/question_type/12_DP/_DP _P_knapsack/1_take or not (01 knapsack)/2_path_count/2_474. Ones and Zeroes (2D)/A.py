# 474. Ones and Zeroes
# https://leetcode.com/problems/ones-and-zeroes
from collections import Counter, defaultdict
from math import inf
from typing import List

# my using template 2_path_count v2 : 311ms Beats98.38%
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int):
        mem = defaultdict(int)
        mem[(0,0)] = 0
        for s in strs:
            cnt = Counter(s)
            n0 = cnt['0']
            n1 = cnt['1']
            for (pn0, pn1), l in list(mem.items()) :
                if (fut_n0 := pn0 + n0) <= m and (fut_n1 := pn1 + n1) <= n :
                    if (new_l := 1+l) > mem[(fut_n0, fut_n1)]:
                        mem[(fut_n0, fut_n1)] = new_l
        # print(mem)
        return max(mem.values())

# my using template 2_path_count : 822ms Beats97.33%
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int):
        dp=[[-inf]*(n+1) for _ in range(m+1)]
        dp[0][0] = 0
        for s in strs:
            cnt = Counter(s)
            n0 = cnt['0']
            n1 = cnt['1']
            for i0 in range(m, n0-1, -1):
                for i1 in range(n, n1-1, -1) :
                    if (t := 1+dp[i0-n0][i1-n1]) > dp[i0][i1]:
                        dp[i0][i1] = t
        return max(n for l in dp for n in l)

s = Solution()
print(s.findMaxForm())



