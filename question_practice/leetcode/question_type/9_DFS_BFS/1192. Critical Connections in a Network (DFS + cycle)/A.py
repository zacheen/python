from collections import defaultdict

# my v1 Time Limit Exceeded
# DFS + union set
# class Solution:
#     def criticalConnections(self, n: int, connections):
#         class UF:
#             def __init__(self, n):
#                 self.id = list(range(n))

#             def union(self, u, v):
#                 i = self.find(u)
#                 j = self.find(v)
#                 if i == j:
#                     return
#                 self.id[i] = j

#             def find(self, u):
#                 if self.id[u] != u:
#                     self.id[u] = self.find(self.id[u])
#                 return self.id[u]
        
#         # DFS 如果到了同一個點 -> 這兩條路徑上全部的點互相的link 都不是 critical 
#         # 先處理 Link
#         link = defaultdict(list)
#         for n1,n2 in connections :
#             link[n1].append(n2)
#             link[n2].append(n1)
        
#         # 開始 DFS
#         finish_DFS = [False]*n # 紀錄已經全部的可能性都走過的點
#         sets = UF(n)
#         path = []
#         path_check = [False]*n
#         def dfs(now_p):
#             path.append(now_p)
#             path_check[now_p] = True
#             # print(path)
#             for next_p in link[now_p] :
#                 if not finish_DFS[now_p] :
#                     # 如果形成圈圈
#                     if path_check[next_p] :
#                         # 如果不是前一個點(要形成3點以上的圈圈) 且 此關係之前沒有建立過
#                         if next_p != path[-2] and sets.find(next_p) != sets.find(now_p) :
#                             # 形成圈圈 因此圈圈的每一點都與圈圈一開始的點有關
#                             # 圈圈一開始的點 應該會比較快 然後 now_p == 圈圈一開始的點
#                             for p in path[path.index(next_p):] :
#                                 # print("union",p,next_p)
#                                 sets.union(p,next_p)
#                         # else 不用做事
#                     else :
#                         dfs(next_p)
#             path.pop()
#             path_check[now_p] = False
#             finish_DFS[now_p] = True
            
#         dfs(0)
#         ans = []
#         for l in connections :
#             if sets.find(l[0]) != sets.find(l[1]) :
#                 ans.append(l)
#         return ans

# my v2 優化 finish_DFS # Time Limit Exceeded
# class Solution:
#     def criticalConnections(self, n: int, connections):
#         class UF:
#             def __init__(self, n):
#                 self.id = list(range(n))

#             def union(self, u, v):
#                 i = self.find(u)
#                 j = self.find(v)
#                 if i == j:
#                     return
#                 self.id[i] = j

#             def find(self, u):
#                 if self.id[u] != u:
#                     self.id[u] = self.find(self.id[u])
#                 return self.id[u]
        
#         # DFS 如果到了同一個點 -> 這兩條路徑上全部的點互相的link 都不是 critical 
#         # 先處理 Link
#         # link = defaultdict(list)
#         link = [[] for _ in range(n)]
#         for n1,n2 in connections :
#             link[n1].append(n2)
#             link[n2].append(n1)
        
#         # 開始 DFS
#         finish_DFS = [False]*n # 紀錄已經全部的可能性都走過的點
#         sets = UF(n)
#         path = []
#         path_check = [False]*n
#         def dfs(now_p):
#             path.append(now_p)
#             path_check[now_p] = True
#             # print(path)
#             for next_p in link[now_p] :  
#                 # 如果形成圈圈
#                 if path_check[next_p] :
#                     # 如果不是前一個點(要形成3點以上的圈圈) 且 此關係之前沒有建立過
#                     if next_p != path[-2] and sets.find(next_p) != sets.find(now_p) :
#                         # 形成圈圈 因此圈圈的每一點都與圈圈一開始的點有關
#                         # 圈圈一開始的點 應該會比較快 然後 now_p == 圈圈一開始的點
#                         for p in path[path.index(next_p):] :
#                             # print("union",p,next_p)
#                             sets.union(p,next_p)
#                     # else 不用做事
#                 elif finish_DFS[next_p] :
#                     continue
#                 else :
#                     finish_DFS[next_p] = True
#                     dfs(next_p)
#             path.pop()
#             path_check[now_p] = False
            
            
#         dfs(0)
#         ans = []
#         for l in connections :
#             if sets.find(l[0]) != sets.find(l[1]) :
#                 ans.append(l)
#         return ans

