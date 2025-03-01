# 1591. Strange Printer II
# https://leetcode.com/problems/strange-printer-ii/description/

from typing import List
from math import inf
from collections import defaultdict
# my 59ms Beats73.00%
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        bound = {}
        for i1,l in enumerate(targetGrid) :
            for i2,n in enumerate(l) :
                if n in bound :
                    b = bound[n]
                    bound[n] = [min(b[0], i1), max(b[1], i1), min(b[2], i2), max(b[3], i2)]
                else :
                    bound[n] = [i1, i1, i2, i2]
        def is_overlap(region1, region2):
            p0 = max(region1[0], region2[0])
            p1 = min(region1[1],region2[1])
            if p0 <= p1 :
                p2 = max(region1[2], region2[2])
                p3 = min(region1[3],region2[3])
                if p2 <= p3 :
                    return [p0,p1,p2,p3]
            return None
        def check_val_in(region, val):
            for i1 in range(region[0], region[1]+1) :
                if val in targetGrid[i1][region[2]: region[3]+1] :
                    return True
            return False
        
        li = defaultdict(list)
        deg = defaultdict(int)
        poss_n = list(bound.keys())
        for limit, sha1_i in enumerate(poss_n):
            sha1 = bound[sha1_i]
            for sha2_i in poss_n[:limit]:
                overlap_re = is_overlap(sha1, bound[sha2_i])
                if overlap_re != None :
                    n1_in = check_val_in(overlap_re, sha1_i)
                    n2_in = check_val_in(overlap_re, sha2_i)
                    if n1_in and n2_in :
                        return False
                    elif n1_in :
                        li[sha2_i].append(sha1_i)
                        deg[sha1_i] += 1
                        deg[sha2_i]
                    elif n2_in :
                        li[sha1_i].append(sha2_i)
                        deg[sha2_i] += 1
                        deg[sha1_i]
        
        end_point = [i for i, d in deg.items() if d == 0]
        while end_point:  # 拓樸排序，剪掉圖上所有樹枝
            now_n = end_point.pop()
            for nei_n in li[now_n] :
                deg[nei_n] -= 1
                if deg[nei_n] == 0:
                    end_point.append(nei_n)

        return all(d == 0 for d in deg.values())

s = Solution()
print("ans :",s.isPrintable([[1,1,1,1],
                             [1,2,2,1],
                             [1,2,2,1],
                             [1,1,1,1]])) # T
print("ans :",s.isPrintable([[1,1,1,1],
                             [1,1,3,3],
                             [1,1,3,4],
                             [5,5,1,4]])) # T
print("ans :",s.isPrintable([[1,2,1],
                             [2,1,2],
                             [1,2,1]])) # F
print("ans :",s.isPrintable([[1,1,1],
                              [3,1,3]])) # F
print("ans :",s.isPrintable([[1,4,1,1,1],
                             [2,4,2,5,2],
                             [2,4,2,5,2],
                             [2,4,2,5,2],
                             [1,1,6,6,6],
                             [1,1,6,6,6]])) # T



