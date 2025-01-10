# 3203. Find Minimum Diameter After Merging Two Trees
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description

from typing import List
import functools

# my 441ms Beats74.48%
from math import ceil
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # 找哪個點 接出去最短 > 先知的條件 : 最長的路徑//2(中間的點) 就是 diameter 
        def find_longest(edges):
            if len(edges) == 0 : return 0
            links = [ [] for _ in range(len(edges)+1) ]
            for p1, p2 in edges :
                links[p1].append(p2)
                links[p2].append(p1)
            
            # DFS find longest path
            max_dia = 0
            def DFS(now_p, prev_p):
                nonlocal max_dia
                max_depth = 0
                sec_depth = 0
                for next_p in links[now_p] :
                    if next_p == prev_p :
                        continue
                    ret = DFS(next_p, now_p)
                    # print("ret :",next_p, now_p, ret)
                    if ret > sec_depth :
                        if ret > max_depth :
                            max_depth, sec_depth = ret, max_depth
                        else :
                            sec_depth = ret
                max_dia = max(max_dia, max_depth + sec_depth)
                return max_depth + 1
            DFS(0,-1)
            # print("max_dia :", max_dia)
            return max_dia
        
        # !! the diameter in the tree is longer than one tree to another
        l1 = find_longest(edges1)
        l2 = find_longest(edges2)
        print( ceil(l1/2)+ceil(l2/2)+1, l1, l2)
        return max(ceil(l1/2)+ceil(l2/2)+1, l1, l2)

# given ans
# Topological Sorting
# BFS

s = Solution()
print("ans :",s.minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]])) # 3
print("ans :",s.minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]])) # 5
print("ans :",s.minimumDiameterAfterMerge(edges1 = [[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]], edges2 = [[0,1],[0,2],[0,3]])) # 7 ?? 6



