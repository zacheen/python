# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/description

from typing import List
from math import inf

# my 0ms Beats100.00%
def link(relation, len_n = -1):
    links = [[] for _ in range(len_n)]
    # build
    for n1,n2 in relation :
        links[n1].append(n2)
        links[n2].append(n1)
    return links

class Solution:
    def findRedundantConnection(self, links: List[List[int]]) -> List[int]:
        len_n = len(links) + 1
        li = link(links, len_n)
        # print(li)
        seen = set()
        cir = set()
        def dfs(n, prev) :
            if n in seen :
                cir.add(n)
                return 1
            seen.add(n)
            for next_n in li[n] :
                if next_n != prev :
                    ret = dfs(next_n, n)
                    if ret == 1 :
                        if n in cir :
                            return 2
                        cir.add(n)
                        return 1
                    elif ret == 2 :
                        return 2
            return 3
        dfs(1, -1)
        # print(cir)
        for n1,n2 in links[::-1] :
            if n1 in cir and n2 in cir :
                return [n1,n2]
        raise Exception

# given ans : union find : 0ms Beats100.00% 
    # (Although both is 0ms, I believe this one is faster)
class Solution:
    def findRedundantConnection(self, edges):
        id=[i for i in range(len(edges)+1)]
        def find(x):
            if id[x]!=x:
                id[x]=find(id[x])
            return id[x]
        def union(x,y):
            rootX=find(x)
            rootY=find(y)
            if rootX==rootY:
                return True
            id[rootX]=rootY
            return False
        for n1,n2 in edges:
            if union(n1,n2):
                return [n1,n2]

s = Solution()
# print("ans :",s.findRedundantConnection(edges = [[1,2],[1,3],[2,3]])) # [2,3]
print("ans :",s.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]])) # [1,4]



