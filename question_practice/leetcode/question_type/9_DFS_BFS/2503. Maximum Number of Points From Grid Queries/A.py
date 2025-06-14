# 2503. Maximum Number of Points From Grid Queries
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries

from typing import List
from math import inf
from heapq import heappush, heappop

# my v2 387ms Beats96.73%
    # direct using tuple to heap is faster
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ans = [0]*len(queries)
        queries = [(que, i) for i, que in enumerate(queries)]
        queries.sort()

        len_c1 = len(grid)
        len_c2 = len(grid[0])
        dir_l = [(1,0),(0,1),(-1,0),(0,-1)]
        not_seen = [[True]*len_c2 for _ in range(len_c1)]
        not_seen[0][0] = False
        heap = [(grid[0][0], 0, 0)]
        cou = 0
        for que, i in queries :
            while heap and que > heap[0][0] :
                _, c1, c2 = heappop(heap)
                cou += 1
                for d1,d2 in dir_l :
                    next1 = c1 + d1
                    next2 = c2 + d2
                    if 0 <= next1 < len_c1 and 0 <= next2 < len_c2 :
                        if not_seen[next1][next2] :
                            not_seen[next1][next2] = False
                            heappush(heap, (grid[next1][next2], next1, next2))
            ans[i] = cou
        return ans

# my v1 675ms Beats58.17%
    # I thought only compare value in heap would be faster
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        class Cell:
            def __init__(self, c1, c2):
                self.value = grid[c1][c2]
                self.c1 = c1
                self.c2 = c2

            def __lt__(self, other): # 如果要創建給 heap 的 class 只需要這個
                # print("using lt")
                return self.value < other.value
            
            # def __gt__(self, other):
            #     print("using gt")
            #     return self.value > other.value
            
            # def __eq__(self, other):
            #     print("using eq")
            #     return self.value == other.value
            
            # def __le__(self, other):
            #     print("using le")
            #     return self.value <= other.value
                
            # def __ge__(self, other):
            #     print("using ge")
            #     return self.value >= other.value
        
        ans = [0]*len(queries)
        queries = [(que, i) for i, que in enumerate(queries)]
        queries.sort()

        len_c1 = len(grid)
        len_c2 = len(grid[0])
        dir_l = [(1,0),(0,1),(-1,0),(0,-1)]
        not_seen = [[True]*len_c2 for _ in range(len_c1)]
        not_seen[0][0] = False
        heap = [Cell(0, 0)]
        cou = 0
        for que, i in queries :
            while heap and que > heap[0].value :
                now_n = heappop(heap)
                cou += 1
                for d1,d2 in dir_l :
                    next1 = now_n.c1 + d1
                    next2 = now_n.c2 + d2
                    if 0 <= next1 < len_c1 and 0 <= next2 < len_c2 :
                        if not_seen[next1][next2] :
                            not_seen[next1][next2] = False
                            heappush(heap, Cell(next1, next2))
            ans[i] = cou
        return ans

s = Solution()
print("ans :",s.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2])) # 
print("ans :",s.maxPoints(grid = [[5,2,1],[1,1,2]], queries = [3])) # 



