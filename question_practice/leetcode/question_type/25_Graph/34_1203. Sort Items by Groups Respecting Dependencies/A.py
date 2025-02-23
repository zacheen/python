# 1203. Sort Items by Groups Respecting Dependencies
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies

from typing import List
from math import inf

from collections import defaultdict

# my 95ms Beats55.90%
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def gro_num(item):
            return 'O'+str(item) if (t := group[item]) == -1 else t
        
        len_n = n
        group_mem = defaultdict(set)
        for n1 in range(len_n): 
            group_mem[gro_num(n1)].add(n1)
        
        li = [[] for _ in range(len_n)]
        deg = [0]*len_n
        deg_grop = defaultdict(int)
        for i in range(m) :
            deg_grop[i] = 0
        for n1, bef_l in enumerate(beforeItems):
            if len(bef_l) == 0 and group[n1] == -1 :
                deg_grop[gro_num(n1)] = 0
            for n2 in bef_l :
                li[n2].append(n1)
                deg[n1] += 1
                n1_gn = gro_num(n1)
                if n2 not in group_mem[n1_gn] :
                    deg_grop[n1_gn] += 1

        ans = []
        end_group = [i for i, d in deg_grop.items() if d == 0]
        while end_group: 
            now_g = group_mem[end_group.pop()]
            # make sure each group has no cycle
            end_p = [gro_n for gro_n in now_g if deg[gro_n] == 0]
            while end_p :
                now_p = end_p.pop()
                ans.append(now_p)
                for nei_n in li[now_p] :
                    # managing single node degree
                    deg[nei_n] -= 1
                    if deg[nei_n] == 0 and nei_n in now_g:
                        end_p.append(nei_n)
                    # managing group degree
                    gn = gro_num(nei_n)
                    if now_p not in group_mem[gn] :
                        deg_grop[gn] -= 1
                        if deg_grop[gn] == 0:
                            end_group.append(gn)
        return ans if len(ans) == len_n else []


s = Solution()
print("ans :",s.sortItems(n = 8, m = 2, 
    group = [-1,-1,1,0,0,1,0,-1], 
    beforeItems = [[],[6],[5],[6],[3,6],[],[],[]])) # [6,3,4,1,5,2,0,7]
print("ans :",s.sortItems(n = 8, m = 2, 
    group = [-1,-1,1,0,0,1,0,-1], 
    beforeItems = [[],[6],[5],[6],[3],[],[4],[]])) # []
# print("ans :",s.sortItems()) # 



