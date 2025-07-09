# 3600. Maximize Spanning Tree Stability with Upgrades
# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/description/

from typing import List
from math import inf

class UF_for_cycle:
    def __init__(self, n):
        self.count = n              # <計算目前總共分成幾個 set> 多的
        self.id = list(range(n))

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        self.id[u] = v
        self.count -= 1             # <計算目前總共分成幾個 set> 多的
        return True

    def find(self, up):
        while (up:=self.id[up]) != (deep:=self.id[up]):
            self.id[up] = self.id[deep]
        return up

# my modify template check_no_cycle : 135ms Beats99.55%
    # O(nlogn)
    # 但其實我沒有辦法證明，這樣做可以找出最大的承重(靠直覺)
        # given ans : Kruskal algorithm 最大生成樹 已經證明過了
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        uf = UF_for_cycle(n)
        min_s = inf
        remain = []
        for n1,n2, s, must in edges :
            if must :
                if not uf.union(n1, n2) :
                    return -1
                if s < min_s :
                    min_s = s
            else :
                remain.append( (n1,n2,s) )
        if uf.count == 1 :
            return min_s
        
        remain.sort(reverse = True, key = lambda x : x[2])
        for n1,n2, s in remain :
            if uf.union(n1, n2) :
                if uf.count <= k :
                    min_s = min(min_s, s*2)
                else :
                    min_s = min(min_s, s)
                if uf.count == 1 :
                    return min_s
        if uf.count == 1 :
            return min_s
        else :
            return -1
        
# inspire by given ans (binary search) : 1059ms Beats48.97%
    # O(nlog(10**5)*2) # (10**5)*2 is bigger than n > thus slower
    # dont have to do sort (might be faster)
from copy import deepcopy
from bisect import bisect_left
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        uf = UF_for_cycle(n)
        min_s = (10**5)*2
        remain = []
        for n1,n2, s, must in edges :
            if must :
                if not uf.union(n1, n2) :
                    return -1
                if s < min_s :
                    min_s = s
            else :
                remain.append( (n1,n2,s) )
        if uf.count == 1 :
            return min_s
        
        # make sure at least there is a solution
        new_uf = deepcopy(uf)
        for n1,n2, s in remain :
            new_uf.union(n1, n2)
        if new_uf.count != 1 :
            return -1

        def mid_too_small(mid):
            new_uf = deepcopy(uf)
            for n1,n2, s in remain :
                if s >= mid :
                    new_uf.union(n1, n2)
            if new_uf.count == 1 :
                return True
            
            if k > 0 :
                cou_k = k
                for n1,n2, s in remain :
                    if s < mid and s*2 >= mid :
                        if new_uf.union(n1, n2) :
                            cou_k -= 1
                            if cou_k == 0 :
                                break
            if new_uf.count == 1 :
                return True
            return False
        return bisect_left(range(min_s+1), True, key= lambda x : not mid_too_small(x))-1


s = Solution()
print("ans :",s.maxStability(n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1)) # 2
print("ans :",s.maxStability(n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2)) # 6
print("ans :",s.maxStability(n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0)) # -1



