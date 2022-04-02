# my (DFS)
# Runtime: 336 ms, faster than 80.10% of Python3 
# 思考 : (O)
# 因為我是判斷變動的那個界線而已( +1:len() -1:0 ) 所以執行速度會快一點點
# 但程式碼比較複雜
# class Solution:
#     def numIslands(self, grid):
        
#         y_len = len(grid[0])
#         def change_to_water(x,y):
#             grid[x][y] = "0"
#             if (x+1)<len(grid) and grid[x+1][y] == "1":
#                 change_to_water(x+1,y)
#             if (y+1) < y_len and grid[x][y+1] == "1":
#                 change_to_water(x,y+1)
#             if (x-1) >= 0 and grid[x-1][y] == "1":
#                 change_to_water(x-1,y)
#             if (y-1) >= 0 and grid[x][y-1] == "1":
#                 change_to_water(x,y-1)
          
#         ans = 0
#         for x in range(len(grid)) :
#             for y in range(y_len) :
#                 # print(x,y)
#                 if grid[x][y] == "1" :
#                     ans += 1
#                     change_to_water(x,y)
#         return ans

# given ans (DFS)
# Runtime: 419 ms, faster than 52.20% of Python3
# class Solution:
#     def numIslands(self, grid):
#         m = len(grid)
#         n = len(grid[0])

#         def dfs(i: int, j: int):
#             # 他是丟給下一個 dfs 再判斷這一點是否存在
#             # 這種寫法比較簡單整齊
#             if i < 0 or i == m or j < 0 or j == n:
#                 return
#             if grid[i][j] != '1':
#                 return

#             grid[i][j] = '2'  # mark '2' as visited
#             dfs(i + 1, j)
#             dfs(i - 1, j)
#             dfs(i, j + 1)
#             dfs(i, j - 1)

#         ans = 0

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     dfs(i, j)
#                     ans += 1

#         return ans

# given ans (BFS)
from collections import deque
class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])

        # 神奇的上左下右方向演算法 (O)
        dirs = [0, 1, 0, -1, 0]
        def bfs(r, c):
            # 初始化 stack
            q = deque([(r, c)])
            grid[r][c] = '2'  # mark '2' as visited

            # 開始把 stack 裡面的東西取出處理  直到沒有東西
            while q:
                i, j = q.popleft()
                for k in range(4):
                    # 神奇的上左下右方向演算法 (O)
                    x = i + dirs[k]
                    y = j + dirs[k + 1]
                    if x < 0 or x == m or y < 0 or y == n:
                        continue
                    if grid[x][y] != '1':
                        continue
                    # 有此點且還沒走過 就要加入 stack
                    q.append((x, y))
                    grid[x][y] = '2'  # mark '2' as visited

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    ans += 1
        return ans

s = Solution()
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))



