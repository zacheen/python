# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance

from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

# my 74ms Beats99.43%
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # do Dijkstra with every node
        # Dijkstra(100*100*log100) * nodes(100)

        li = defaultdict(list)
        for n1,n2,w in edges :
            li[n1].append((n2,w))
            li[n2].append((n1,w))

        all_min_path = defaultdict(list)
        min_cnt = n+1
        min_indx = -1
        for each_node in range(n-1, -1, -1):
            min_path = defaultdict(lambda : inf)
            min_path[each_node] = 0
            heap = [(0, each_node)]
            # optimized
            for dp_node, dp_dist in all_min_path[each_node]:
                heappush(heap, (dp_dist, dp_node))
                min_path[dp_node] = dp_dist
            
            new_cnt = 0
            while heap and new_cnt < min_cnt:
                now_path, now_node = heappop(heap)
                if now_path > distanceThreshold :
                    break
                if now_path > min_path[now_node] :
                    continue
                new_cnt += 1
                all_min_path[now_node].append((each_node, now_path))
                for nei_node, nei_w in li[now_node] :
                    if (new_path := now_path + nei_w) < min_path[nei_node] :
                        min_path[nei_node] = new_path
                        heappush(heap, (new_path, nei_node))
            if new_cnt < min_cnt :
                min_cnt = new_cnt
                min_indx = each_node
        return min_indx
            

s = Solution()
print("ans :",s.findTheCity(5, [[0,1,2],[0,4,8],[1,2,10000],[1,4,2],[2,3,10000],[3,4,1]], 10000)) # 
# print("ans :",s.findTheCity()) # 



