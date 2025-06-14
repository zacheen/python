from typing import List
import functools

# # my v1 
#     # I know will Time exceed (10^5 * 10^5 too big)
# from collections import defaultdict
# import heapq
# from math import inf
# class Solution:
#     def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         mem_path = [defaultdict(lambda: inf) for _ in range(n)]
#         for i,j,limit in edgeList :
#             mem_path[i][j] = min(mem_path[i][j], limit)
#             mem_path[j][i] = min(mem_path[j][i], limit)

#         mem_max_limit = [[inf]*n for _ in range(n)]
#         def bfs_return_max_limit(i,j):
#             max_limit = 0
#             stack = [(-1,i)]
#             mem_seen = set()
#             while stack :
#                 this_limit, this_p = heapq.heappop(stack)
#                 max_limit = max(this_limit, max_limit)
#                 if this_p == j :
#                     # print(mem_seen)
#                     return max_limit
#                 mem_seen.add(this_p)
#                 for next_p, next_limit in mem_path[this_p].items() :
#                     if next_p in mem_seen :
#                         continue
#                     heapq.heappush(stack, (next_limit, next_p))
#             # print("no path")
#             return -1
        
#         ans = []
#         ret_list = []
#         for start, end, limit in queries :
#             ret = bfs_return_max_limit(start, end)
#             ret_list.append((start, end, limit,ret))
#             ans.append(ret != -1 and ret < limit)
#         print(ret_list)
#         return ans
    
# submit fail : 回傳的東西錯誤 原本想要回傳-1當作失敗 但是我在第一個點就被改掉了 

# # my v2 mem wrong
    # 下面有解釋
# from collections import defaultdict
# import heapq
# from math import inf
# class Solution:
#     def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         mem_path = [defaultdict(lambda: inf) for _ in range(n)]
#         for i,j,limit in edgeList :
#             mem_path[i][j] = min(mem_path[i][j], limit)
#             mem_path[j][i] = min(mem_path[j][i], limit)

#         mem_max_limit = [[inf]*n for _ in range(n)]
#         # inf 代表沒走過
#         # -1 代表不會到
#         # 其他數字代表 max limit
#         def bfs_return_max_limit(i,j):
#             max_limit = -1
#             stack = [(-1,i)]
#             mem_seen = set()
#             while stack : 
#                 this_limit, this_p = heapq.heappop(stack)
#                 # commit fail 這裡沒有再判斷一次 有沒有看過
#                 if this_p in mem_seen :
#                     continue
#                 mem_seen.add(this_p)
#                 max_limit = max(this_limit, max_limit)
#                 mem_max_limit[i][this_p] = max_limit
#                 mem_max_limit[this_p][i] = max_limit
#                 if this_p == j :
#                     return max_limit
#                 mem_ret = mem_max_limit[this_p][j]
#                 if mem_ret == -1 :
#                     continue
#                 elif mem_ret != inf :
#                     print("pull mem : ",this_p, j, mem_ret)
#                     # 這裡我使用 mem 
#                     # 但是其實 this_p ~ j 之前走過的路徑，應該也要加入 seen 
#                     # 但是沒有 所以stack就會走另外一條路 到某一個中間的點 導致出錯
#                     heapq.heappush(stack, (mem_ret, j))
#                     continue
#                 else :
#                     for next_p, next_limit in mem_path[this_p].items() :
#                         if next_p in mem_seen :
#                             continue
#                         if (next_p == 78) :
#                             print("in for :",this_p, next_p, next_limit)
#                         heapq.heappush(stack, (next_limit, next_p))
#             # print("no path")
#             mem_max_limit[i][j] = -1
#             return -1
        
#         ans = []
#         ret_list = []
#         for start, end, limit in queries :
#             print("doing ", start, end, limit, "----------------------------")
#             ret = bfs_return_max_limit(start, end)
#             ret_list.append((start, end, limit, ret))
#             ans.append(ret != -1 and ret < limit)
#             # print("mem",mem_max_limit[228][78])
#         print(ret_list)
#         return ans

# my v3 我在想辦法解決 mem 的問題
    # 但總不可能把 i 到 j 全部的路徑都紀錄起來
    # 但是我可以記錄 從點 i 到 j 所有經過的點的最小limit
        # 但是這個演算法跟 heap 好像沒有辦法搭配 
            # (因為我是紀錄從 i 這個點延伸出去最小limit 並不知道中途點的最小limit)
        # 所以我的演算法要改成 DP，從所有可以到 j 點的路徑找到最小limit
            # (i,j) i個組合 * j個組合 * 找max -> 10^5 * 10^5 * 10^5 應該會超出 time limit
        # 所以失敗

