# 3608. Minimum Time for K Connected Components
# https://leetcode.com/problems/minimum-time-for-k-connected-components

from typing import List
from math import inf

# my using template UF_count : 114ms Beats100.00%
class UF_count:
    def __init__(self, n):
        self.count = n              # <計算目前總共分成幾個 set> 多的
        self.id = list(range(n))

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.id[u] = v
        self.count -= 1             # <計算目前總共分成幾個 set> 多的

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if n == k :
            return max( (t for n1, n2, t in edges), default = 0)
        
        edges.sort(reverse = True, key = lambda x : x[2])
        # print(edges)

        uf = UF_count(n)
        for n1, n2, t in edges :
            uf.union(n1, n2)
            if uf.count < k :
                return t
        return 0

s = Solution()
print("ans :",s.minTime(n = 2, edges = [[0,1,3]], k = 2)) # 3
print("ans :",s.minTime(n = 3, edges = [[0,1,2],[1,2,4]], k = 3)) # 4
print("ans :",s.minTime(n = 3, edges = [[0,2,5]], k = 2)) # 0
print("ans :",s.minTime(n = 1, edges = [], k = 1)) # 0
print("ans :",s.minTime(n = 2, edges = [[0,1,4]], k = 1)) # 0
print("ans :",s.minTime(n = 2, edges = [[0,1,4]], k = 2)) # 4



