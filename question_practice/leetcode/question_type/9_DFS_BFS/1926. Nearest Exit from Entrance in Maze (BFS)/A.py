# 1926. Nearest Exit from Entrance in Maze
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze

from typing import List
from math import inf

# my 53ms Beats83.79%
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n1_limit = len(maze)-1
        n2_limit = len(maze[0])-1
        dir_list = [(0,1),(0,-1),(1,0),(-1,0)]
        q = [entrance]
        ans_cou = 0
        while q :
            new_q = []
            for n1,n2 in q :
                if maze[n1][n2] == "+" :
                    continue
                if ans_cou != 0 and (n1 == 0 or n1 == n1_limit or n2 == 0 or n2 == n2_limit) :
                    return ans_cou
                maze[n1][n2] = "+"
                for d1,d2 in dir_list :
                    nei1 = n1+d1
                    nei2 = n2+d2
                    if ans_cou == 0 :
                        if 0 <= nei1 <= n1_limit and 0 <= nei2 <= n2_limit :
                            new_q.append((nei1, nei2))
                    else :
                        new_q.append((nei1, nei2))
            q = new_q
            ans_cou += 1
        return -1

s = Solution()
print("ans :",s.nearestExit([
    ["+","+",".","+"],
    [".",".",".","+"],
    ["+","+","+","."]], [1,2])) # 1
print("ans :",s.nearestExit([
    ["+","+","+"],
    [".",".","."],
    ["+","+","+"]], [1,0])) # 2



