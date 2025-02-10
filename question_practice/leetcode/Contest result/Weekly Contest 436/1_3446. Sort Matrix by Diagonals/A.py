# 3446. Sort Matrix by Diagonals
# https://leetcode.com/problems/sort-matrix-by-diagonals/description/

from typing import List
from math import inf

# my 
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mem = []
        n_len = len(grid)
        for n2 in range(n_len-1,-1,-1) :
            n1 = 0
            this_mem = []
            while n2 < n_len :
                this_mem.append(grid[n2][n1])
                n1 += 1
                n2 += 1
            this_mem.sort()
            mem.append(this_mem)

        for n1 in range(1, n_len) :
            n2 = 0
            this_mem = []
            while n1 < n_len :
                this_mem.append(grid[n2][n1])
                n1 += 1
                n2 += 1
            this_mem.sort(reverse = True)
            mem.append(this_mem)
        
        ans = []
        for _ in range(n_len) :
            ans.append([l.pop() for l in mem[-n_len:]])
            mem.pop()
        return ans

# given ans


s = Solution()
print("ans :",s.sortMatrix(grid = [[1,7,3],[9,8,2],[4,5,6]])) # [[8,2,3],[9,6,7],[4,5,1]]



