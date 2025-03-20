# 3108. Minimum Cost Walk in Weighted Graph
# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph

from typing import List
from math import inf

# my 127ms Beats100.00%
class UF:
    def __init__(self, n):
        max_n = (1<<18)-1
        self.min_path = [max_n]*n
        self.id = list(range(n))

    def union(self, u, v, w):
        i = self.find(u)
        j = self.find(v)
        
        self.min_path[j] &= w # 同一條路徑 可能會有不同的 status
        if i == j:
            return
        # merge 兩個 set 的 status
        self.min_path[j] &= self.min_path[i]
        self.id[i] = j

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            # 這裡不需要再 merge status, union 就會做到了
            self.id[up] = self.id[deep]
        return up

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UF(n)
        for n1,n2,w in edges :
            uf.union(n1,n2,w)

        ans = []
        for n1,n2 in query:
            if (n1_set:=uf.find(n1)) == uf.find(n2) :
                ans.append(uf.min_path[n1_set])
            else :
                ans.append(-1)
        return ans

s = Solution()
# print("ans :",s.minimumCost(n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]])) # 
# print("ans :",s.minimumCost(n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]])) # 
# print("ans :",s.minimumCost(n = 4, edges = [[2,3,1],[1,3,5],[1,2,6],[3,0,7],[1,3,7],[0,2,5],[0,1,7]], 
#     query = [[2,1],[1,2],[0,1],[2,0],[0,2],[1,2],[3,2],[0,3],[2,1],[1,2]])) # 

print("ans :",s.minimumCost(n = 4, edges = [[0,1,1],[2,3,7],[0,2,3]], query = [[1,3]])) # 
