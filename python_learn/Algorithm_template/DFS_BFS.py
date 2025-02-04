# DFS
# <template> ####################
# n1_len = len(grid)
# n2_len = len(grid[0])
# dir_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# def dfs(n1, n2):
#     grid[n1][n2] = STATE
#     for d1,d2 in dir_list: 
#         nei1, nei2 = n1 + d1, n2 + d2
#         if 0 <= nei1 < n1_len and 0 <= nei2 < n2_len and grid[nei1][nei2] != STATE: 
#             ?? = dfs(nei1, nei2) 
#     return s
# <template> ####################

# classic
# 2658. Maximum Number of Fish in a Grid
# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description
class Solution:
    def findMaxFish(self, grid):
        n1_len = len(grid)
        n2_len = len(grid[0])
        dir_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(n1, n2):
            s = grid[n1][n2] 
            grid[n1][n2] = 0
            for d1,d2 in dir_list: 
                nei1, nei2 = n1 + d1, n2 + d2
                if 0 <= nei1 < n1_len and 0 <= nei2 < n2_len and grid[nei1][nei2] != 0: 
                    s += dfs(nei1, nei2) 
            return s

        return max([dfs(i1, i2) for i1 in range(n1_len) for i2 in range(n2_len) if grid[i1][i2] != 0] + [0])

s = Solution()
print("ans :",s.findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]])) # 7
print("ans :",s.findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])) # 1
print("ans :",s.findMaxFish([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])) # 0


# BFS 
# from collections import deque
# class Solution:
#     def numIslands(self, grid):
#         m = len(grid)
#         n = len(grid[0])

#         # 神奇的上左下右方向演算法 (O)
#         dirs = [0, 1, 0, -1, 0]
#         def bfs(r, c):
#             # 初始化 stack
#             q = deque([(r, c)])
#             grid[r][c] = '2'  # mark '2' as visited

#             # 開始把 stack 裡面的東西取出處理  直到沒有東西
#             while q:
#                 i, j = q.popleft()
#                 for k in range(4):
#                     # 神奇的上左下右方向演算法 (O)
#                     x = i + dirs[k]
#                     y = j + dirs[k + 1]
#                     if x < 0 or x == m or y < 0 or y == n:
#                         continue
#                     if grid[x][y] != '1':
#                         continue
#                     # 有此點且還沒走過 就要加入 stack
#                     q.append((x, y))
#                     grid[x][y] = '2'  # mark '2' as visited

#         ans = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     bfs(i, j)
#                     ans += 1
#         return ans