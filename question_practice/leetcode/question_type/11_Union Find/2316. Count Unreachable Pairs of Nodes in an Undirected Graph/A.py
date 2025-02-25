# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/

# my practice again : 143ms Beats97.33%
class UF_each_set_count:
    def __init__(self, n):
        self.id = list(range(n))
        self.set_member = [1]*n     # <計算各個 set 的個數> 多的

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.set_member[j] += self.set_member[i]  # <計算各個 set 的個數> 多的
        self.set_member[i] = 0
        self.id[i] = j 

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

class Solution:
    def countPairs(self, n: int, edges) -> int:
        uf = UF_each_set_count(n)
        for n1,n2 in edges :
            uf.union(n1,n2)
        
        return sum(g_num*(n-g_num) for g_num in uf.set_member if g_num != 0)//2

s = Solution()
print(s.countPairs(n = 3, edges = [[0,1],[0,2],[1,2]])) # 0
print(s.countPairs(n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]])) # 14



