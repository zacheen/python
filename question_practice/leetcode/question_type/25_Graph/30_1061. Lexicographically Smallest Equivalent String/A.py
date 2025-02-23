# 1061. Lexicographically Smallest Equivalent String
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string

from typing import List
from math import inf

# my 3ms Beats93.50%
class UF_by_min:
    def __init__(self):
        self.id = {}

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        if i < j :           # union 的時候比較數字大小
            self.id[j] = i
        else :
            self.id[i] = j

    def find(self, u):
        if u not in self.id :
            return u
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UF_by_min()
        for c1,c2 in zip(s1,s2):
            uf.union(c1,c2)
        return "".join(uf.find(c) for c in baseStr)

s = Solution()
print("ans :",s.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser")) # "makkek"



