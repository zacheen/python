# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/description/

from typing import List
import functools

# # my BFS Beats 51.93%
# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         mem_set = [0]*len(graph)
#         mem_seen = set()
#         stack = list(range(len(graph)))
#         while stack :
#             now_p = stack.pop()

#             if now_p in mem_seen :
#                 continue
#             else :
#                 mem_seen.add(now_p)

#             # new dfs start
#             if mem_set[now_p] == 0 :
#                 mem_set[now_p] = 1      

#             this_set = mem_set[now_p]
#             if this_set == 1 :
#                 diff_set = 2
#             else :
#                 diff_set = 1
#             for link_p in graph[now_p] : 
#                 if mem_set[link_p] == this_set :
#                     # print(mem_set, mem_set[link_p], this_set)
#                     return False 
#                 if mem_set[link_p] == 0 :
#                     mem_set[link_p] = diff_set
#                     stack.append(link_p)
        
#         # print(mem_set)
#         return True
#         # I thought that the point no link to other is False (because no path)
#         # if ans :
#         #     return len(mem_pass) == len(graph)
#         # else :
#         #     return ans

# # my DFS Beats 46.22%
# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         mem_set = [0]*len(graph)
#         mem_pass = set()

#         ans = True
#         def dfs(p):
#             nonlocal ans
#             if p in mem_pass :
#                 return
#             mem_pass.add(p)
            
#             this_set = mem_set[p]
#             if this_set == 1 :
#                 diff_set = 2
#             else :
#                 diff_set = 1

#             for link_p in graph[p] : 
#                 if mem_set[link_p] == this_set :
#                     ans = False
#                     return 
#                 mem_set[link_p] = diff_set
#                 dfs(link_p)
#                 if not ans :
#                     return 
        
#         for i in range(len(graph)):
#             if mem_set[i] == 0 :
#                 mem_set[i] = 1
#                 dfs(i)
#         # print(mem_set)
#         return ans
#         # if ans :
#         #     return len(mem_pass) == len(graph)
#         # else :
#         #     return ans

# given ans
from collections import deque
from enum import Enum
class Color(Enum):
    kWhite = 0
    kRed = 1
    kGreen = 2
# # BFS
# # 跟我的想法一樣
# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         colors = [Color.kWhite] * len(graph)

#         for i in range(len(graph)):
#             # Already colored, do nothing
#             if colors[i] != Color.kWhite:
#                 continue
#             # colors[i] == Color.kWhite
#             colors[i] = Color.kRed  # Always paint w/ Color.kRed
#             # BFS
#             q = deque([i])
#             while q:
#                 u = q.popleft()
#                 for v in graph[u]:
#                     if colors[v] == colors[u]:
#                         return False
#                     if colors[v] == Color.kWhite:
#                         colors[v] = Color.kRed if colors[u] == Color.kGreen else Color.kGreen
#                         q.append(v)
#         return True

# BFS 優化 by me Beats 62.32%
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [Color.kWhite] * len(graph)

        for i in range(len(graph)):
            # Already colored, do nothing
            if colors[i] != Color.kWhite:
                continue
            # colors[i] == Color.kWhite
            colors[i] = Color.kRed  # Always paint w/ Color.kRed
            # BFS
            q = [i]
            while q:
                u = q.pop()
                for v in graph[u]:
                    if colors[v] == colors[u]:
                        return False
                    if colors[v] == Color.kWhite:
                        colors[v] = Color.kRed if colors[u] == Color.kGreen else Color.kGreen
                        q.append(v)
        return True

# DFS Beats 65.69%
# 我一開始有這個想法 但是架構沒想好
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [Color.kWhite] * len(graph)

        def isValidColor(u: int, color: Color) -> bool:
            # The painted color should be same as the `color`
            if colors[u] != Color.kWhite:
                return colors[u] == color

            colors[u] = color  # Always paint `color`

            # All children should have valid colors
            childrenColor = Color.kRed if colors[u] == Color.kGreen else Color.kGreen
            return all(isValidColor(v, childrenColor) for v in graph[u])

        return all(colors[i] != Color.kWhite or isValidColor(i, Color.kRed)
                for i in range(len(graph)))

s = Solution()
print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))     # true
print(s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])) # false



