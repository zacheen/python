from typing import List
import functools
from sortedcontainers import SortedList
from math import inf

# # my Time Limit Exceeded
# class Graph:
#     def __init__(self, n: int, edges: List[List[int]]):
#         self.n = n
#         self.distance = [[inf]*n for _ in range(n)]
#         self.path = [[] for _ in range(n)]
#         for p1,p2,cost in edges :
#             self.path[p1].append((p2, cost))
#         # print("path :",self.path)
#         self.fill_distance()
        
#     def fill_distance(self):
#         # 沒想到要怎麼減少這裡的時間複雜度
#         # 我再想 這裡應該可以變成 order N
#         self.distance = [[inf]*self.n for _ in range(self.n)]
#         for i in range(self.n) :
#             self.distance[i][i] = 0
#             stack = SortedList([(0,i)]) #(cost, p)
#             while stack :
#                 total_cost, cost_less_p = stack.pop()
#                 for new_point, cost in self.path[cost_less_p] :
#                     new_cost = total_cost + cost
#                     if new_cost < self.distance[i][new_point] :
#                         self.distance[i][new_point] = new_cost
#                         stack.add((new_cost, new_point))
#         # print("distance :",self.distance)
        

#     def addEdge(self, edge: List[int]) -> None:
#         self.path[edge[0]].append((edge[1], edge[2]))
#         # 沒想到要怎麼減少這裡的時間複雜度
#         self.fill_distance()
#         return

#     def shortestPath(self, node1: int, node2: int) -> int:
#         ret = self.distance[node1][node2]
#         if ret == inf :
#             ret = -1
#         return ret
    
# # my v2  Time Limit Exceeded
# class Graph:
#     def __init__(self, n: int, edges: List[List[int]]):
#         self.n = n
#         self.path = [[] for _ in range(n)]
#         for p1,p2,cost in edges :
#             self.path[p1].append((p2, cost))

#     def addEdge(self, edge: List[int]) -> None:
#         self.path[edge[0]].append((edge[1], edge[2]))
#         return

#     def shortestPath(self, node1: int, node2: int) -> int:
#         distance = [inf]*self.n
#         distance[node1] = 0
#         stack = SortedList([(0,node1)]) #(cost, p)
#         while stack :
#             total_cost, cost_less_p = stack[0]
#             del(stack[0])
#             for new_point, cost in self.path[cost_less_p] :
#                 new_cost = total_cost + cost
#                 if new_cost < distance[new_point] :
#                     distance[new_point] = new_cost
#                     stack.add((new_cost, new_point))
#                 if new_point == node2 :
#                     return new_cost
#         return -1

# # my v3 研究 SortedList 之後調整 Beats 41.84%
# # 解 BUG : 判斷 if cost_less_p == node2 : 的位置
# from sortedcontainers import SortedList
# from math import inf
# class Graph:
#     def __init__(self, n: int, edges: List[List[int]]):
#         self.n = n
#         self.path = [[] for _ in range(n)]
#         for e in edges :
#             self.addEdge(e)
#         # print(self.path)

#     def addEdge(self, edge: List[int]) -> None:
#         self.path[edge[0]].append((edge[1], edge[2]))
#         return

#     def shortestPath(self, node1: int, node2: int) -> int:
#         distance = [inf]*self.n
#         distance[node1] = 0
#         stack = SortedList([(0,node1)], key=lambda x: -x[0]) #(cost, p)
#         while stack :
#             # print(stack)
#             total_cost, cost_less_p = stack.pop()
#             if cost_less_p == node2 :
#                 return total_cost
#             # print(total_cost, cost_less_p, self.path[cost_less_p])
#             for new_point, cost in self.path[cost_less_p] :
#                 new_cost = total_cost + cost
#                 # print("for", new_cost, total_cost, cost, new_point)
#                 if new_cost < distance[new_point] :
#                     distance[new_point] = new_cost
#                     stack.add((new_cost, new_point))
#                     # print("add",new_cost, new_point)
#         return -1
    
