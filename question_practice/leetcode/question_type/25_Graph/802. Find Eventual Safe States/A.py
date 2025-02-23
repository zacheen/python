# 802. Find Eventual Safe States
# https://leetcode.com/problems/find-eventual-safe-states/description

from typing import List
import functools

# my 27ms Beats89.20%
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        circle_n = set()
        ans = set()
        path = set()
        def check_circle(n):
            if (n in circle_n) or (n in path) :
                return True
            if n in ans :
                return False
            path.add(n)
            for next_n in graph[n] :
                if check_circle(next_n) :
                    circle_n.add(n)
                    return True
            ans.add(n)
            path.remove(n)
            return False
        return [i for i in range(len(graph)) if not check_circle(i)]

# given ans : 59ms Beats41.26%
    # I thought it would be faster, but actually slower...
# using state to mem 
kInit = 0
kVisiting = 1
kVisited = 2
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        states = [kInit] * len(graph)
        def hasCycle(u: int) -> bool:
            if states[u] == kVisiting:
                return True
            if states[u] == kVisited:
                return False
            states[u] = kVisiting
            if any(hasCycle(v) for v in graph[u]):
                return True
            states[u] = kVisited
        return [i for i in range(len(graph)) if not hasCycle(i)]
    
s = Solution()
print("ans :",s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])) # [2,4,5,6]
print("ans :",s.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]])) # [4]
print("ans :",s.eventualSafeNodes([[],[0,2,3,4],[3],[4],[]])) # [0, 1, 2, 3, 4]



