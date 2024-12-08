# 3367. Maximize Sum of Weights after Edge Removals
# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/description/

from typing import List
import functools

# my + given ans' opt 567ms Beats94.87%
import heapq
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        links = [[] for _ in range(len(edges)+1)]
        for n1,n2,v in edges :
            links[n1].append((n2,v))
            links[n2].append((n1,v))
        km1 = k-1
        def dfs(n, pre):
            each_diff = []
            tot_w = 0
            for each_l, w in links[n]:
                if each_l != pre :
                    pre_to_w_k, pre_to_w_k_m1 = dfs(each_l, n)
                    tot_w += pre_to_w_k
                    diff = (pre_to_w_k_m1+w)-pre_to_w_k # diff is bigger, more important to get this w
                    if diff > 0 :
                        each_diff.append(diff) # max(0 因為如果 diff 是負的 一定就不要選
            each_diff.sort(reverse=True)
            # print(n, each_diff, tot_w)
            total_diff = sum(each_diff[:km1])
            to_km1 = total_diff + tot_w
            if km1 >= len(each_diff) :
                # print(n, to_km1, to_km1)
                return to_km1, to_km1
            else :
                # print(n, to_km1 + each_diff[km1], to_km1)
                return to_km1 + each_diff[km1], to_km1
            
        return max(dfs(0, -1))

# # # my v1 895ms Beats66.13%
# import heapq
# class Solution:
#     def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
#         links = [[] for _ in range(len(edges)+1)]
#         for n1,n2,v in edges :
#             links[n1].append((n2,v))
#             links[n2].append((n1,v))
#         km1 = k-1
#         def dfs(n, pre):
#             each_n_w = []
#             tot_w = 0
#             for each_l, w in links[n]:
#                 if each_l == pre :
#                     continue
#                 pre_to_w_k, pre_to_w_k_m1 = dfs(each_l, n)
#                 choose_w = pre_to_w_k_m1+w
#                 diff = choose_w-pre_to_w_k # diff is bigger, more important to get this w
#                 if diff <= 0:
#                     tot_w += pre_to_w_k
#                 else :
#                     each_n_w.append((diff, choose_w, pre_to_w_k))
#             each_n_w.sort(reverse=True)
#             # print(n, each_n_w)
#             r0_km1 = sum( w1 for _, w1, w2 in each_n_w[:km1] )
#             rk_end = sum( w2 for _, w1, w2 in each_n_w[k:] )
#             tot_w += (r0_km1+rk_end)
#             if km1 >= len(each_n_w) :
#                 # print(n, tot_w, tot_w)
#                 return tot_w, tot_w
#             else :
#                 _, wk, wkm1 = each_n_w[km1]
#                 # print(n, tot_w+wk, tot_w+wkm1)
#                 return tot_w+wk, tot_w+wkm1
#         return max(dfs(0, -1))  

# # given ans 922ms Beats62.03%
# import heapq
# class Solution:
#     def maximizeSumOfWeights(self, edges: list[list[int]], k: int) -> int:
#         graph = [[] for _ in range(len(edges) + 1)]

#         for u, v, w in edges:
#             graph[u].append((v, w))
#             graph[v].append((u, w))

#         def dfs(u: int, prev: int) -> tuple[int, int]:
#             """
#             Returns
#             (the weight sum of the subtree rooted at u with at most k - 1 children,
#              the weight sum of the subtree rooted at u with at most k children).
#             """
#             weightSum = 0
#             diffs = []
#             for v, w in graph[u]:
#                 if v == prev:
#                     continue
#                 subK1, subK = dfs(v, u)
#                 weightSum += subK
#                 # If picking (u, v) makes the sum larger, we should pick it.
#                 diffs.append(max(0, subK1 - subK + w)) # (subK1 - subK + w) 取用這個k 會多多少
#             return (weightSum + sum(heapq.nlargest(k - 1, diffs)), 
#                         weightSum + sum(heapq.nlargest(k, diffs)))
#         return dfs(0, -1)[1]

s = Solution()
print("ans :",s.maximizeSumOfWeights(edges = [[0,1,4],[0,2,2],[2,3,12],[2,4,6]], k = 2))
print("ans :",s.maximizeSumOfWeights(edges = [[0,1,5],[1,2,10],[0,3,15],[3,4,20],[3,5,5],[0,6,10]], k = 3))
print("ans :",s.maximizeSumOfWeights(edges = [[0,1,3],[2,3,3],[1,2,5]], k = 2))
print("ans :",s.maximizeSumOfWeights(edges = [[0,1,34],[0,2,17]], k = 1))
print("ans :",s.maximizeSumOfWeights(edges = [[0,1,25],[0,2,10],[1,3,29]], k = 1))
# print("ans :",s.maximizeSumOfWeights(edges = [[0,1,3],[1,2,20],[1,3,10]], k = 2))



