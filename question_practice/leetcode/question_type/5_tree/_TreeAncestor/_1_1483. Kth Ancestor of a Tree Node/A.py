# 1483. Kth Ancestor of a Tree Node
# https://leetcode.com/problems/kth-ancestor-of-a-tree-node

from typing import List
from math import inf

# my using template : 217ms Beats96.00%
class TreeAncestor:
    def __init__(self, n: int, parent_rela: List[int]):
        len_n = len(parent_rela)
        self.max_bit_len = max_bit_len = len_n.bit_length()
        li = [[] for _ in range(len_n)]
        for x, y in enumerate(parent_rela) :
            if y == -1 : continue
            li[x].append(y)
            li[y].append(x)

        depth = [0]*len_n  # 此 node 在第幾層
        stack = [0]
        while stack:
            u = stack.pop()
            for v in li[u]:
                if v == parent_rela[u]: continue
                depth[v] = depth[u]+1
                stack.append(v)

        self.depth = depth
        self.fa_list = [parent_rela]+[[-1]*len_n for _ in range(max_bit_len)]

        now_lv = self.fa_list[0]
        for lv in range(1, max_bit_len+1):
            next_lv = self.fa_list[lv]
            for node in range(len_n):
                if (par:=now_lv[node]) == -1: continue
                next_lv[node] = now_lv[par]
            now_lv = next_lv

    def getKthAncestor(self, node: int, k: int) -> int:
        for shift in range(k.bit_length()):
            if k >> shift & 1:
                node = self.fa_list[shift][node]
                if node == -1: # 如果常常超出再開
                    break
        return node