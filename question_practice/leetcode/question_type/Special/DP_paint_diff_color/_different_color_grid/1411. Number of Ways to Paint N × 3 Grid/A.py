# 1411. Number of Ways to Paint N × 3 Grid
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/

# given ans 3ms Beats97.22%
MOD = 10**9+7
class Solution:
    def numOfWays(self, n: int) -> int:
        color2 = 6  # 121, 131, 212, 232, 313, 323
        color3 = 6  # 123, 132, 213, 231, 312, 321
        for i in range(1, n) :
            nextColor2 = color2 * 3 + color3 * 2
            nextColor3 = color2 * 2 + color3 * 2
            color2 = nextColor2 % MOD
            color3 = nextColor3 % MOD
        return (color2 + color3) % MOD

s = Solution()
print("ans :",s.numOfWays(n = 1)) # 12
print("ans :",s.numOfWays(n = 2)) # 54



