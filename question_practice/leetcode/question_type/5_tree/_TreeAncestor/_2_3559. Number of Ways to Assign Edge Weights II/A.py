# 3559. Number of Ways to Assign Edge Weights II
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii

from typing import List
from math import inf
from functools import cache

MOD = 10**9+7

# my using template Factorial, TreeAncestor_no_weight: 1254ms Beats77.81%
# class Factorial:
#     def __init__(self, N, MOD) -> None:
#         N += 1
#         self.MOD = MOD
#         self.fact = [1]*N      # mul from 1 to i
#         self.invfact = [1]*N   
#         for i in range(1, N):
#             self.fact[i] = self.fact[i - 1] * i % self.MOD
#         self.invfact[-1] = pow(self.fact[-1], MOD - 2, MOD)
#         for i in range(N - 2, -1, -1):
#             self.invfact[i] = self.invfact[i + 1] * (i + 1) % self.MOD

#     def fac(self, n):
#         return self.fact[n]

#     def fac_inv(self, n):
#         return self.invfact[n]

#     def combi(self, n, m):
#         if m < 0 or n < m: return 0
#         return self.fact[n] * self.invfact[m] % self.MOD * self.invfact[n - m] % self.MOD

#     def permu(self, n, m):
#         if m < 0 or n < m: return 0
#         return self.fact[n] * self.invfact[n - m] % self.MOD

#     def catalan(self, n):
#         return (self.combi(2 * n, n) - self.combi(2 * n, n - 1)) % self.MOD

#     def inv(self, n):
#         return self.fact[n-1] * self.invfact[n] % self.MOD
# fac = Factorial(10**5+1, MOD)

# @cache
# def cal_all_comb(dist):
#     total_comb = 0
#     for odd_cou in range(1,dist+1,2):
#         total_comb = (fac.combi(dist, odd_cou) + total_comb) % MOD
#     return total_comb

# given ans optimize : 740ms Beats91.53%
@cache
def cal_all_comb(dist):
    if dist==0:
        return 0
    else:
        return (pow(2,dist-1,MOD))

class TreeAncestor_no_weight:
    def __init__(self, edges):
        len_n = len(edges)+1 +1 # edges indx start from 1
        self.max_bit_len = max_bit_len = len_n.bit_length()
        li = [[] for _ in range(len_n)]
        for x, y in edges:
            li[x].append(y)
            li[y].append(x)

        parent = [-1]*len_n
        depth = [0]*len_n  # 此 node 在第幾層
        root_num = 1
        stack = [root_num]
        while stack:
            u = stack.pop()
            for v in li[u]:
                if v == parent[u]: continue
                parent[v] = u
                depth[v] = depth[u]+1
                stack.append(v)

        self.depth = depth
        self.fa_list = [parent]+[[-1]*len_n for _ in range(max_bit_len)]
        # fa_list[parent_lv][node]
		# 用來記錄 [父節點, 父節點的父節點, (父節點)**4, (父節點)**8...] 是誰
            # 這樣找 kth_ancestor 就可以在 O(logn) 的時間內做到
                # 例如 k = 13 = 往上1+往上4+往上8
        now_lv = self.fa_list[0]
        for lv in range(1, max_bit_len+1):
            next_lv = self.fa_list[lv]
            for node in range(len_n):
                if (par:=now_lv[node]) == -1: continue
                next_lv[node] = now_lv[par]
            now_lv = next_lv

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for shift in range(k.bit_length()):
            if k >> shift & 1:
                node = self.fa_list[shift][node]
                if node == -1: # 如果常常超出再開
                    break
        return node

    # 返回 x和y 的最近公共祖先
    def get_lca(self, x, y):
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(self.depth[y].bit_length()-1, -1, -1):
            px, py = self.fa_list[i][x], self.fa_list[i][y]
            if px != py:
                x, y = px, py  # 同時往上找前 2**i 個父node
        return self.fa_list[0][x]

    # # 如果已經知道 x和y 在同一條路徑上，不應該呼叫此function，而是直接在程式中計算
    def get_dist(self, x: int, y: int, lca = None) -> int:
        if lca == None: lca = self.get_lca(x, y)
        return self.depth[x] + self.depth[y] - self.depth[lca]*2

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        tree_an = TreeAncestor_no_weight(edges)
        return [cal_all_comb(tree_an.get_dist(*q)) for q in queries]

s = Solution()
print("ans :",s.assignEdgeWeights(edges = [[1,2]], queries = [[1,1],[1,2]])) # [0, 1]
print("ans :",s.assignEdgeWeights(edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]])) # [2, 1, 4]



