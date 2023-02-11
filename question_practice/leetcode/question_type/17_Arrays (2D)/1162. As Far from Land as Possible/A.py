# my Ver1
# 1998 ms
# import copy
# class Solution(object):
#     def maxDistance(self, grid):
#         ans_count = -1

#         len_x = len(grid)
#         len_x_bound = len_x - 1
#         len_y = len(grid[0])
#         len_y_bound = len_y - 1
#         while True :
#             no_zero = True
#             prev_grid = copy.deepcopy(grid)
#             for x in range(len_x) :
#                 for y in range(len_y) :
#                     # 另外一個方法是增加一個邊界
#                     if grid[x][y] != 0 :
#                         continue
                    
#                     # left
#                     if (x > 0):
#                         if prev_grid[x-1][y] != 0 :
#                             grid[x][y] = 1
#                             no_zero = False
#                             continue
#                     # right
#                     if (x < len_y_bound):
#                         if prev_grid[x+1][y] != 0 :
#                             grid[x][y] = 1
#                             no_zero = False
#                             continue
#                     # top
#                     if (y > 0):
#                         if prev_grid[x][y-1] != 0 :
#                             grid[x][y] = 1
#                             no_zero = False
#                             continue
#                     # buttom
#                     if (y < len_y_bound):
#                         if prev_grid[x][y+1] != 0 :
#                             grid[x][y] = 1
#                             no_zero = False
#                             continue
            
#             if no_zero :
#                 return ans_count
#             else :
#                 if ans_count == -1 :
#                     ans_count = 0
#                 ans_count += 1

# # my Ver2
# # 竟然反而更慢 Runtime : 4784 ms
# import numpy as np
# class Solution(object):
#     def maxDistance(self, grid):
#         ans_count = -1

#         grid_len = len(grid)
#         np_mid = np.array(grid)
#         np_have_boundary = np.zeros( shape = (grid_len+2, grid_len+2) , dtype=int ) 
#         np_have_boundary[1:grid_len+1, 1:grid_len+1] = np_mid

#         while True :
#             no_zero = True
#             prev_grid = np_have_boundary.copy()
#             for x in range(1,grid_len+1) :
#                 for y in range(1,grid_len+1) :
#                     if prev_grid[x][y] != 0 :
#                         continue
                    
#                     if prev_grid[x-1][y] != 0 or prev_grid[x+1][y] != 0 or prev_grid[x][y-1] != 0 or prev_grid[x][y+1] != 0 :
#                         np_have_boundary[x][y] = 1
#                         no_zero = False
            
#             if no_zero :
#                 if ans_count == -1 :
#                     return -1
#                 else :
#                     return ans_count + 1
#             ans_count += 1

# my Ver3
# Runtime 3850 ms
# import copy
# class Solution(object):
#     def maxDistance(self, grid):
#         ans_count = -1
#         len_grid = len(grid)
#         final_sum = len_grid * len_grid

#         all_zero = True
#         while True :
#             no_zero = True
            
#             # sum_num = sum(grid)
#             for x in range(len(grid)) :
#                 for y in range(len(grid)) :
#                     if grid[x][y] == 0 :
#                         no_zero = False
#                     else :
#                         all_zero = False

#                     if not no_zero and not all_zero :
#                         break
#                 if not no_zero and not all_zero :
#                         break
            
#             if all_zero :
#                 return -1
#             if no_zero :
#                 # print("ans_count : ",ans_count)
#                 if ans_count == -1 :
#                     return -1
#                 else :
#                     return ans_count + 1
#             ans_count += 1

#             prev_grid = copy.deepcopy(grid)
#             for prev_i in range(len(grid)-1) :
#                 i = prev_i + 1
#                 for j in range(len(grid)) :
#                     # 看上面
#                     grid[i][j] = prev_grid[prev_i][j] + grid[i][j]
#                     # 看下面
#                     grid[prev_i][j] = prev_grid[i][j] + grid[prev_i][j]
#                     # 看上面
#                     grid[j][i] = prev_grid[j][prev_i] + grid[j][i]
#                     # 看下面
#                     grid[j][prev_i] = prev_grid[j][i] + grid[j][prev_i]
            
# given ans
# Runtime 442 ms
# 紀錄哪些點已經走過了
# 然後再從這些點去判斷上下左右 去擴張
    # 第一個想法我還是 判斷剩下的海的上下左右，但其實判斷擴張的面積快很多(每個位置只會判斷一次)
    # 而且 ver 1 我還是每次都去判斷當下點 所以慢很多
import collections
class Solution:
    def maxDistance(self, grid):
        m = len(grid)
        n = len(grid[0])
        dirs = [0, 1, 0, -1, 0]
        q = collections.deque()
        water = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    water += 1
                else:
                    q.append((i, j))

        if water == 0 or water == m * n:
            return -1

        ans = 0
        d = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                ans = d
                for k in range(4):
                    x = i + dirs[k]
                    y = j + dirs[k + 1]
                    if x < 0 or x == m or y < 0 or y == n:
                        continue
                    if grid[x][y] > 0:
                        continue
                    q.append((x, y))
                    grid[x][y] = 2  # Mark as visited.
            d += 1

        return ans

s = Solution()
print(s.maxDistance([[1,0,1],[0,0,0],[1,0,1]])) # 2
print(s.maxDistance([[1,0,0],[0,0,0],[0,0,0]])) # 4
print(s.maxDistance([[0,0,0],[0,0,0],[0,0,0]])) # -1
print(s.maxDistance([[1,1,1],[1,1,1],[1,1,1]])) # -1

