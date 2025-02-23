# 1557. Minimum Number of Vertices to Reach All Nodes
# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-node

from typing import List
import functools

# my practice again : pick the node with in degree == 0 (must pick, otherwise no can travel it)
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree_0 = set( i for i in range(n) )
        for _,n2 in edges :
            in_degree_0.discard(n2)
        return list(in_degree_0)

# given ans : Beats 71.40%
# 用 mem 紀錄 哪些點走過了
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        not_seen_mem = [True] * n
        for _, v in edges:
            not_seen_mem[v] = False
        return [i for i, not_seen in enumerate(not_seen_mem) if not_seen]
  
s = Solution()
print(s.findSmallestSetOfVertices())



