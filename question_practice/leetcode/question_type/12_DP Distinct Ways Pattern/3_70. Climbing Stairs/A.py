# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

# my practice again : 0ms Beats100.00%
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 : return 1
        dp = [1,2]
        for i in range(2,n) :
            dp.append(dp[-1] + dp[-2])
        return dp[-1]

# given ans 一樣

s = Solution()
print(s.climbStairs(3))



