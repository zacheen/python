# my fail 這樣如果右下角沒有 0 的話會進無窮迴圈
# 想法是對的 但實作方式是錯的 應該要框框擴張 而不是0的範圍擴張
# class Solution:
#     def maximalSquare(self, matrix):

#         stack_0 = []
#         stack_1 = []
#         first_have_1 = False
#         for i in range(len(matrix)) :
#             for j in range(len(matrix[0])) :
#                 if matrix[i][j] == "0" :
#                     # 把左邊跟上面的 matrix 也改成0
#                     if i>=1 and matrix[i-1][j] != "0" :
#                         stack_0.append((i-1, j))
#                         # print("修改", (i-1,j))
#                         matrix[i-1][j] = "0"
#                     if j>=1 and  matrix[i][j-1] != "0" :
#                         stack_0.append((i, j-1))
#                         # print("修改", (i,j-1))
#                         matrix[i][j-1] = "0"
#                     if  i>=1 and j>=1 and matrix[i-1][j-1] != "0" :
#                         stack_0.append((i-1, j-1))
#                         # print("修改", (i-1,j-1))
#                         matrix[i-1][j-1] = "0"
#                 else :
#                     # print("有1")
#                     stack_1.append((i,j))
#                     first_have_1 = True
        
#         if first_have_1 == False :
#             return 0

#         ans_count = 1
#         # check remain 1
#         while True:
#             for indx in range(len(stack_1)-1, -1, -1) :
#                 x, y = stack_1[indx]
#                 if matrix[x][y] == "0" :
#                     del(stack_1[indx])
#             if len(stack_1) == 0 :
#                 return ans_count**2
#             else :
#                 ans_count += 1

#             new_stack_0 = []
#             for i, j in stack_0 :
#                 if i-1 >= 0 and matrix[i-1][j] != "0" :
#                     new_stack_0.append((i-1, j))
#                     matrix[i-1][j] = "0"
#                 if j-1 >= 0 and matrix[i][j-1] != "0" :
#                     new_stack_0.append((i, j-1))
#                     matrix[i][j-1] = "0"
#                 if j-1 >= 0 and i-1 >= 0 and matrix[i-1][j-1] != "0" :
#                     new_stack_0.append((i-1, j-1))
#                     matrix[i-1][j-1] = "0"
#             stack_0 = new_stack_0
#             # print(matrix)
#             # print(stack_0)
#             # import time
#             # time.sleep(1)

# my v2 算周圍的1 正方形大小是多少
# Runtime: 583 ms, faster than 73.90% of Python3
class Solution:
    def maximalSquare(self, matrix):
        mem = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        now_max = 0
        for i in range(1,len(matrix)+1) :
            for ii in range(1,len(matrix[0])+1) :
                if matrix[i-1][ii-1] == "1":
                    mem[i][ii] = min(mem[i-1][ii], mem[i][ii-1], mem[i-1][ii-1]) + 1
                    now_max = max( mem[i][ii] , now_max )
                    
        return now_max*now_max

# 我是用補邊界的方法
# given ans 是用判斷邊界的方法
# 然後 mem 只存一維
# Runtime: 554 ms, faster than 82.11% of Python3
# class Solution:
#     def maximalSquare(self, matrix):
#         m = len(matrix)
#         n = len(matrix[0])
#         dp = [0] * n
#         maxLength = 0
#         prev = 0  # dp[i - 1][j - 1]

#         for i in range(m):
#             for j in range(n):
#                 cache = dp[j]
#                 if i == 0 or j == 0 or matrix[i][j] == '0':
#                     dp[j] = 1 if matrix[i][j] == '1' else 0
#                 else:
#                     dp[j] = min([prev, dp[j], dp[j - 1]]) + 1
#                 maxLength = max(maxLength, dp[j])
#                 prev = cache

#         return maxLength * maxLength

s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],
                       ["1","0","1","1","1"],
                       ["1","1","1","1","1"],
                       ["1","0","0","1","0"]]))
# print(s.maximalSquare( matrix = [["0","1"],["1","0"]]))


