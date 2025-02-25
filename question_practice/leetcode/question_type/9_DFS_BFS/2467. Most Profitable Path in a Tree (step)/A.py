# 2467. Most Profitable Path in a Tree
# https://leetcode.com/problems/most-profitable-path-in-a-tree

from typing import List
from math import inf

# # my 176ms Beats96.95%
# def link(relation, len_n = -1):
#     li = [[] for _ in range(len_n)]
#     # build
#     for n1,n2 in relation :
#         li[n1].append(n2)
#         li[n2].append(n1)
#     return li

# class Solution:
#     def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
#         li = link(edges, len(edges)+1)

#         path = []
#         def dfs_find_0(now_p, pre_p):
#             if now_p == 0: 
#                 return True
#             for next_p in li[now_p] :
#                 if next_p == pre_p :
#                     continue
#                 if dfs_find_0(next_p, now_p) :
#                     path.append(next_p)
#                     return True
#             return False
#         dfs_find_0(bob, -1)
#         path = [bob] + list(reversed(path))

#         max_ans = -inf
#         def dfs(now_n, pre_n, step, now_s):
#             bob_move = False
#             if step < len(path) :
#                 bob_move = True
#                 bob_now_n = path[step]
#                 if bob_now_n == now_n :
#                     now_s += amount[now_n] // 2
#                 else :
#                     now_s += amount[now_n]
#             else :
#                 now_s += amount[now_n]
            
#             if len(li[now_n]) == 1 and step > 0:
#                 nonlocal max_ans
#                 if now_s > max_ans :
#                     max_ans = now_s
#                 return 
            
#             if bob_move :
#                 mem_amount = amount[bob_now_n]
#                 amount[bob_now_n] = 0
#             for nei_n in li[now_n] :
#                 if nei_n == pre_n :
#                     continue
#                 dfs(nei_n, now_n, step+1, now_s)
#             if bob_move :
#                 amount[bob_now_n] = mem_amount
#         dfs(0,-1,0,0)
#         return max_ans

# # given ans : optimized dfs_find_0
# # 147ms Beats99.66%
# path = []
# def dfs_find_0(now_p, pre_p):
#     if now_p == 0: 
#         return True
#     for next_p in li[now_p] :
#         if next_p == pre_p :
#             continue
#         if dfs_find_0(next_p, now_p) :
#             path.append(next_p)
#             return True
#     return False
# dfs_find_0(bob, -1)
# path = [bob] + list(reversed(path))

# given ans 2 : 150ms Beats99.32%
def link(relation, len_n = -1):
    li = [[] for _ in range(len_n)]
    # build
    for n1,n2 in relation :
        li[n1].append(n2)
        li[n2].append(n1)
    return li
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        len_n = len(edges)+1
        li = link(edges, len_n)

        bob_time = {}
        def dfs_find_0(now_p, pre_p, step):
            if now_p == 0: 
                bob_time[now_p] = step
                return True
            for next_p in li[now_p] :
                if next_p == pre_p :
                    continue
                if dfs_find_0(next_p, now_p, step+1) :
                    bob_time[now_p] = step
                    return True
            return False
        dfs_find_0(bob, -1, 0)
        print(bob_time)

        max_ans = -inf
        def dfs(now_n, pre_n, step, now_s):
            bob_step = bob_time.get(now_n, inf)
            if step < bob_step :
                now_s += amount[now_n]
            elif step == bob_step :
                now_s += amount[now_n] // 2
            
            if len(li[now_n]) == 1 and step > 0:
                nonlocal max_ans
                if now_s > max_ans :
                    max_ans = now_s
                return 
            
            for nei_n in li[now_n] :
                if nei_n == pre_n :
                    continue
                dfs(nei_n, now_n, step+1, now_s)
        dfs(0,-1,0,0)
        return max_ans


s = Solution()
print("ans :",s.mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], 
                                   bob = 3, amount = [-2,4,2,-4,6])) # 6
print("ans :",s.mostProfitablePath(edges = [[0,1]], bob = 1, amount = [-7280,2350])) # -7280
print("ans :",s.mostProfitablePath(edges = [[0,2],[0,4],[1,3],[1,2]], 
                                   bob = 1, amount = [3958,-9854,-8334,-9388,3410])) # -7280



