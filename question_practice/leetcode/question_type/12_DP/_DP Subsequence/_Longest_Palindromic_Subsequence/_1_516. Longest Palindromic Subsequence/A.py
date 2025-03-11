

# given ans Runtime: 862 ms, faster than 98.31% of Python3
# 用包圍的 好像有一些位置甚至不會跑 所以還比較快
class Solution:
    def longestPalindromeSubseq(self, s):
        dp = [[0]*len(s) for _ in range(len(s))]
        def lps(i, j) :
            nonlocal s
            # base case
            if i>j :
                return 0
            if i==j :
                return 1
            # 代表跑過了
            if dp[i][j] > 0 :
                return dp[i][j]
            
            if (s[i] == s[j]) :
                dp[i][j] = 2 + lps(i+1, j-1)
            else :
                dp[i][j] = max(lps(i+1, j), lps(i, j-1))
                
            return dp[i][j]
        
        return lps(0, len(s)-1)

# 20230414 重新練習 Beats 96.24%
# 使用 recursive 的方法
import functools
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @functools.lru_cache()
        def dp(l,r):
            if l > r :
                return 0
            if l == r :
                return 1
            
            if s[l] == s[r] :
                return dp(l+1, r-1) + 2
            else :
                return max(dp(l+1, r), dp(l, r-1))

        return dp(0,len(s)-1)

# 找到其他的 given ans
# # given ans Beats 40%
# # Memory Beats 74.67%
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         # dp[i][j] := LPS's length in s[i..j]
#         dp = [[0] * n for _ in range(n)]

#         for i in range(n):
#             dp[i][i] = 1

#         for d in range(1, n):
#             for i in range(n - d):
#                 j = i + d
#                 if s[i] == s[j]:
#                     dp[i][j] = 2 + dp[i + 1][j - 1]
#                 else:
#                     dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
#         return dp[0][n - 1]
    
s = Solution()
print(s.longestPalindromeSubseq("bbbab"))
print(s.longestPalindromeSubseq("cbbd"))



