# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

# using C_Knap_perm template
class Solution:
    def climbStairs(self, n: int) -> int:
        # 爬梯問題可以想成 Unbounded Permustation，只是 nums 只有 1 到 MAX 的爬梯限制
            # 我可以取無限個 1, 2, MAX 組成 target(梯子的底)
        nums = [1, 2]
        # using C_Knap_perm template
        dp = [1]
        for i in range(1,n+1):
            dp.append(sum( dp[i-n] for n in nums if i>=n ) )
        return dp[-1]
    
# my practice again : 0ms Beats100.00%
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 : return 1
        dp = [1,2]
        for i in range(2,n) :
            dp.append(dp[-1] + dp[-2]) # 從前面一格過來(爬一格) + 從前面兩格過來(爬兩格)
        return dp[-1]

s = Solution()
print(s.climbStairs(3))



