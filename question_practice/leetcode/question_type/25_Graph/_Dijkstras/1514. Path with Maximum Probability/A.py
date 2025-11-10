# 1514. Path with Maximum Probability
# https://leetcode.com/problems/path-with-maximum-probability/

from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

# my 43ms Beats99.86%
class Solution:
    def other_dir(self, dir):
        return 1-dir
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        li = defaultdict(list)
        for (n1, n2), w in zip(edges, succProb):
            li[n1].append((n2, w))
            li[n2].append((n1, w))
        
        # using list to memorize both directions' info
        seen = [set(), set()]
        dists = [{start: 1}, {end: 1}]  # total distances from start and target node
        node_heap = [(-1, start, 0), (-1, end, 1)]  # heap of (distance, node, dir) for choosing next node to expand

        min_dist = 0
        while node_heap:
            # get minimum distance to expand
            now_dist, now_fri, direct = heappop(node_heap)
            now_dist = -now_dist
            if now_dist < dists[direct][now_fri]:
                # Shortest path to now_fri has already been found
                continue
            if now_fri in seen[self.other_dir(direct)]:
                break
            seen[direct].add(now_fri)
            for new_fri, new_weight in li[now_fri]:
                new_dist = now_dist*new_weight
                if new_dist > dists[direct].get(new_fri, 0):
                    dists[direct][new_fri] = new_dist
                    heappush(node_heap, (-new_dist, new_fri, direct))
                    if new_fri in dists[0] and new_fri in dists[1]: # if new_fri connects both sets
                        # check whether this path is better
                        totaldist = dists[0][new_fri]*dists[1][new_fri]
                        if min_dist < totaldist:
                            min_dist = totaldist
        if min_dist == 0:
            return 0
        return min_dist

s = Solution()
print("ans :",s.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2)) # 0.25
print("ans :",s.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2)) # 0.3
print("ans :",s.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2)) # 0



