# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

from math import inf
from collections import defaultdict
from heapq import heappop, heappush

# Runtime: 362ms Beats94.86% 
class Solution:
    def networkDelayTime(self, times, n, k):
        start = k
        
        li = defaultdict(list)
        for n1,n2,t in times :
            li[n1].append((n2,t))

        min_path = defaultdict(lambda : inf)
        heap = [(0, start)]
        cnt = 0
        while heap:
            now_path, now_node = heappop(heap)
            if now_path > min_path[now_node] :
                continue
            min_path[now_node] = now_path
            cnt += 1
            if cnt == n:
                return now_path
            for nei_node, nei_w in li[now_node] :
                if (new_path := now_path + nei_w) < min_path[nei_node] :
                    min_path[nei_node] = new_path
                    heappush(heap, (new_path, nei_node))
        return -1

s = Solution()
print(s.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))



