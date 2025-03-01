# 2392. Build a Matrix With Conditions
# https://leetcode.com/problems/build-a-matrix-with-conditions/description/

from typing import List
from math import inf

# my 11ms Beats93.39%
def cut_all_branch(links, len_n):
    len_n += 1
    deg = [0] * len_n
    li = [[] for _ in range(len_n)]
    for n1,n2 in links:
        deg[n2] += 1  # 統計基環樹每個節點的入度
        li[n1].append(n2)
    end_point = [i for i, d in enumerate(deg) if d == 0]
    ret_ord = []
    while end_point:  # 拓樸排序，剪掉圖上所有樹枝
        now_n = end_point.pop()
        if now_n == 0 :
            continue
        ret_ord.append(now_n)
        for nei_n in li[now_n] :
            deg[nei_n] -= 1
            if deg[nei_n] == 0:
                end_point.append(nei_n)
    return ret_ord

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = cut_all_branch(rowConditions, k)
        if len(row_order) < k :
            return []
        col_order = cut_all_branch(colConditions, k)
        if len(col_order) < k :
            return []
        
        print(row_order, col_order)
        row_n_to_i = { n:i for i,n in enumerate(row_order) }
        ans = [[0]*k for _ in range(k)]
        for i,n in enumerate(col_order) :
            ans[row_n_to_i[n]][i] = n
        return ans


# given ans


s = Solution()
print("ans :",s.buildMatrix(k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]])) 
print("ans :",s.buildMatrix(k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]])) 



