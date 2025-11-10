# 3650. Minimum Cost Path with Edge Reversals
# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/description/

from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

# my 712ms Beats47.02%
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        li = defaultdict(list)
        rev_li = defaultdict(list)
        # build
        for n1,n2,cost in edges :
            li[n1].append((n2,cost))
            rev_li[n2].append((n1,cost*2))
        
        seen = set()
        heap_mem = [(0,0)] # [cost, node]
        end_node = n-1
        while heap_mem :
            now_cost, now_node = heappop(heap_mem)
            if now_node == end_node :
                return now_cost
            if now_node in seen :
                continue
            seen.add(now_node)
            for next_node, next_cost in li[now_node] :
                heappush(heap_mem, (now_cost+next_cost, next_node))
            for next_node, next_cost in rev_li[now_node] :
                heappush(heap_mem, (now_cost+next_cost, next_node))
        return -1

# # my fail : I thought only can switch once
# class Solution:
#     def minCost(self, n: int, edges: List[List[int]]) -> int:
#         li = defaultdict(list)
#         rev_li = defaultdict(list)
#         # build
#         for n1,n2,cost in edges :
#             li[n1].append((n2,cost))
#             rev_li[n2].append((n1,cost*2))
        
#         seen = [set(), set()] # [non_rev, rev]
#         heap_mem = [(0,0,0)] # [cost, node, rev_flag]
#         end_node = n-1
#         while heap_mem :
#             now_cost, now_node, rev_flag = heappop(heap_mem)
#             if now_node == end_node :
#                 return now_cost
#             if now_node in seen[rev_flag] :
#                 continue
#             seen[rev_flag].add(now_node)
#             for next_node, next_cost in li[now_node] :
#                 heappush(heap_mem, (now_cost+next_cost, next_node, rev_flag))
#             if rev_flag == 0 :
#                 for next_node, next_cost in rev_li[now_node] :
#                     heappush(heap_mem, (now_cost+next_cost, next_node, 1))
#         return -1


s = Solution()
print("ans :",s.minCost(n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]])) # 5
print("ans :",s.minCost(n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]])) # 3



