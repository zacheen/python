# 1976. Number of Ways to Arrive at Destination
# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination

from typing import List
from math import inf
from heapq import heappop, heappush

# my Dijkstra
MOD = 10**9+7
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # build link
        li = [[] for _ in range(n)]
        for n1,n2,t in roads :
            li[n1].append((n2,t))
            li[n2].append((n1,t))
        
        final_p = n-1
        min_time = [0]+[inf]*(n-1)
        path_cou = [1]+[0]*(n-1)

        heap = [(0,0)]
        while heap:
            t, dest = heappop(heap)
            # if t > min_time[final_p] : # don't execute this is faster
            #     break
            if t <= min_time[dest] :
                for next_n, add_t in li[dest] :
                    if (new_t := t+add_t) < min_time[next_n] :
                        min_time[next_n] = new_t
                        path_cou[next_n] = path_cou[dest]
                        heappush(heap, (new_t, next_n))
                    elif new_t == min_time[next_n] :
                        path_cou[next_n] += path_cou[dest]
        return path_cou[final_p] % MOD

# Bidirectional Dijkstra, when one node reaching other side, counting will be duplicate
    # relation 0-1
        # Both 0->1 and 1->0 will be counted

s = Solution()
print("ans :",s.countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])) # 4
print("ans :",s.countPaths(n = 2, roads = [[1,0,10]])) # 1
# print("ans :",s.countPaths()) # 



