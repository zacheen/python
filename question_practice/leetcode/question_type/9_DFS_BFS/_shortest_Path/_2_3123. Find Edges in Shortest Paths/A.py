# 3123. Find Edges in Shortest Paths
# https://leetcode.com/problems/find-edges-in-shortest-paths/description/

from typing import List
from math import inf
from heapq import heappop, heappush
from functools import cache

# (heap shortest path)
# my v2 this implement method is faster again : 529ms Beats83.87%
class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        li = [[] for _ in range(n)]
        # build
        for i,(n1,n2,w) in enumerate(edges) :
            li[n1].append((w,n2,i))
            li[n2].append((w,n1,i))
        
        # mem the path_indexs that can reach [i] with min_weight
        mem_min_p = [inf]*n
        mem_pre = [[] for _ in range(n)] # (previous_node, path_i)
        heap = [(0,0)]
        mem_min_p[0] = 0
        while heap :
            path_w, now_n = heappop(heap)
            if path_w == mem_min_p[now_n] :
                for add_w, next_n, path_i in li[now_n] :
                     
                    if (new_w := path_w+add_w) < (pre_min_p := mem_min_p[next_n]) :
                        # new visited with min w
                        mem_pre[next_n] = [(now_n, path_i)]
                        mem_min_p[next_n] = new_w
                        heappush(heap, (new_w, next_n))
                    elif new_w == pre_min_p :
                        mem_pre[next_n].append((now_n, path_i))
        
        ans = [False]*len(edges)
        @cache
        def dfs(now_n) :
            if now_n == 0 :
                return
            for pre_n, path_i in mem_pre[now_n] :
                ans[path_i] = True
                dfs(pre_n)
        dfs(n-1)
        dfs.cache_clear()
        return ans

# # my v1 907ms Beats15.48%
# class Solution:
#     def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
#         li = [[] for _ in range(n)]
#         # build
#         for i,(n1,n2,w) in enumerate(edges) :
#             li[n1].append((w,n2,i))
#             li[n2].append((w,n1,i))
        
#         # mem the path_indexs that can reach [i] with min_weight
#         mem_min_p = [inf]*n
#         mem_pre = [[] for _ in range(n)] # (previous_node, path_i)
#         final_p = n-1
#         heap = [(0,0)]
#         mem_min_p[0] = 0
#         while heap :
#             path_w, now_n = heappop(heap)
#             if path_w <= mem_min_p[now_n] :
#                 for add_w, next_n, path_i in li[now_n] :
#                     if (new_w := path_w+add_w) < mem_min_p[next_n] :
#                         # new visited with min w
#                         _ = mem_pre[next_n]
#                         mem_pre[next_n] = [(now_n, path_i)]
#                         mem_min_p[next_n] = new_w
#                         heappush(heap, (new_w, next_n))
#                     elif new_w == mem_min_p[next_n] :
#                         mem_pre[next_n].append((now_n, path_i))
        
#         ans = [False]*len(edges)
#         @cache
#         def dfs(now_n) :
#             if now_n == 0 :
#                 return
#             for pre_n, path_i in mem_pre[now_n] :
#                 ans[path_i] = True
#                 dfs(pre_n)
#         dfs(final_p)
#         dfs.cache_clear()
#         return ans

# given ans


s = Solution()
print("ans :",s.findAnswer(n = 6, \
    edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]])) 
           # [true,  true,   true,   false,  true,   true,   true,   false]
print("ans :",s.findAnswer(n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]])) # 
# print("ans :",s.findAnswer()) # 



