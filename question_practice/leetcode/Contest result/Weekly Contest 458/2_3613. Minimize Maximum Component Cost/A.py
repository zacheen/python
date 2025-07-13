# 3613. Minimize Maximum Component Cost
# https://leetcode.com/problems/minimize-maximum-component-cost/

from typing import List
from math import inf

# my 131ms Beats98.33%
class UF_count:
    def __init__(self, n):
        self.count = n              # <計算目前總共分成幾個 set> 多的
        self.id = list(range(n))

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        self.id[u] = v
        self.count -= 1             # <計算目前總共分成幾個 set> 多的
        return True

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if n == k :
            return 0
        
        edges.sort(key = lambda x : x[2])
        uf = UF_count(n)
        for n1, n2, c in edges:
            if uf.union(n1, n2) :
                if uf.count == k:
                    return c

s = Solution()
print("ans :",s.minCost(n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 4)) # 2
print("ans :",s.minCost(n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2)) # 4
print("ans :",s.minCost(n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 1)) # 6
print("ans :",s.minCost(n = 4, edges = [[0,1,5],[1,2,5],[2,3,5]], k = 1)) # 5
print("ans :",s.minCost(n = 4, edges = [[0,1,5],[1,2,5],[2,3,5]], k = 4)) # 0
# print("ans :",s.minCost()) # 
# print("ans :",s.minCost()) # 



