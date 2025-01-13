# 3419. Minimize the Maximum Edge Weight of Graph
# https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/description/

from typing import List
import functools

# actually "Each node has at most threshold outgoing edges." is usless, not links, only 'outgoing' edges
    # because after linking and optimize, one node at most have one "outgoing" edges, like tree.

# # my 691ms Beats100.00%
# # fail : almost done, no enough time
import heapq
from collections import defaultdict
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        link = defaultdict(list)
        for n1, n2, w in edges :
            link[n2].append((n1, w))
        
        stack = [(0, 0)]
        max_w = 0
        seen_cou = set()
        while stack :
            new_w, new_n = heapq.heappop(stack)
            if new_n in seen_cou :
                continue
            else :
                seen_cou.add(new_n)
                max_w = max(max_w, new_w)
                if len(seen_cou) == n :
                    return max_w
                for next_n, next_w in link[new_n] :
                    heapq.heappush(stack, (next_w, next_n))
        return -1

# given ans
# 1. No1. same concept, but mine implement method is better
# 2. some are using bisect, but logic is a little bit weird
    # if I can add all the links in (unlimited)
    # why don't I just add all the links that I can link from the smallest to the biggest ? > which is method number 1

s = Solution()
# print("ans :",s.minMaxWeight(n = 5, edges = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]], threshold = 2)) # 1
# print("ans :",s.minMaxWeight(n = 5, edges = [[0,1,1],[0,2,2],[0,3,1],[0,4,1],[1,2,1],[1,4,1]], threshold = 1)) # -1
# print("ans :",s.minMaxWeight(n = 5, edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[3,4,2],[4,0,1]], threshold = 1)) # 2
print("ans :",s.minMaxWeight(n = 5, edges = [[1,0,2],[2,1,1],[3,1,2],[4,1,3]], threshold = 2)) # 2
print("ans :",s.minMaxWeight(n = 5, edges = [[1,0,2],[2,1,1],[3,1,2],[4,1,3],[2,3,4]], threshold = 2)) # 2



