# # my 
# class Solution(object):
#     def gameOfLife(self, board):
#         # count_neighbors_array = np.zeros( shape = (len(board), len(board[0])) , dtype=int )
#         count_neighbors_array = [0]*len(board[0])
#         count_neighbors_array = [count_neighbors_array.copy()]*len(board)
#         for x in range(len(board)) :
#             for y in range(len(board[0])) :
#                 count_neighbors = 0
#                 for dir_x in range(-1,2):
#                     for dir_y in range(-1,2):
#                         if dir_x == 0 and dir_y == 0 :
#                             continue
#                         nei_x = x+dir_x
#                         nei_y = y+dir_y
#                         # print(nei_x, nei_y)
#                         if nei_x < 0 or nei_y < 0 or nei_x >= len(board) or nei_y >= len(board[0]) :
#                             continue
#                         # print(nei_x, nei_y)
#                         if board[nei_x][nei_y] == 1:
#                             count_neighbors += 1
#                 count_neighbors_array[x][y] = count_neighbors    
#         for x in range(len(board)) :
#             for y in range(len(board[0])) :
#                 if board[x][y] == 1 :
#                     if count_neighbors_array[x][y] < 2 or count_neighbors_array[x][y] > 3:
#                         board[x][y] = 0
#                     else :
#                         board[x][y] = 1
#                 else :
#                     if count_neighbors_array[x][y] == 3 :
#                         board[x][y] = 1
#                     else :
#                         board[x][y] = 0

# # my 優化
# # Beats 47.99%
# # 比賽的時候盡量不要使用 np (超慢的)
# import numpy as np
# class Solution(object):
#     def gameOfLife(self, board):
#         len_x = len(board)
#         len_y = len(board[0])
#         # count_neighbors_array = np.zeros( shape = (len_x, len_y) , dtype=int )
#         count_neighbors_array = [[0]*len_y for _ in range(len_x)]
#         for x in range(len_x) :
#             for y in range(len_y) :
#                 count_neighbors = 0
#                 for nei_x in range(max(x-1,0),min(x+2,len_x)):
#                     for nei_y in range(max(y-1,0),min(y+2,len_y)):
#                         if board[nei_x][nei_y] == 1:
#                             count_neighbors += 1
#                 count_neighbors_array[x][y] = count_neighbors  
#         print(count_neighbors_array)  
#         for x in range(len_x) :
#             for y in range(len_y) :
#                 if board[x][y] == 1 :
#                     if count_neighbors_array[x][y] in [3,4]:
#                         board[x][y] = 1
#                     else :
#                         board[x][y] = 0
#                 else :
#                     if count_neighbors_array[x][y] == 3 :
#                         board[x][y] = 1
#                     else :
#                         board[x][y] = 0

# given ans
# 跟我的想法架構一樣，但優化了很多地方 
    # 1. 只是用 bit 運算 所以不用多空間
    # 2. 不用排除自己數字的計算 (直接加到後面改變排除的條件)
    # 3. 
# Beats 95.85%
class Solution(object):
    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                ones = 0
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        ones += board[x][y] & 1
                # Any live cell with 2 or 3 live neighbors
                # lives on to the next generation
                if board[i][j] == 1 and (ones == 3 or ones == 4):
                    board[i][j] |= 0b10
                # Any dead cell with exactly 3 live neighbors
                # becomes a live cell, as if by reproduction
                if board[i][j] == 0 and ones == 3:
                    board[i][j] |= 0b10

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

s = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(board)
print("ans :",board)
board = [[1,1],[1,0]]
s.gameOfLife(board)
print("ans :",board)



