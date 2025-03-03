# my Runtime: 49 ms, faster than 74.08% of Python3
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # 代表 (i,j) 這個位置走到右下 有幾種方法
        # @cache
        def dp(i,j):
            # print(i,j)
            if obstacleGrid[i-1][j-1] == 1 :  # tricky 反正旋轉180度結果還是會一樣
                # print(i,j,"return 0")
                return 0
            if i == 1 and j == 1 :
                return 1
            elif i == 1 :
                return dp(i,j-1)
            elif j == 1 :
                return dp(i-1,j)
            else :
                return dp(i-1,j) + dp(i,j-1)

        return dp(len(obstacleGrid),len(obstacleGrid[0]))

# given ans
# 採用沒有 recursive 的寫法
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         # dp[i][j] := unique paths from (0, 0) to (i - 1, j - 1)
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
#         dp[0][1] = 1  # can also set dp[1][0] = 1

#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if obstacleGrid[i - 1][j - 1] == 0:
#                     dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

#         return dp[m][n]

s = Solution()
print(s.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
print(s.uniquePathsWithObstacles(obstacleGrid = [[0,0]]))
print(s.uniquePathsWithObstacles(obstacleGrid = [[1,0]]))
print(s.uniquePathsWithObstacles(obstacleGrid = [[0,0],[1,1],[0,0]]))
