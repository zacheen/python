# 1319. Number of Operations to Make Network Connected
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/

# my 31ms Beats92.59%
class UF_count:
    def __init__(self, n):
        self.count = n              # <計算目前總共分成幾個 set> 多的
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.id[i] = j
        self.count -= 1             # <計算目前總共分成幾個 set> 多的

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < (n-1) :
            return -1

        uf = UF_count(n)
        for n1,n2 in connections :
            uf.union(n1,n2)

        return uf.count-1
