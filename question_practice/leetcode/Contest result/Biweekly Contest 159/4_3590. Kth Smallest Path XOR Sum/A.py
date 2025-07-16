# 3590. Kth Smallest Path XOR Sum
# https://leetcode.com/problems/kth-smallest-path-xor-sum/description/

from typing import List
from math import inf
from sortedcontainers import SortedSet
from collections import defaultdict
from bisect import bisect_left

# v3 inspire by given ans (using bisect is much faster) : 726ms Beats98.07%
class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        len_n = len(par)
        li = [[] for _ in range(len_n)]
        for ch, par in enumerate(par) :
            if par != -1 :
                li[par].append(ch)

        mem_q = defaultdict(list)
        for i, (p, k) in enumerate(queries) :
            mem_q[p].append((i,k))
        ans = [-1]*len(queries)

        def dfs(par, xor_val):
            xor_val ^= vals[par]
            all_poss = [xor_val]
            for ch in li[par]:
                ret = dfs(ch, xor_val)
                if len(ret) > len(all_poss) :
                    all_poss,ret = ret,all_poss
                for new_poss in ret :
                    ins_i = bisect_left(all_poss, new_poss)
                    if ins_i == len(all_poss) or all_poss[ins_i] != new_poss :
                        all_poss.insert(ins_i, new_poss)
        
            # fill ans
            for i,k in mem_q[par]:
                if len(all_poss) >= k :
                    ans[i] = all_poss[k-1]
            return all_poss
        dfs(0, 0)
        return ans

# # my v2 (opt : fill the ans while dfs): 3136ms Beats16.43%
# class Solution:
#     def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
#         len_n = len(par)
#         li = [[] for _ in range(len_n)]
#         for ch, par in enumerate(par) :
#             if par != -1 :
#                 li[par].append(ch)

#         mem_q = defaultdict(list)
#         for i, (p, k) in enumerate(queries) :
#             mem_q[p].append((i,k))
#         ans = [-1]*len(queries)

#         def dfs(par, xor_val):
#             node_val = vals[par]
#             xor_val ^= node_val
#             all_poss = SortedSet([xor_val])
#             for ch in li[par]:
#                 ret = dfs(ch, xor_val)
#                 # inspire by given ans (if none then Time Limit Exceeded)
#                 if len(ret) > len(all_poss) :
#                     all_poss,ret = ret,all_poss
#                 all_poss |= ret
        
#             # fill ans
#             for i,k in mem_q[par]:
#                 if len(all_poss) >= k :
#                     ans[i] = all_poss[k-1]
#             return all_poss
#         dfs(0, 0)
#         return ans

# # my v1 : Memory Limit Exceeded
#     # tree is not balanced
#         # if the situation is that the tree is a line
#         # the memory needed is O(n^2) < (n+1)*n/2
# class Solution:
#     def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
#         len_n = len(par)
#         li = [[] for _ in range(len_n)]
#         for ch, par in enumerate(par) :
#             if par != -1 :
#                 li[par].append(ch)
        
#         mem = [None]*len_n
#         def dfs(par, xor_val):
#             node_val = vals[par]
#             xor_val ^= node_val
#             poss = SortedSet([xor_val])
#             for ch in li[par]:
#                 poss |= dfs(ch, xor_val)
#             mem[par] = poss
#             return poss
#         dfs(0, 0)

#         ans = []
#         for p, k in queries :
#             all_poss = mem[p]
#             if len(all_poss) < k :
#                 ans.append(-1)
#             else :
#                 ans.append(all_poss[k-1])
#         return ans

s = Solution()
print("ans :",s.kthSmallest(par = [-1,0,0], vals = [1,1,1], queries = [[0,1],[0,2],[0,3]])) # [0, 1, -1]
print("ans :",s.kthSmallest(par = [-1,0,1], vals = [5,2,7], queries = [[0,1],[1,2],[1,3],[2,1]])) # [0, 7, -1, 0]
# print("ans :",s.kthSmallest()) # 



