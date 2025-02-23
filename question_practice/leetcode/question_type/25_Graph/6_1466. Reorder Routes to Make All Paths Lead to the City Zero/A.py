# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero

from typing import List
from math import inf

# my 143ms Beats94.82%
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        links = [[] for _ in range(n)]
        for n1,n2 in connections :
            links[n1].append((n2, True))
            links[n2].append((n1, False))
        
        ans_cou = 0
        def dfs(n1, prev) :
            nonlocal ans_cou
            for next_n, d in links[n1] :
                if next_n == prev :
                    continue
                if d :
                    ans_cou += 1
                dfs(next_n, n1)
        dfs(0,-1)
        return ans_cou

s = Solution()
print("ans :",s.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]])) # 3 
print("ans :",s.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]])) # 2 



