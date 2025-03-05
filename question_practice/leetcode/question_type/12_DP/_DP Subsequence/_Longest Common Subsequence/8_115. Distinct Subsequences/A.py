# 115. Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/description/

# my using knapsack_01 template : 207ms Beats90.59%
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1]+[0]*len(t)
        for c in s:
            for i in range(len(t)-1, -1, -1): # 從大到小
                if t[i] == c :
                    dp[i+1] += dp[i]
        return dp[-1]

# my using lcs template
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[1]+[0]*(len(t)) for _ in range(len(s)+1)]
        for i, c1 in enumerate(s) :
            for j, c2 in enumerate(t) :
                if c1 == c2 :
                    dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] += dp[i][j+1]
        return dp[-1][-1]

s = Solution()
print(s.numDistinct(s = "rabbbit", t = "rabbit")) # 3
print(s.numDistinct(s = "babgbag", t = "bag")) # 5
print(s.numDistinct(s = "baba", t = "ba")) # 3

