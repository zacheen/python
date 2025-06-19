# 2846. Minimum Edge Weight Equilibrium Queries in a Tree
# https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/description/

from typing import List
from math import inf
from collections import Counter

# my, modify template TreeAncestor : 3811ms Beats18.07%
class TreeAncestor:
    def __init__(self, edges):
        len_n = len(edges)+1
        self.max_bit_len = max_bit_len = len_n.bit_length()
        li = [[] for _ in range(len_n)]
        for x, y, w in edges:
            li[x].append((y, w))
            li[y].append((x, w))

        parent = [-1]*len_n
        depth = [0]*len_n  # 此 node 在第幾層
        dist = [None]*len_n   # 從 root 到 node 的 weight 總和
        dist[0] = Counter()
        root_num = 0
        stack = [root_num]
        while stack:
            u = stack.pop()
            for v,w in li[u]:
                if v == parent[u]: continue
                parent[v] = u
                depth[v] = depth[u]+1
                copy_cou = dist[u].copy()
                copy_cou[w] += 1
                dist[v] = copy_cou
                stack.append(v)

        self.depth = depth
        self.dist = dist
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
                # if node == -1: # 如果常常超出再開
                #     break
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
        return self.dist[x] + self.dist[y] - self.dist[lca] - self.dist[lca]
 
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        tree_ac = TreeAncestor(edges)
        ans = []
        for st, en in queries:
            cou = tree_ac.get_dist(st, en).values()
            if len(cou) == 0:
                ans.append(0)
            else:
                ans.append(sum(cou)-max(cou))
        return ans

# given ans
# since 1 <= wi <= 26, so using [0]*26 to mem and cal would be faster

s = Solution()
print("ans :",s.minOperationsQueries(n = 7, 
    edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], 
    queries = [[0,3],[3,6],[2,6],[0,6]])) # [0,0,1,3]
print("ans :",s.minOperationsQueries(n = 8, 
    edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], 
    queries = [[4,6],[0,4],[6,5],[7,4]])) # [1,2,2,3]
# print("ans :",s.minOperationsQueries()) # 
