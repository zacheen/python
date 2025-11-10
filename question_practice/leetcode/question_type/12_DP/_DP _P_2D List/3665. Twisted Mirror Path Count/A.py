# 3665. Twisted Mirror Path Count
# https://leetcode.com/problems/twisted-mirror-path-count/description/

from typing import List
from math import inf

# my 455ms Beats98.73%
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m_p1 = len(grid[0])+1
        mem = [0]*m_p1 # from top
        mem[0] = 1
        for each_row in grid :
            new_mem = [0]*m_p1
            for i, n in enumerate(each_row) :
                if n == 0 : 
                    new_mem[i] += mem[i]        # receive from top
                    new_mem[i+1] += new_mem[i]  # direct give it to the right
                else : # n == 1
                    new_mem[i+1] += mem[i]      # direct give "receive from top" to the right
            mem = new_mem
            # print(mem)
        return mem[-1] % (10**9+7)

s = Solution()
print("ans :",s.uniquePaths([[0,1,0],
                             [0,0,1],
                             [1,0,0]])) # 5
print("ans :",s.uniquePaths([[0,0],
                             [0,0]])) # 2



