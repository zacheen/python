# my ver1
# 沒思考清楚 binary tree 的定義
# class UF:
#     def __init__(self, n):
#         self.id = list(range(n))

#     def union(self, u, v):
#         i = self.find(u)
#         j = self.find(v)
#         if i == j:
#             return
#         self.id[i] = j

#     def find(self, u):
#         if self.id[u] != u:
#             self.id[u] = self.find(self.id[u])
#         return self.id[u]

# from collections import Counter
# class Solution:
#     def cost_fuel(self, union_count, seat):
#         mod = union_count // seat
#         return ((mod+1)*mod//2)*seat + (union_count % seat)*(mod+1)

#     def minimumFuelCost(self, roads, seats):
#         # 先找出所有的路徑
#         # 再計算每條路徑所需的油量

#         # ->
#         # 因為是 tree 所以 我只要分 union (找最末端的點)
#         # 然後計算每個區域所需的 fuel 數量

#         # print("test :",self.cost_fuel(4,3)) # 4 + 1
#         # print("test :",self.cost_fuel(7,3)) # 7 + 4 + 1

#         union = UF(len(roads)+1)
#         for d1,d2 in roads :
#             if d1 == 0 or d2 == 0:
#                 continue
#             union.union(d1, d2)
        
#         count = Counter()
#         for i in range(1, len(roads)+1):
#             count[union.find(i)] += 1

#         total_fuel = 0
#         for each_union_city_count in count.values():
#             total_fuel += self.cost_fuel(each_union_city_count, seats)
#         return total_fuel

# Beats 73.48%
class Solution:
    def minimumFuelCost(self, roads, seats):
        # DFS 每個點
        # 回到上一個點紀錄在此點有多少人 需要多少車 ( 人 // seats 若有餘數 + 1 台車) 

        graph = [[] for _ in range(len(roads) + 1)]
        for d1,d2 in roads :
            graph[d1].append(d2)
            graph[d2].append(d1)

        def DFS(point, prev_point):
            total_num = 0
            total_cost = 0
            for p in graph[point] :
                if p == prev_point :
                    continue
                return_num, return_cost = DFS(p, point)
                total_num += return_num
                total_cost += return_cost
            
            if prev_point == None :
                return total_num, total_cost
            # cal this point change
            total_num += 1
            # cal this point to father point cost
            total_cost += ((total_num-1)//seats)+1
            return total_num, total_cost
        return DFS(0, None)[1]


# # given ans
# 跟我的差不多 只是 total_cost 使用 global 去加
# import math
# class Solution:
#     def minimumFuelCost(self, roads, seats):
#         ans = 0
#         graph = [[] for _ in range(len(roads) + 1)]

#         for u, v in roads:
#             graph[u].append(v)
#             graph[v].append(u)

#         def dfs(u, prev):
#             nonlocal ans
#             people = 1
#             for v in graph[u]:
#                 if v == prev:
#                     continue
#                 people += dfs(v, u)
#             if u > 0:
#                 # of cars needed.
#                 ans += int(math.ceil(people / seats))
#             return people

#         dfs(0, -1)
#         return ans

s = Solution()
print(s.minimumFuelCost(roads = [[0,1],[0,2],[0,3]], seats = 5))
print(s.minimumFuelCost(roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2))
print(s.minimumFuelCost(roads = [[1,0],[0,2],[3,1],[1,4],[5,0]], seats = 1))
print(s.minimumFuelCost(roads = [[1,0],[1,2],[3,2]], seats = 1))



