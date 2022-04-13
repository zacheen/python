# my Runtime: 32 ms, faster than 89.30% of Python3
class Solution:
    def uniquePaths(self, m, n):
        # i*j 的方格有幾種走法
        # 或是代表 (i,j) 這個位置走到右下 有幾種方法
        # @cache
        def dp(i,j):
            if j > i :
                return dp(j,i)
            if i == 1 or j == 1 :
                return 1
            else :
                return dp(i-1,j) + dp(i,j-1)

        return dp(m,n)

# given ans
# 採用沒有 recursive 的寫法
# class Solution:
#     def uniquePaths(self, m, n):
#     # dp[i][j] := unique paths from (0, 0) to (i, j)
#         dp = [[1] * n for _ in range(m)]

#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

#         return dp[-1][-1]

s = Solution()
print(s.uniquePaths(m = 3, n = 7))
print(s.uniquePaths(m = 3, n = 2))


