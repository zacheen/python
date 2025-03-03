# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/description/

# my practice again : 0ms Beats100.00%
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for _ in range(1,m) :
            for i in range(1,n):
                dp[i] = dp[i]+dp[i-1]
        return dp[-1]

s = Solution()
print(s.uniquePaths(m = 3, n = 7))
print(s.uniquePaths(m = 3, n = 2))