# given ans
# 我是檢查有沒有圈圈
# 但其實另一個想法就是 如果走到底沒有圈圈 -> 這條路徑是 critical
    # 只需要 DFS 一次

# 看觀念 自己實作看看
# 還是 Time Limit Exceeded ...
# class Solution:
#     def criticalConnections(self, n: int, connections):
#         # 先處理 Link
#         link = defaultdict(list)
#         # link = [[] for _ in range(n)]
#         for n1,n2 in connections :
#             link[n1].append(n2)
#             link[n2].append(n1)
        
#         # 開始 DFS
#         finish_DFS = [False]*n # 紀錄已經全部的可能性都走過的點
#         path = []
#         path_add = []
#         path_check = [False]*n
#         ans = []
#         def dfs(now_p):
#             nonlocal path

#             # 這是上一個 要刪除
#             if len(path) >= 2 and now_p == path[-2] :
#                 return 
            
#             # base case 1 走過了
#             if path_check[now_p] :
#                 # print(now_p,"走過了")
#                 for i in range(path.index(now_p)+1, len(path_add)):
#                     path_add[i] = False
#                 return
            
#             # base case 2 到底了
#             if len(link[now_p]) == 1 and len(path) >= 2 :
#                 # print(now_p,"到底了",path)
#                 ans.append([path[-1], now_p])
#                 return 

#             if finish_DFS[now_p] :
#                 return
#             finish_DFS[now_p] = True
            
#             path.append(now_p) 
#             path_check[now_p] = True
#             path_add.append(True) # 預設都是 True

#             for next_p in link[now_p] :  
#                 dfs(next_p)
            
#             pop_res = path_add.pop()
#             # print("pop_res",pop_res)
#             if pop_res :
#                 if len(path) >= 2 :
#                     ans.append([path[-1], path[-2]])
#             path.pop()
#             path_check[now_p] = False
            
#         dfs(0)
#         return ans

# given ans Runtime: 2218 ms, faster than 96.86% of Python3
class Solution:
    def criticalConnections(self, n: int, connections):
        # 先處理 Link
        graph = defaultdict(list)
        # link = [[] for _ in range(n)]
        for n1,n2 in connections :
            graph[n1].append(n2)
            graph[n2].append(n1)

        NO_RANK = -2
        rank = [NO_RANK]*n
        ans = []

        def getRank(u, myRank):
            nonlocal rank
            if rank[u] != NO_RANK :
                return rank[u]

            rank[u] = myRank
            minRank = myRank

            for v in graph[u] :
                # 如果已經走過了 或 是上一個位置
                if rank[u] == n or rank[v] == myRank-1 :
                    continue
                nextRank = getRank(v, myRank+1)
                if nextRank == (myRank + 1) :
                    ans.append([u,v])
                minRank = min(minRank, nextRank)
            
            rank[u] = n
            # 回傳最小的圈圈位置
            # return rank + minRank 解決了我用path_add紀錄的問題 (O)
            return minRank

        getRank(0, 0)
        return ans

s = Solution()
# print(s.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]))
# print(s.criticalConnections(n = 2, connections = [[0,1]]))
# print(s.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,3]]))
# print(s.criticalConnections(n = 5, connections = [[0,1],[1,2],[2,0],[1,3],[2,4]]))
# print(s.criticalConnections(n = 5, connections = [[0,1],[1,2],[2,0],[1,3],[2,4],[1,4]]))
print(s.criticalConnections(n = 5, connections = [[1,2],[2,0],[1,3],[2,4],[1,4]]))


