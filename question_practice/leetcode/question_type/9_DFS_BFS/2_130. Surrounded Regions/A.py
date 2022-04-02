# (O) DFS 盡量執行確定的東西 要不然很麻煩
# 我的想法到最後才會知道要不要改符號
# 但是 given ans 一開始就知道 這個是要留下的

# my Runtime: 514 ms, faster than 5.02% of Python3
# import numpy
# class Solution:
#     def solve(self, board):
#         len_y = len(board[0])
#         pass_before = numpy.zeros( shape = (len(board), len_y) , dtype=bool) 
        
#         dirs = [0, 1, 0, -1, 0]
#         pass_p = []
#         # return True 代表有碰到邊界
#         # 這裡不能用 cache  因為有可能某條支線回傳是True 但另一條是False 
#         # @cache
#         def dfs(i,j):
#             print((i,j))
#             if pass_before[i][j] :
#                 return False
#             pass_p.append((i,j))
#             pass_before[i][j] = True
#             ret = False
#             # 這裡不能提前回去 因為我要找到連著的全部圈
#             for k in range(4) :
#                 x = i + dirs[k]
#                 y = j + dirs[k + 1]
#                 # 如果到邊界
#                 # print("比較 :",x, len(board))
#                 if x < 0 or x >= len(board) or y < 0 or y >= len_y :
#                     ret = True
#                 elif board[x][y] == "O" :
#                     if dfs(x,y) :
#                         ret = True
#             return ret
        
#         change_list = []
        
#         for x in range(1,len(board)-1) :
#             for y in range(1,len_y-1) :
#                 if not pass_before[x][y] and board[x][y] == "O" and not dfs(x,y) :
#                     # 如果沒有碰到邊界 把經過的點全部變成 "X"
#                     for e_x, e_y in pass_p :
#                         board[e_x][e_y] = "X"
#                 pass_p = []

# given ans Runtime: 218 ms, faster than 44.83% of Python3
# 跟我的想法是反方向的
# 只做周邊的點的 DFS  改成*  這些就是最後O的位置
# (代表其他的O 沒有接觸到邊邊)
class Solution:
    def solve(self, board):
        if not board:
            return

        m = len(board)
        n = len(board[0])

        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n:
                return
            if board[i][j] != 'O':
                return

            board[i][j] = '*'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if i * j == 0 or i == m - 1 or j == n - 1:
                    dfs(i, j)

        for row in board:
            for i, c in enumerate(row):
                row[i] = 'O' if c == '*' else 'X'


s = Solution()
# board = [["X","X","X","X"],["X","O","X","X"],["X","X","X","X"],["X","O","X","X"]]
# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["X","O","X","X"],
         ["O","X","O","X"],
         ["X","O","X","O"],
         ["O","X","O","X"]]
s.solve(board)
print(board)



