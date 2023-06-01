# 934. Shortest Bridge
# https://leetcode.com/problems/shortest-bridge/description/

from typing import List
import functools

# my Beats 11.77%
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        direction = [-1, 0, 1, 0, -1]

        flag = 1
        # find one island
        for find_x in range(len(grid)) :
            for find_y in range(len(grid[0])) :
                if grid[find_x][find_y] == 1 :
                    bfs_stack = set()
                    # DFS to link all P
                    stack = [(find_x,find_y)]
                    while stack :
                        now_x, now_y = stack.pop()
                        if now_x < 0 or now_x >= len(grid) or now_y < 0 or now_y >= len(grid[0]) :
                            continue
                        if grid[now_x][now_y] == 0 :
                            # print(grid, now_x, now_y)
                            bfs_stack.add((now_x, now_y))
                        if grid[now_x][now_y] == 1 :
                            grid[now_x][now_y] = 2
                            for i in range(4) :
                                stack.append((now_x+direction[i], now_y+direction[i+1]))
                                
                    # print(grid)
                    # print("bfs_stack :", bfs_stack)
                    # bfs the first island to another island
                    ans = 0
                    while bfs_stack :
                        new_stack = set()
                        for b_x, b_y in bfs_stack :
                            if b_x < 0 or b_x >= len(grid) or b_y < 0 or b_y >= len(grid[0]) :
                                continue
                            if grid[b_x][b_y] == 1 :
                                return ans
                            elif grid[b_x][b_y] == 0 :
                                for i in range(4) :
                                    new_stack.add((b_x+direction[i], b_y+direction[i+1]))
                        bfs_stack = new_stack
                        ans += 1
        return -1

# given ans

s = Solution()
print(s.shortestBridge([[0,1],[1,0]])) # 1
print(s.shortestBridge([[0,1,0],[0,0,0],[0,0,1]])) # 2
print(s.shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])) # 1



