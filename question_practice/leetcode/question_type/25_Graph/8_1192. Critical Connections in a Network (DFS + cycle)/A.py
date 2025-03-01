# 1192. Critical Connections in a Network
# https://leetcode.com/problems/critical-connections-in-a-network/description/

# my practice again : 247ms Beats87.30%
# actuall I accidently optimize : using path = {} to memorize path and seen_order
from math import inf
class Solution:
    def criticalConnections(self, n, connections):
        links = [[] for _ in range(n)]
        for n1,n2 in connections :
            links[n1].append(n2)
            links[n2].append(n1)
        
        path = {}
        ans = []
        def dfs(now_n, prev_n) :
            if now_n in path : # form a circle
                return path[now_n]
            path[now_n] = len(path)
            min_ret = len(path)
            for next_n in links[now_n] :
                if next_n != prev_n :
                    ret = dfs(next_n, now_n)
                    if ret > path[now_n] :
                        ans.append((now_n, next_n))
                    min_ret = min(min_ret, ret)
            path[now_n] = min_ret
            return min_ret
        dfs(0,-1)
        return ans

# # given ans Runtime: 303ms Beats52.37%
# class Solution:
#     def criticalConnections(self, n: int, connections):
#         # 先處理 Link
#         graph = [[] for _ in range(n)]
#         for n1,n2 in connections :
#             graph[n1].append(n2)
#             graph[n2].append(n1)

#         NO_RANK = -2
#         rank = [NO_RANK]*n
#         ans = []

#         def getRank(u, myRank):
#             nonlocal rank
#             if rank[u] != NO_RANK :
#                 return rank[u]

#             rank[u] = myRank
#             minRank = myRank
#             for v in graph[u] :
#                 # 如果已經走過了 或 是上一個位置
#                 if rank[u] == n or rank[v] == myRank-1 :
#                     continue
#                 nextRank = getRank(v, myRank+1)
#                 if nextRank == (myRank + 1) :
#                     ans.append([u,v])
#                 minRank = min(minRank, nextRank)
            
#             rank[u] = n
#             # 回傳最小的圈圈位置
#             # return rank + minRank 解決了我用path_add紀錄的問題 (O)
#             return minRank

#         getRank(0, 0)
#         return ans

s = Solution()
print(s.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]])) # [(1, 3)]
print(s.criticalConnections(n = 2, connections = [[0,1]])) # [(0, 1)]
print(s.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,3]])) # [(2, 3), (1, 2), (0, 1)]
print(s.criticalConnections(n = 5, connections = [[0,1],[1,2],[2,0],[1,3],[2,4]]))
print(s.criticalConnections(n = 5, connections = [[0,1],[1,2],[2,0],[1,3],[2,4],[1,4]]))
print(s.criticalConnections(n = 5, connections = [[1,2],[2,0],[1,3],[2,4],[1,4]]))


