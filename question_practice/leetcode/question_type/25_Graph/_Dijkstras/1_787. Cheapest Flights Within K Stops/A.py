# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops

from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

# 後面比較長的路徑 會覆蓋前面比較短的路徑 但是 stop 會減少
# my 17ms Beats54.14%
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        li = defaultdict(list)
        for n1,n2,w in flights :
            li[n1].append((n2,w))
        
        dists = defaultdict(lambda : defaultdict(lambda : inf))
        # dists[src][k+1] = 0
        min_heap = [ (0, src, k+1) ] # k stops means k+1 nodes
        while min_heap :
            now_dist, now_node, now_stop = heappop(min_heap)
            if now_node == dst :
                return now_dist
            if now_stop > 0 :
                for next_node, next_dist in li[now_node] :
                    new_dist = now_dist + next_dist
                    if new_dist < dists[next_node][now_stop-1] :
                        dists[next_node][now_stop-1] = new_dist
                        heappush(min_heap, (new_dist, next_node, now_stop-1))
        return -1

s = Solution()
print("ans :",s.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 
                                  src = 0, dst = 3, k = 1)) # 700
print("ans :",s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], 
                                  src = 0, dst = 2, k = 1)) # 200
print("ans :",s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], 
                                  src = 0, dst = 2, k = 0)) # 500



