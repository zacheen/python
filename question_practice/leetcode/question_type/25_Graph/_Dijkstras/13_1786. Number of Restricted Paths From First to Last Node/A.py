# 1786. Number of Restricted Paths From First to Last Node
# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node

from typing import List
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

# my 335ms Beats42.86%
# can be imporve to 275ms Beats79.72%, by replacing dict to list
MOD = 10**9+7
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        li = defaultdict(list)
        for n1,n2,w in edges :
            li[n1].append((n2,w))
            li[n2].append((n1,w))

        start = n
        min_path = defaultdict(lambda : inf)
        min_path[start] = 0
        heap = [(0, start)]
        # cnt difference is not big
        # cnt = 0
        while heap:
            now_path, now_node = heappop(heap)
            if now_path > min_path[now_node] :
                continue
            # min_path[now_node] = now_path # no needed
            # cnt += 1
            # if cnt == n:
            #     break
            for nei_node, nei_w in li[now_node] :
                if (new_path := now_path + nei_w) < min_path[nei_node] :
                    min_path[nei_node] = new_path
                    heappush(heap, (new_path, nei_node))
        
        deg = [inf] + [0]*(n)
        li = defaultdict(list)
        for n1,n2,w in edges :
            if min_path[n1] > min_path[n2] :
                deg[n2] += 1
                li[n1].append(n2)
            elif min_path[n1] < min_path[n2] :
                deg[n1] += 1
                li[n2].append(n1)

        start = 1
        end = n
        comb_cnt = [0]*(n+1)
        comb_cnt[start] = 1
        end_point = [n for n, d in enumerate(deg) if d == 0]
        while end_point:  # 拓樸排序，剪掉圖上所有樹枝
            now_n = end_point.pop()
            for nei_n in li[now_n] :
                comb_cnt[nei_n] = (comb_cnt[nei_n] + comb_cnt[now_n]) % MOD
                deg[nei_n] -= 1
                if deg[nei_n] == 0:
                    end_point.append(nei_n)
        return comb_cnt[end]
    
        # method 2 using dfs
        # @lru_cache(None)
        # def dfs(u):
        #     if u == n:
        #         return 1
        #     total = 0
        #     for v, _ in li[u]:
        #         if min_path[v] < min_path[u]:
        #             total += dfs(v)
        #     return total % MOD
        # return dfs(1)  

s = Solution()
print("ans :",s.countRestrictedPaths(n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]])) # 
# print("ans :",s.countRestrictedPaths()) # 
# print("ans :",s.countRestrictedPaths()) # 



