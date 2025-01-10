# 2940. Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description

from typing import List
import functools

# my opt 279ms Beats95.83%
from collections import defaultdict
import heapq
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ret = [-1]*len(queries)
        remain_q = defaultdict(list)
        for q_indx, (h1_indx, h2_indx) in enumerate(queries) :
            if h1_indx == h2_indx:
                ret[q_indx] = h2_indx
                continue
            if h1_indx < h2_indx :
                h1_indx, h2_indx = h2_indx, h1_indx
            # h1_indx > h2_indx
            if  heights[h1_indx] > heights[h2_indx]:
                # print("dir",q_indx, h2_indx)
                ret[q_indx] = h1_indx
            else :
                remain_q[h1_indx].append(
                    (max(heights[h1_indx], heights[h2_indx]), q_indx)
                )
        
        ava_q = []
        for h_indx, h in enumerate(heights) :
            while ava_q and h > ava_q[0][0] :
                # print("meet",q_indx, h_indx)
                ret[heapq.heappop(ava_q)[1]] = h_indx
            for q in remain_q[h_indx] :
                heapq.heappush(ava_q, q)
        return ret
    
# # given ans 279ms Beats95.83%
# import heapq
# class Solution:
#     def leftmostBuildingQueries(self, heights, queries):
#         results = [-1] * len(queries)
#         store_queries = [[] for _ in heights]

#         # Store the mappings for all queries in store_queries.
#         for q_indx, query in enumerate(queries):
#             a, b = query
#             # 主要是因為下面 max_idx[0][0] < height 不包含 ==, 所以要先排除相同點的狀況
#             if a < b and heights[a] < heights[b]:
#                 results[q_indx] = b
#             elif a > b and heights[a] > heights[b]:
#                 results[q_indx] = a
#             elif a == b:
#                 results[q_indx] = a
#             else:
#                 store_queries[max(a, b)].append(          # available indx
#                     (max(heights[a], heights[b]), q_indx) # (available height, q_indx)
#                 )

#         max_idx = []  # Min-heap to simulate priority queue
#         for h_idx, height in enumerate(heights):
#             # 從前往後掃 indx一定最小，heap 幫忙判斷有沒有符合的 query
#             while max_idx and max_idx[0][0] < height:
#                 _, q_idx = heapq.heappop(max_idx)
#                 results[q_idx] = h_idx
#             # 把 h_idx 的 query 加入，下一個for一定會大於 h_idx
#             for element in store_queries[h_idx]:
#                 heapq.heappush(max_idx, element)
#         return results

# # my
# from collections import defaultdict
# import heapq
# class Solution:
#     def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
#         min_indx = [len(heights)]*len(heights)
#         stack = []
#         for i, h in enumerate(heights) :
#             while stack and h > stack[-1][1]:
#                 s_i, s_h = stack.pop()
#                 min_indx[s_i] = i
#             stack.append((i,h))
        
#         ret = [-1]*len(queries)
#         for q_indx, (h1, h2) in enumerate(queries) :
#             if h1 == h2:
#                 ret[q_indx] = h2
#                 continue
#             if h1 < h2 :
#                 h1, h2 = h2, h1
#             # h1 > h2
#             if  heights[h1] > heights[h2]:
#                 print("dir",q_indx, h2)
#                 ret[q_indx] = h1
#             elif min_indx[h2] > h1 :
#                 temp = max(min_indx[h1], min_indx[h2])
#                 ret[q_indx] = temp if temp != len(heights) else -1
#             else :
#                 # fail dealing this part
#         return ret

s = Solution()
print("ans :",s.leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]])) # [2,5,-1,5,2] 
print("ans :",s.leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]])) # [7,6,-1,4,6]
# print("ans :",s.leftmostBuildingQueries(heights = [3,4,1,2], queries = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]])) 
# print("ans :",s.leftmostBuildingQueries(heights = [3,4,1,2], queries = [[0,2]])) 



