# 3607. Power Grid Maintenance
# https://leetcode.com/problems/power-grid-maintenance

from typing import List
from math import inf
from heapq import heapify, heappop
from collections import defaultdict
    
# my v2 opt (generate set_member after union): 314ms Beats94.52%
class UF:
    def __init__(self, n):
        self.id = list(range(n))

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.id[u] = v

    # 這個方法會跳著更新link (但更新整個link最多花 log2 次)
    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up
    
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UF(c+1)
        for n1, n2 in connections :
            uf.union(n1, n2)
    
        set_member = defaultdict(list)
        for i in range(1, c+1):
            set_member[uf.find(i)].append(i)

        for li in set_member.values() :
            heapify(li)
        
        active_node = [True]*(c+1)
        ans = []
        for ty, x in queries :
            if ty == 1 :
                if active_node[x] : 
                    ans.append(x)
                else :
                    rel_set = set_member[uf.find(x)]
                    while rel_set and not active_node[rel_set[0]]:
                        heappop(rel_set)
                    if rel_set :
                        ans.append(rel_set[0])
                    else :
                        ans.append(-1)
            else :
                active_node[x] = False
        return ans

# # my v1 : 9037ms Beats5.01%
# class UF_find_relate:
#     def __init__(self, n):
#         self.id = list(range(n))
#         self.set_member = [[i] for i in range(n)]

#     def union(self, u, v):
#         i = self.find(u)
#         j = self.find(v)
#         if i == j:
#             return
#         self.set_member[j] += self.set_member[i]
#         self.set_member[i] = None
#         self.id[i] = j

#     def find(self, up):
#         while (up:=self.id[up]) != (deep:=self.id[up]):
#             self.id[up] = self.id[deep]
#         return up
    
#     def ger_related(self, u):
#         if self.id[u] != u:
#             self.id[u] = self.find(self.id[u])
#         return self.set_member[self.id[u]]
    
#     def heapify(self):
#         for li in self.set_member :
#             if li != None :
#                 heapify(li)

# class Solution:
#     def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
#         uf = UF_find_relate(c+1)
#         for n1, n2 in connections :
#             uf.union(n1, n2)
#         uf.heapify()
        
#         close_node = set()
#         ans = []
#         for ty, x in queries :
#             if ty == 1 :
#                 if x not in close_node : 
#                     ans.append(x)
#                 else :
#                     rel_set = uf.ger_related(x)
#                     while rel_set and rel_set[0] in close_node:
#                         heappop(rel_set)
#                     if rel_set :
#                         ans.append(rel_set[0])
#                     else :
#                         ans.append(-1)
#             else :
#                 close_node.add(x)
#         return ans


s = Solution()
print("ans :",s.processQueries(c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], 
                               queries = [[1,3],[2,1],[1,1],[2,2],[1,2]])) # [3,2,3]
print("ans :",s.processQueries(c = 3, connections = [], 
                               queries = [[1,1],[2,1],[1,1]])) # [1,-1]



