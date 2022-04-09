# my v1 Runtime: 200 ms, faster than 17.00% of Python3
# class Solution:
#     def solveNQueens(self, n):
        
#         plate = []
#         for i in range(n) :
#             plate.append(["."]*n)
            
#         def check_valid(i, j):
#             # print(i, j)
#             for ind in range(n) :
#                 if plate[i][ind] == "Q" or plate[ind][j] == "Q" :
#                     return False

#             for dir_x , dir_y in [(1,1),(-1,1),(1,-1),(-1,-1)] :
#                 x = i
#                 y = j
#                 while x < n and y < n and x >= 0 and y >= 0 :
#                     if plate[x][y] == "Q" :
#                         return False
#                     x += dir_x
#                     y += dir_y
#             return True

#         ans = []
#         def rec(now_line):
#             if now_line == n :
#                 pass_in = []
#                 for each_line in plate :
#                     pass_in.append("".join(each_line))
#                 ans.append(pass_in)
#                 return 

#             for i in range(n) :
#                 if check_valid(now_line, i) :
#                     plate[now_line][i] = "Q"
#                     rec(now_line+1)
#                     plate[now_line][i] = "."

#         rec(0)
#         return ans

# my v2 Runtime: 92 ms, faster than 57.10% of Python3
# 用 mem 紀錄那些點不能放
class Solution:
    def solveNQueens(self, n):
        
        plate = []
        mem = []
        for i in range(n) :
            plate.append(["."]*n)
            mem.append([True]*n)

        def change(i, j):
            change = []
            for ind in range(n) :
                if mem[i][ind]:
                    change.append((i,ind))
                    mem[i][ind] = False
                if mem[ind][j]:
                    change.append((ind,j))
                    mem[ind][j] = False

            for dir_x , dir_y in [(1,1),(-1,1),(1,-1),(-1,-1)] :
                x = i
                y = j
                while x < n and y < n and x >= 0 and y >= 0 :
                    if mem[x][y]:
                        change.append((x,y))
                        mem[x][y] = False
                    x += dir_x
                    y += dir_y
            return change

        ans = []
        def rec(now_line):
            if now_line == n :
                pass_in = []
                for each_line in plate :
                    pass_in.append("".join(each_line))
                ans.append(pass_in)
                return 

            for i in range(n) :
                if mem[now_line][i] :
                    plate[now_line][i] = "Q"
                    change_list = change(now_line, i)
                    rec(now_line+1)
                    for p1, p2 in change_list :
                        mem[p1][p2] = True
                    plate[now_line][i] = "."

        rec(0)
        return ans

# given ans
# 又再把 memery 優化
# 太猛了 對角線有沒有queen是用算的
# class Solution:
#     def solveNQueens(self, n):
#         ans = []
#         cols = [False] * n
#         diag1 = [False] * (2 * n - 1)
#         diag2 = [False] * (2 * n - 1)

#         def dfs(i, board):
#             if i == n:
#                 ans.append(board)
#                 return

#             for j in range(n):
#                 if cols[j] or diag1[i + j] or diag2[j - i + n - 1]:
#                     continue
#                 cols[j] = diag1[i + j] = diag2[j - i + n - 1] = True
#                 dfs(i + 1, board + ['.' * j + 'Q' + '.' * (n - j - 1)])
#                 cols[j] = diag1[i + j] = diag2[j - i + n - 1] = False

#         dfs(0, [])
#         return ans

s = Solution()
print(s.solveNQueens(5))



