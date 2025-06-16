# 1143. Longest Common Subsequence (Subsequence 可以不相連)
# https://leetcode.com/problems/longest-common-subsequence

# template 1D array : 319ms Beats97.26%
class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        # 1 finding longest common subsequence length
        dp = [0]*(len(str2)+1)
        for c1 in str1 :
            new_dp = dp.copy()
            for j, c2 in enumerate(str2) :
                if c1 == c2 :
                    new_dp[j+1] = dp[j] + 1
                else :
                    new_dp[j+1] = max(dp[j+1], new_dp[j])
            dp = new_dp
        return dp[-1] 

# template 2D array : 415ms Beats84.78%
class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        # 1 finding longest common subsequence length
        dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
        for i, c1 in enumerate(str1) :
            for j, c2 in enumerate(str2) :
                if c1 == c2 :
                    dp[i+1][j+1] = dp[i][j] + 1
                else :
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])  
        return dp[-1][-1]

s = Solution()
print(s.longestCommonSubsequence("abcde", "deabc" )) # 3, abc
print(s.longestCommonSubsequence("abac", "cab" )) # 2, ab
print(s.longestCommonSubsequence("abcde", "ace" )) # 3, ace
print(s.longestCommonSubsequence("abc", "def" )) # 0



