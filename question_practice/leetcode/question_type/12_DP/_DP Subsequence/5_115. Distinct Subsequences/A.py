# my 印象之前做過類似的題目
# Runtime: 304 ms, faster than 90.36% of Python3
# class Solution:
#     def numDistinct(self, s, t):

#         count = [1]+[0]*len(t)
#         for c in s :
#             for i in range(len(t)-1, -1, -1) :
#                 if t[i] == c :
#                     count[i+1] += count[i]

#         print(count)
#         return count[-1]


# given ans 一樣

# given ans 2D解法
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]

s = Solution()
print(s.numDistinct(s = "rabbbit", t = "rabbit"))
print(s.numDistinct(s = "babgbag", t = "bag"))
print(s.numDistinct(s = "baba", t = "ba"))

