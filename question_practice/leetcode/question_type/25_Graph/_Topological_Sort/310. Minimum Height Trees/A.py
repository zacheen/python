# 310. Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/description/

from typing import List
from math import inf

# my 43ms Beats88.03%
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        li = [set() for _ in range(n)]
        for n1,n2 in edges :
            li[n1].add(n2)
            li[n2].add(n1)
        
        end_point = [i for i, nei in enumerate(li) if len(nei) <= 1]
        while end_point :
            new_end_point = []
            for now_n in end_point :
                for nei_n in li[now_n] :
                    li[nei_n].remove(now_n)
                    if len(li[nei_n]) == 1:
                        new_end_point.append(nei_n) 
            if len(new_end_point) == 0 :
                return end_point
            else :
                end_point = new_end_point

# given ans


s = Solution()
print("ans :",s.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]])) # 
print("ans :",s.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]])) # 



