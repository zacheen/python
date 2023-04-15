from typing import List
import functools

# my Time Limit Exceeded
from sortedcontainers import SortedList
from math import inf
from operator import neg
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.distance = [[inf]*n for _ in range(n)]
        self.path = [[] for _ in range(n)]
        for p1,p2,cost in edges :
            self.path[p1].append((p2, cost))
        # print("path :",self.path)
        self.fill_distance()
        
    def fill_distance(self):
        self.distance = [[inf]*self.n for _ in range(self.n)]
        for i in range(self.n) :
            self.distance[i][i] = 0
            stack = SortedList([(0,i)]) #(cost, p)
            while stack :
                total_cost, cost_less_p = stack.pop()
                for new_point, cost in self.path[cost_less_p] :
                    new_cost = total_cost + cost
                    if new_cost < self.distance[i][new_point] :
                        self.distance[i][new_point] = new_cost
                        stack.add((new_cost, new_point))
        # print("distance :",self.distance)
        

    def addEdge(self, edge: List[int]) -> None:
        self.path[edge[0]].append((edge[1], edge[2]))
        self.fill_distance()
        return

    def shortestPath(self, node1: int, node2: int) -> int:
        ret = self.distance[node1][node2]
        if ret == inf :
            ret = -1
        return ret

# given ans

# s = Solution()
# print(s.())



