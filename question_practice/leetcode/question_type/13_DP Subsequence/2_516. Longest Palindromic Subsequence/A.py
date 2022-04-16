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

s = Solution()
print(s.longestPalindromeSubseq("bbbab"))
print(s.longestPalindromeSubseq("cbbd"))



