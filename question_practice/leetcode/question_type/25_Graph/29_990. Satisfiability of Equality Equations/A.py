# 990. Satisfiability of Equality Equations
# https://leetcode.com/problems/satisfiability-of-equality-equations

from typing import List
from math import inf

# my 2ms Beats70.65%
ord_a = ord('a')
class UF:
    def __init__(self):
        self.id = {chr(c):chr(c) for c in range(ord_a,ord_a+26)}

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.id[i] = j

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF()
        ne_l = []
        for s in equations :
            if s[1] == "!" :
                ne_l.append((s[0], s[3]))
            else :
                uf.union(s[0], s[3])

        for n1,n2 in ne_l :
            if uf.find(n1) == uf.find(n2) :
                return False
        return True
        

# given ans


s = Solution()
print("ans :",s.equationsPossible(["a==b","b!=a"])) # F
print("ans :",s.equationsPossible(["b==a","a==b"])) # T
print("ans :",s.equationsPossible(["a==b","b!=c","c==a"])) # F



