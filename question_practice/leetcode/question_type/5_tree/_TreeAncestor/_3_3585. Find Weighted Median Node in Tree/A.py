# 3585. Find Weighted Median Node in Tree
# https://leetcode.com/problems/find-weighted-median-node-in-tree

from typing import List
from math import inf

# my 890ms Beats97.40%
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
        dist = [0]*len_n   # 從 root 到 node 的 weight 總和
        stack = [0]
        while stack:
            u = stack.pop()
            for v,w in li[u]:
                if v == parent[u]: continue
                parent[v] = u
                depth[v] = depth[u]+1
                dist[v]=dist[u]+w
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
        return self.dist[x] + self.dist[y] - self.dist[lca]*2
    
    def upto_dist_in(self, st, dist): # include
        dist_2_st = self.dist[st]
        for shift in range(self.depth[st].bit_length()-1,-1,-1):
            next_node = self.fa_list[shift][st]
            if next_node != -1 and (dist_2_st-self.dist[next_node]) <= dist:
                st = next_node
        return st

    def upto_dist_not_in(self, st, dist): # include
        dist_2_st = self.dist[st]
        for shift in range(self.depth[st].bit_length()-1,-1,-1):
            next_node = self.fa_list[shift][st]
            if next_node != -1 and (dist_2_st-self.dist[next_node]) < dist:
                st = next_node
        return st
    
    def over_dist(self, st, dist): # 要 over 所以當然不包含此點
        return self.fa_list[0][self.upto_dist_not_in(st, dist)]

class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # assuming tree root is 0
        tree = TreeAncestor(edges)
        ans = []
        for st_n, en_n in queries:
            lca = tree.get_lca(st_n, en_n)
            if tree.dist[st_n] == tree.dist[en_n] :
                ans.append(lca)
                continue
            mid_dist = tree.get_dist(st_n, en_n, lca) / 2
            if tree.dist[st_n] > tree.dist[en_n] :
                ans.append(tree.over_dist(st_n, mid_dist))
            else:
                ans.append(tree.upto_dist_in(en_n, mid_dist))
        return ans

s = Solution()
print("ans :",s.findMedian(n = 2, edges = [[0,1,7]], queries = [[1,0],[0,1]])) # [0,1]
print("ans :",s.findMedian(n = 3, edges = [[0,1,2],[2,0,4]], queries = [[0,1],[2,0],[1,2]])) # [1,0,2]
print("ans :",s.findMedian(n = 5, edges = [[0,1,2],[0,2,5],[1,3,1],[2,4,3]], queries = [[3,4],[1,2]])) # [2,2]
print("ans :",s.findMedian(n = 5, edges = [[0,1,15],[0,2,15],[1,3,23],[2,4,19]], 
                           queries = [[2,1],[3,4]])) # [0,0]
print("ans :",s.findMedian(n = 7, edges = [[0,1,34],[1,2,30],[2,3,8],[0,4,34],[2,5,30],[2,6,46]], 
                           queries = [[3,5],[3,6],[5,1]])) # [5,6,2]
print("ans :",s.findMedian(n = 5, edges = [[0,1,1],[1,2,11],[1,3,1],[0,4,8]], 
                           queries = [[0,3],[3,0],[0,1]])) # [1, 1, 1]



