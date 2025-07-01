# 2940. Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description
from typing import List
from math import inf

# fail : since the graph is not a tree
class TreeAncestor_no_weight:
    def __init__(self, heights):
        heights.append(inf)
        len_n = len(heights)
        self.last = len_n-1
        root_num = len_n-1
        self.max_bit_len = max_bit_len = len_n.bit_length()
        li = [[] for _ in range(len_n)]

        stack = []
        for i,n in enumerate(heights) :
            while stack and stack[-1][0] < n :
                li[i].append(stack.pop()[1])
            stack.append((n,i))

        parent = [-1]*len_n
        depth = [0]*len_n  # 此 node 在第幾層
        
        stack = [root_num]
        while stack:
            u = stack.pop()
            for v in li[u]:
                # if v == parent[u]: continue
                parent[v] = u
                depth[v] = depth[u]+1
                stack.append(v)

        self.depth = depth
        self.bin_lift = [parent]+[[-1]*len_n for _ in range(max_bit_len)]
        now_lv = self.bin_lift[0]
        for lv in range(1, max_bit_len+1):
            next_lv = self.bin_lift[lv]
            for node in range(len_n):
                if (par:=now_lv[node]) == -1: continue
                next_lv[node] = now_lv[par]
            now_lv = next_lv
        _ = ""

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for shift in range(k.bit_length()):
            if k >> shift & 1:
                node = self.bin_lift[shift][node]
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
            px, py = self.bin_lift[i][x], self.bin_lift[i][y]
            if px != py:
                x, y = px, py  # 同時往上找前 2**i 個父node
        if (ret := self.bin_lift[0][x]) != self.last :
            return ret
        return -1

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        treeAn = TreeAncestor_no_weight(heights)
        ans = []
        for q1, q2 in queries :
            if q1 == q2 :
                ans.append(q1)
                continue
            ans.append(treeAn.get_lca(q1, q2))
        return ans

s = Solution()
print("ans :",s.leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]])) # [2,5,-1,5,2] 
print("ans :",s.leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]])) # [7,6,-1,4,6]
# print("ans :",s.leftmostBuildingQueries(heights = [3,4,1,2], queries = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]])) 
# print("ans :",s.leftmostBuildingQueries(heights = [3,4,1,2], queries = [[0,2]])) 



