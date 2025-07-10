# 3604. Minimum Time to Reach Destination in Directed Graph
# https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/description/

from typing import List
from math import inf
from collections import defaultdict
from heapq import heappush, heappop

# my 191ms Beats57.98%
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        li = defaultdict(list)
        for n1, n2, st, en in edges :
            li[n1].append((st, en, n2))

        end_i = n-1
        heap = [(0,0)]
        seen = set()
        while heap :
            arr_time, n1 = heappop(heap)
            if n1 == end_i : 
                return arr_time
            if n1 in seen : 
                continue
            seen.add(n1)
            for new_st, new_en, new_n2 in li[n1] :
                if new_n2 in seen : 
                    continue
                if new_en < arr_time : 
                    continue
                heappush(heap, (max(arr_time, new_st)+1, new_n2))
        return -1

s = Solution()
print("ans :",s.minTime(n = 3, edges = [[0,1,0,1],[1,2,2,5]])) # 3
print("ans :",s.minTime(n = 4, edges = [[0,1,0,3],[1,3,7,8],[0,2,1,5],[2,3,4,7]])) # 5
print("ans :",s.minTime(n = 3, edges = [[1,0,1,3],[1,2,3,5]])) # -1



