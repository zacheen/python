# 1631. Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

# my 264ms Beats88.09%
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dir_list = [(0,1), (1,0), (0,-1), (-1,0)]
        min_heap = [(0,0,0)]
        seen = defaultdict(set)

        end_n1 = len(heights)-1
        end_n2 = len(heights[0])-1
        while min_heap :
            now_min_diff, now_n1, now_n2 = heappop(min_heap)
            if now_n1 == end_n1 and now_n2 == end_n2 :
                return now_min_diff
            if now_n2 in seen[now_n1] :
                continue
            seen[now_n1].add(now_n2)
            for d1, d2 in dir_list :
                if 0 <= (nei1 := d1+now_n1) <= end_n1 and 0 <= (nei2 := d2+now_n2) <= end_n2 :
                    if nei2 in seen[nei1] : # crucial
                        continue
                    heappush(min_heap, (
                        max(now_min_diff, abs(heights[now_n1][now_n2] - heights[nei1][nei2])),
                        nei1,
                        nei2
                    ))


s = Solution()
print("ans :",s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])) # 2
print("ans :",s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]])) # 1
print("ans :",s.minimumEffortPath([[1,2,1,1,1],
                                   [1,2,1,2,1],
                                   [1,2,1,2,1],
                                   [1,2,1,2,1],
                                   [1,1,1,2,1]])) # 0



