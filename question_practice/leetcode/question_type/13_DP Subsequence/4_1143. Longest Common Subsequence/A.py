
# given ans
class Solution:
    def longestCommonSubsequence(self, text1, text2) :
        # dp[i][j] := LCS's length of text1[0..i) and text2[0..j)
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1,len(text1)+1) :
            for j in range(1,len(text2)+1) :
                if text1[i-1] == text2[j-1] :
                    dp[i][j] = 1 + dp[i-1][j-1]
                else :
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            print(dp)
        return dp[len(text1)][len(text2)]

# my 參考 given ans 寫成 recursive
# 通常 兩個參數用 cache 都會比較慢
# Runtime: 801 ms, faster than 32.11% of Python3
# class Solution:
#     def longestCommonSubsequence(self, text1, text2) :
#         @cache
#         def rec(i, j):
#             if i < 0 or j < 0 :
#                 return 0

#             if text1[i] == text2[j] :
#                 return 1+rec(i-1, j-1) # 為什麼不用 return max(1+rec(i-1, j-1), 左減一, 右減一)  因為這個一定比較大
#             else :
#                 return max(rec(i-1, j), rec(i, j-1))

#         return rec(len(text1)-1, len(text2)-1)

s = Solution()
print(s.longestCommonSubsequence(text1 = "abcde", text2 = "deabc" ))
# print(s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))
# print(s.longestCommonSubsequence(text1 = "abc", text2 = "def" ))



