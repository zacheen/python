# 847. Shortest Path Visiting All Nodes
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/description/

from typing import List
from math import inf
from collections import deque

# given ans
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        len_n = len(graph)
        full_status = (1 << len_n) - 1
        queue = deque([(1 << i, i, 0) for i in range(len_n)])
        visited = set()
        
        while queue:
            mask, node, dist = queue.popleft()
            if mask == full_status:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, dist + 1))

s = Solution()
print("ans :",s.shortestPathLength([[1,2,3],[0],[0],[0]])) # 4
print("ans :",s.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]])) # 4
