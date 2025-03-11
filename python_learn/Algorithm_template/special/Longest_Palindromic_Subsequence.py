# Longest_Palindromic_Subsequence
# 找尋最長的 Palindrom (第n個字 == 第len-n個字)

from functools import cache

# 用包圍的 好像有一些位置甚至不會跑 所以還比較快
def LPS(self, s):
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

# 用 cache 比較慢
def LPS_cache(self, s):
    @cache
    def lps(i, j) :
        nonlocal s
        # base case
        if i>j :
            return 0
        if i==j :
            return 1
        
        if (s[i] == s[j]) :
            return 2 + lps(i+1, j-1)
        else :
            return max(lps(i+1, j), lps(i, j-1))
    return lps(0, len(s)-1)