# # given ans (unionByRank) Beats 66.75%
# 看起來這個 case unionByRank 跟普通的 Union 差不多
class UF:
    def __init__(self, n):
        self.id = list(range(n))
        self.rank = [0]*n

    def unionByRank(self, u, v) :
        i = self.find(u)
        j = self.find(v)
        if (i == j) :
            return
        if (self.rank[i] < self.rank[j]) :
            self.id[i] = self.id[j]
        elif (self.rank[i] > self.rank[j]) :
            self.id[j] = self.id[i]
        else :
            self.id[i] = self.id[j]
            self.rank[j] += 1

    def find(self, u) :
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]
        
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [False]*len(queries)
        qs = [ query + [indx] for indx , query in enumerate(queries) ]
        uf = UF(n)

        # 用 limit 排序
        qs.sort(key=lambda x : x[2])
        edgeList.sort(key=lambda x : x[2])

        i = 0; # i : edgeList's index
        for q in qs :
            # 每次只先相連小於 edgeList 的 limit 的 edge
            while i < len(edgeList) and edgeList[i][2] < q[2] :
                uf.unionByRank( edgeList[i][0], edgeList[i][1] )
                i+=1
            # 如果是同一個集合代表此兩點在 limit 的限制下有相連
            if uf.find(q[0]) == uf.find(q[1]) :
                ans[q[3]] = True
        return ans
    
# given ans (Normal Union) Beats 70.76%
class UF:
    def __init__(self, n):
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        self.id[i] = j

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]
        
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [False]*len(queries)
        qs = [ query + [indx] for indx , query in enumerate(queries) ]
        uf = UF(n)

        # 用 limit 排序
        qs.sort(key=lambda x : x[2])
        edgeList.sort(key=lambda x : x[2])

        i = 0; # i : edgeList's index
        for q in qs :
            # 每次只先相連小於 edgeList 的 limit 的 edge
            while i < len(edgeList) and edgeList[i][2] < q[2] :
                uf.union( edgeList[i][0], edgeList[i][1] )
                i+=1
            # 如果是同一個集合代表此兩點在 limit 的限制下有相連
            if uf.find(q[0]) == uf.find(q[1]) :
                ans[q[3]] = True
        return ans

s = Solution()
# print(s.distanceLimitedPathsExist(
#     13,
#     [[9,1,53],[3,2,66],[12,5,99],[9,7,26],[1,4,78],[11,1,62],[3,10,50],[12,1,71],[12,6,63],[1,10,63],[9,10,88],[9,11,59],[1,4,37],[4,2,63],[0,2,26],[6,12,98],[9,11,99],[4,5,40],[2,8,25],[4,2,35],[8,10,9],[11,9,25],[10,11,11],[7,6,89],[2,4,99],[10,4,63]],
#     [[9,7,65],[9,6,1],[4,5,34],[10,8,43],[3,7,76],[4,2,15],[7,6,52],[2,0,50],[7,6,62],[1,0,81],[4,5,35],[0,11,86],[12,5,50],[11,2,2],[9,5,6],[12,0,95],[10,6,9],[9,4,73],[6,10,48],[12,0,91],[9,10,58],[9,8,73],[2,3,44],[7,11,83],[5,3,14],[6,2,33]]
# ))
# print(s.distanceLimitedPathsExist(
#     30,
#     [[9,14,88],[11,27,51],[29,22,58],[29,27,26],[18,20,97],[25,4,12],[2,4,16],[17,18,40],[21,9,37],[3,14,6],[8,23,24],[7,27,39],[24,16,95],[9,29,19],[9,18,22],[26,21,12],[12,14,81],[6,14,79],[3,16,47],[13,19,18],[24,15,59],[14,20,26],[24,20,14],[25,26,7],[13,12,81],[1,0,51],[17,4,39],[8,16,77],[28,9,53],[23,6,40],[29,18,31],[10,9,35],[29,27,7],[1,29,91],[10,19,70],[28,29,58],[20,17,86],[21,14,77],[19,4,43],[26,21,22],[2,26,61],[24,22,16]],
#     [[21,10,1],[14,2,21],[15,11,64],[21,27,17],[3,26,1],[26,18,93],[8,6,5],[18,19,62],[19,18,30],[7,25,76],[0,20,78],[11,6,16],[16,2,91],[22,21,66],[28,24,95],[19,4,18],[14,23,37],[19,27,7],[15,10,83],[23,5,59],[17,12,9],[26,5,90],[26,24,46],[21,29,30],[24,18,54],[27,3,94],[1,23,75],[28,22,75],[27,11,32],[11,20,62],[12,11,10],[17,14,4],[27,22,67],[19,0,25],[16,24,38],[23,6,35],[11,21,96],[28,14,38],[29,17,8],[10,21,85],[2,27,97],[25,13,98]],
# ))