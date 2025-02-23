# 1857. Largest Color Value in a Directed Graph
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph

from typing import List
from math import inf

from collections import defaultdict
# my 1358ms Beats96.57%
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        len_n = len(colors)

        # build links
        li = [[] for _ in range(len_n)]
        for n1,n2 in edges :
            li[n1].append(n2)
        
        ans_cou = [defaultdict(int) for _ in range(len_n)]
        deg = [0] * len_n
        for n1,n2 in edges:
            deg[n2] += 1  # 統計基環樹每個節點的入度
        end_point = [i for i, d in enumerate(deg) if d == 0]
        while end_point:  # 拓樸排序，剪掉圖上所有樹枝
            now_n = end_point.pop()
            now_ans_c = ans_cou[now_n]
            now_ans_c[colors[now_n]] += 1
            for nei_n in li[now_n] :
                nei_ans_c = ans_cou[nei_n]
                for e_color, cou in now_ans_c.items() :
                    if cou > nei_ans_c[e_color] :
                        nei_ans_c[e_color] = cou
                deg[nei_n] -= 1
                if deg[nei_n] == 0:
                    end_point.append(nei_n)
        
        if any(d != 0 for d in deg) :
            return -1
        else :
            return max(l for each_len in ans_cou for l in each_len.values())

# given ans


s = Solution()
print("ans :",s.largestPathValue(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]])) # 3
print("ans :",s.largestPathValue(colors = "a", edges = [[0,0]])) # -1



