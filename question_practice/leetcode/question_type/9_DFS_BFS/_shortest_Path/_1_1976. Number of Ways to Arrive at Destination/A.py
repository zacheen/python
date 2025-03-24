# 1976. Number of Ways to Arrive at Destination
# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination

from typing import List
from math import inf
from heapq import heappop, heappush

# my v2 : 15ms Beats90.31% (but I don't know why speed varies so much)
MOD = 10**9+7
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # build link
        li = [[] for _ in range(n)]
        for n1,n2,t in roads :
            li[n1].append((n2,t))
            li[n2].append((n1,t))
        
        final_p = n-1
        min_time = [0]+[inf]*(n-1)
        path_cou = [1]+[0]*(n-1)

        heap = [(0,0)]
        while heap:
            t, dest = heappop(heap)
            # if t > min_time[final_p] : # don't execute this is faster
            #     break
            if t <= min_time[dest] :
                for next_n, add_t in li[dest] :
                    if (new_t := t+add_t) < min_time[next_n] :
                        min_time[next_n] = new_t
                        path_cou[next_n] = path_cou[dest]
                        heappush(heap, (new_t, next_n))
                    elif new_t == min_time[next_n] :
                        path_cou[next_n] += path_cou[dest]
        return path_cou[final_p] % MOD

# # my 32ms Beats9.69%
# MOD = 10**9+7
# class Solution:
#     def countPaths(self, n: int, roads: List[List[int]]) -> int:
#         # build link
#         li = [[] for _ in range(n)]
#         for n1,n2,t in roads :
#             li[n1].append((n2,t))
#             li[n2].append((n1,t))
        
#         final_p = n-1
#         min_time = [inf]*n
#         path_cou = [0]*n + [1]

#         heap = [(0,0,n)]
#         while heap:
#             t, dest, pre_n = heappop(heap)
#             if t > min_time[final_p] :
#                 break
#             if t == (last_min_t := min_time[dest]) :
#                 path_cou[dest] += path_cou[pre_n]
#             elif t < last_min_t :
#                 # non visit node
#                 min_time[dest] = t
#                 path_cou[dest] = path_cou[pre_n]
#                 for next_n, add_t in li[dest] :
#                     if min_time[next_n] == inf :
#                         heappush(heap, (t+add_t, next_n, dest))
#         return path_cou[final_p] % MOD

s = Solution()
print("ans :",s.countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])) # 4
print("ans :",s.countPaths(n = 2, roads = [[1,0,10]])) # 1
# print("ans :",s.countPaths()) # 



