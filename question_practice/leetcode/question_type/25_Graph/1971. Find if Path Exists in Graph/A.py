# 1971. Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

from typing import List
from math import inf

# my (dfs)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        li = [[] for _ in range(n)]
        # build
        for n1,n2 in edges :
            li[n1].append(n2)
            li[n2].append(n1)
        
        seen = set()
        def dfs(now_n):
            nonlocal seen
            if now_n == destination :
                return True
            seen.add(now_n)
            for next_n in li[now_n] :
                if next_n in seen :
                    continue
                if dfs(next_n) :
                    return True
            return False
        return dfs(source)