# my v3.5 參考 given ans 優化 Beats 45.12%
from sortedcontainers import SortedList
from math import inf
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.path = [[] for _ in range(n)]
        for e in edges :
            self.addEdge(e)
        # print(self.path)

    def addEdge(self, edge: List[int]) -> None:
        self.path[edge[0]].append((edge[1], edge[2]))
        return

    def shortestPath(self, node1: int, node2: int) -> int:
        distance = [inf]*self.n
        distance[node1] = 0
        stack = SortedList([(0,node1)], key=lambda x: -x[0]) #(cost, p)
        while stack :
            # print(stack)
            total_cost, cost_less_p = stack.pop()
            if cost_less_p == node2 :
                return total_cost
            if total_cost > distance[cost_less_p]:
                continue
            # print(total_cost, cost_less_p, self.path[cost_less_p])
            for new_point, cost in self.path[cost_less_p] :
                new_cost = total_cost + cost
                # print("for", new_cost, total_cost, cost, new_point)
                if new_cost < distance[new_point] :
                    distance[new_point] = new_cost
                    stack.add((new_cost, new_point))
                    # print("add",new_cost, new_point)
        return -1

# # my v4 改成紀錄路徑 竟然比較慢 Beats 10.69%
# from sortedcontainers import SortedList
# from math import inf
# class Graph:
#     def __init__(self, n: int, edges: List[List[int]]):
#         self.n = n
#         self.path = [[] for _ in range(n)]
#         for e in edges :
#             self.addEdge(e)
#         # print(self.path)

#     def addEdge(self, edge: List[int]) -> None:
#         self.path[edge[0]].append((edge[1], edge[2]))
#         return

#     def shortestPath(self, node1: int, node2: int) -> int:
#         mem_path = set()
#         stack = SortedList([(0,node1)], key=lambda x: -x[0]) #(cost, p)
#         while stack :
#             # print(stack)
#             total_cost, cost_less_p = stack.pop()
#             if cost_less_p == node2 :
#                 return total_cost
#             if cost_less_p in mem_path :
#                 continue
#             mem_path.add(cost_less_p)
#             # print(total_cost, cost_less_p, self.path[cost_less_p])
#             for new_point, cost in self.path[cost_less_p] :
#                 new_cost = total_cost + cost
#                 # print("for", new_cost, total_cost, cost, new_point)
#                 stack.add((new_cost, new_point))
#                 # print("add",new_cost, new_point)
#         return -1
    
# my v4.5 優化 v4 Beats 17.25%
# 真的不懂為什麼比較慢
from sortedcontainers import SortedList
from math import inf
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.path = [[] for _ in range(n)]
        for e in edges :
            self.addEdge(e)
        # print(self.path)

    def addEdge(self, edge: List[int]) -> None:
        self.path[edge[0]].append((edge[1], edge[2]))
        return

    def shortestPath(self, node1: int, node2: int) -> int:
        mem_path = [False]*self.n
        stack = SortedList([(0,node1)], key=lambda x: -x[0]) #(cost, p)
        while stack :
            # print(stack)
            total_cost, cost_less_p = stack.pop()
            if cost_less_p == node2 :
                return total_cost
            if mem_path[cost_less_p] :
                continue
            mem_path[cost_less_p] = True
            # print(total_cost, cost_less_p, self.path[cost_less_p])
            for new_point, cost in self.path[cost_less_p] :
                if mem_path[new_point] == False :
                    new_cost = total_cost + cost
                    # print("for", new_cost, total_cost, cost, new_point)
                    stack.add((new_cost, new_point))
                    # print("add",new_cost, new_point)
        return -1
    
# given ans Beats 45.12% -> 95.86%
# 其他架構完全相同，只差在使用 heap
# 用 heap 因為只要找最小的那一個cost路徑就好了
    # 我記得 heap 的時間複雜度比較小
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        x, y, z = edge
        self.graph[x].append((y, z))

    def shortestPath(self, node1: int, node2: int) -> int:
        START_NODE = node1
        distances = [inf] * self.n
        distances[START_NODE] = 0 
        heap = [(0, START_NODE)]
        while heap:
            cur_dist, cur_node = heappop(heap)
            if cur_node == node2:
                return cur_dist
            
            if cur_dist > distances[cur_node]:
                continue
                
            for nei, w in self.graph[cur_node]:
                dist = cur_dist + w
                if dist < distances[nei]:
                    distances[nei] = dist
                    heappush(heap, (dist, nei))
        return -1
    
# s = Solution()
# print(s.())



