import time
# my Runtime: 452 ms, faster than 45.83% of Python3
# 如果要優化應該是弄3個mem 然後用hash查找有沒有用過
class Solution:
    def solveSudoku(self, board):
        def check_can_place(i,j,num) :
            return check19(i,j,num) and check91(i,j,num) and check33(i,j,num)
        
        def check19(i,j,num):
            for idx in range(9):
                if board[idx][j] == num :
                    return False
            return True
            
        def check91(i,j,num):
            # for idx in range(9):
            #     if board[i][idx] == num :
            #         return False
            # return True
            return not num in board[i]
        
        def check33(i,j,num):
            start_x = (i//3)*3
            start_y = (j//3)*3
            for x in range(start_x, start_x+3):
                for y in range(start_y, start_y+3):
                    # print(x,y)
                    if board[x][y] == num :
                        return False
            return True
        
        def rec(i,j):
            # print(i,j)
            # time.sleep(0.1)
            if i == 9 :
                j += 1
                i = 0
            if j == 9 :
                print("success")
                return True
            
            if board[i][j] == "." :
                for this_num in range(1,10) :
                    # print(i,j,this_num)
                    if check_can_place(i,j,str(this_num)) :
                        board[i][j] = str(this_num)
                        # print(board)
                        if rec(i+1,j) :
                            return True
                        board[i][j] = "."
            else :
                if rec(i+1,j) :
                    return True
        rec(0,0)
        return 
        # print(check19(6,0,"9"))
        # print(check91(6,0,"9"))
        # print(check33(6,0,"9"))
        # print("test",check_can_place(6,0,"9"))


# given ans 解法一樣 
# 只是做了某些優化
# 像是把 check19 跟 check91 合併  這樣只要for一次

s = Solution()
# board = [
#     ["5","3","4","6","7","8",".",".","."],
#     ["6","7","2","1","9","5",".",".","."],
#     [".","9","8","3","4","2",".","6","."],
#     ["8","5","9","7","6","1",".",".","3"],
#     ["4","2","6","8","5","3",".",".","1"],
#     ["7","1","3","9","2","4",".",".","6"],
#     ["9","6","1","5","3","7","2","8","."],
#     ["2","8","7","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]]
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
# print(s.solveSudoku(board))
s.solveSudoku(board)
for i in range(9):
    print(board[i])



