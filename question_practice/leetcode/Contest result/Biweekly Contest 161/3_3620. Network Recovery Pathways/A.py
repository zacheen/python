# 3620. Network Recovery Pathways
# https://leetcode.com/problems/network-recovery-pathways/description/
    
from typing import List
from math import inf
from bisect import bisect_left

# many solutions are actually fault, so Beats% is not reliable
# my 3379ms
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        def check(min_w) :
            len_n = len(online)
            deg = [0] * len_n
            li = [[] for _ in range(len_n)]
            for n1,n2,cost in edges:
                if cost < min_w :
                    continue
                if not online[n1] or not online[n2] :
                    continue
                deg[n2] += 1  # 統計基環樹每個節點的入度
                li[n1].append((n2,cost))
            
            # 剪枝(因為從 leaf 出發的點 都不可能是 0~n-1 中間的點)
            end_point = [i for i, d in enumerate(deg[1:], 1) if d == 0]
            while end_point:  # 拓樸排序，剪掉圖上所有樹枝
                now_n = end_point.pop()
                for nei_n, cost in li[now_n] :
                    deg[nei_n] -= 1
                    if deg[nei_n] == 0:
                        end_point.append(nei_n)

            # 真正的計算 有沒有可行的路徑
            end_point = [0]
            min_sum = [inf]*len_n
            min_sum[0] = 0
            while end_point :
                now_n = end_point.pop()
                past_cost = min_sum[now_n]
                for nei_n, cost in li[now_n] :
                    deg[nei_n] -= 1
                    if deg[nei_n] == 0:
                        end_point.append(nei_n)

                    new_cost = past_cost + cost
                    if min_sum[nei_n] > new_cost :
                        min_sum[nei_n] = new_cost 
            return min_sum[-1] <= k

        max_c = max((cost for n1,n2,cost in edges), default = -1)
        if max_c == -1 :
            return -1
        return bisect_left(range(max_c+1), True, key= lambda x : not check(x))-1

# inspire by given ans : using dfs to go through all points : 2066ms
from functools import cache
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        len_n = len(online)
        li = [[] for _ in range(len_n)]
        for n1,n2,cost in edges:
            if not online[n1] or not online[n2] :
                continue
            li[n1].append((n2,cost))
        
        end_n = len_n-1
        def check(min_w) :
            @cache
            def dfs(now_n) :
                if now_n == end_n :
                    return 0
                
                ret = inf
                for nei_n, cost in li[now_n] :
                    if cost < min_w :
                        continue
                    if (new_c := cost + dfs(nei_n)) < ret :
                        ret = new_c
                return ret
        
            return dfs(0) <= k


        max_c = max((cost for n1,n2,cost in edges), default = -1)
        if max_c == -1 :
            return -1
        return bisect_left(range(max_c+1), True, key= lambda x : not check(x))-1

s = Solution()
print("ans :",s.findMaxPathScore(edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [True,True,True,True], k = 10)) # 3
print("ans :",s.findMaxPathScore(edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [True,True,True,False,True], k = 12)) # 4
print("ans :",s.findMaxPathScore(edges = [[2,3,22],[0,2,4],[1,2,42]], 
                                 online = [True,True,True,True], k = 36)) # 6

