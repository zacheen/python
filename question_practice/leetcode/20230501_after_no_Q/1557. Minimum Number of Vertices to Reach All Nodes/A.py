# 1557. Minimum Number of Vertices to Reach All Nodes
# 

from typing import List
import functools

# my Beats 81.2%
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        not_been_pointed = set(range(n)) # 沒有被指到的點
        for n1, n2 in edges :
            if n2 in not_been_pointed :
                not_been_pointed.remove(n2)
        return not_been_pointed

# given ans
    # 速度差不多 : Beats 71.40%
# 用 mem 紀錄 哪些點走過了
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        not_seen_mem = [True] * n
        for _, v in edges:
            not_seen_mem[v] = False
        return [i for i, not_seen in enumerate(not_seen_mem) if not_seen]
  
s = Solution()
print(s.findSmallestSetOfVertices())



