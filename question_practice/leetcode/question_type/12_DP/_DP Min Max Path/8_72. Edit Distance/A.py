# my Runtime: 119 ms, faster than 93.00% of Python3
import math
class Solution:
    def minDistance(self, word1, word2):
        mem = [[math.inf]*len(word2) for _ in range(len(word1))]
        
        def dp(i,j):
            if i == -1 :
                return j+1
            if j == -1 :
                return i+1

            if mem[i][j] != math.inf :
                # print("do it before")
                return mem[i][j]
        
            if word1[i] == word2[j] :
                # print(i,j,i-1,j-1,"same",dp(i-1, j-1))
                mem[i][j] = dp(i-1, j-1)
            else :
                # insert or delete or replace
                # 其實 insert == delete 另外一邊的一個字母
                mem[i][j] = min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
                
            # print(i,j,word1[i],word2[j],mem[i][j])
            return mem[i][j]
        
        return dp(len(word1)-1, len(word2)-1)

# given ans
# 概念相同 只是用 for 迴圈實作
# class Solution:
#     def minDistance(self, word1, word2):
#         m = len(word1)
#         n = len(word2)
#         # dp[i][j] := min # of operations to convert word1[0..i) to word2[0..j)
#         dp = [[0] * (n + 1) for _ in range(m + 1)]

#         for i in range(1, m + 1):
#             dp[i][0] = i

#         for j in range(1, n + 1):
#             dp[0][j] = j

#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if word1[i - 1] == word2[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

#         return dp[m][n]

s = Solution()
# print(s.minDistance(word1 = "", word2 = ""))
# print(s.minDistance(word1 = "horse", word2 = "osr"))
# print(s.minDistance(word1 = "horse", word2 = "ros"))
# print(s.minDistance(word1 = "intention", word2 = "execution"))
# print(s.minDistance(word1 = "sa", word2 = "at"))
print(s.minDistance(word1 = "sea", word2 = "eat"))



