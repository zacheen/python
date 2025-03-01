# 2876. Count Visited Nodes in a Directed Graph
# https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/description/

from typing import List
from math import inf
from collections import deque

# # my 239ms Beats82.50%
#     # modify from "find_all_cycle"
# class Solution:
#     def countVisitedNodes(self, edges: List[int]) -> List[int]:
#         len_n = len(edges)
#         ans = [len_n] * len_n
#         visit = [len_n] * len_n
#         for now_n in range(len_n):
#             if visit[now_n] != len_n :
#                 continue
#             path = deque([])
#             while now_n != -1 and visit[now_n] == len_n:
#                 path.append(now_n)
#                 visit[now_n] = path[0]
#                 now_n = edges[now_n]  # Move to next node
#             if now_n == -1 : # 一直線
#                 while path :
#                     l = len(path)
#                     ans[path.popleft()] = l # ??
#             elif visit[now_n] == path[0]: # new cycle
#                 while path[0] != now_n :
#                     l = len(path)
#                     ans[path.popleft()] = l
#                 for remain in path :
#                     ans[remain] = len(path)
#             else : # meet other route
#                 while path :
#                     l = len(path)
#                     ans[path.popleft()] = l + ans[now_n]
#         return ans

# my opt by ans : 179ms Beats95.00%
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        len_n = len(edges)
        ans = [len_n] * len_n
        visit = [len_n] * len_n
        for now_n in range(len_n):
            if visit[now_n] != len_n :
                continue
            start_node = now_n
            path = []
            while now_n != -1 and visit[now_n] == len_n:
                path.append(now_n)
                visit[now_n] = start_node
                now_n = edges[now_n]  # Move to next node
            
            # dealing loop
            if visit[now_n] == start_node :
                loop_l = len(path) - path.index(now_n)
                for _ in range(loop_l):
                    ans[path.pop()] = loop_l
            # dealing line 
            app_len = ans[now_n]
            while path :
                app_len += 1
                ans[path.pop()] = app_len
        return ans

# given ans
class Solution(object):
    def countVisitedNodes(self, edges):
        res = [None] * len(edges)
        for i in range(len(edges)):
            if res[i] is not None: 
                continue
            n, j = 0, i
            while res[j] == None: 
                res[j], j, n = -n, edges[j], n + 1
            if res[j] > 0: 
                n += res[j]
            else:
                res[j], k = n + res[j], edges[j]
                while k != j: 
                    res[k], k = res[j], edges[k]
            while i != j: 
                res[i], i = res[i] + n, edges[i]
        return res

s = Solution()
print("ans :",s.countVisitedNodes([1,2,0,0])) # [3,3,3,4]
print("ans :",s.countVisitedNodes([1,2,3,4,0])) # [5,5,5,5,5]
print("ans :",s.countVisitedNodes([7,0,7,0,5,3,3,0])) # [2,3,3,3,5,4,4,2]
