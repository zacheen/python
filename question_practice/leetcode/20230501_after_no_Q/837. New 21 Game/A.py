# 837. New 21 Game
# 

from typing import List
import functools

# # my 
# class Solution:
#     def new21Game(self, n: int, k: int, maxPts: int) -> float:
#         # 找出所有可以的組合
#         # 然後進行排列 計算 總共組合
#         # 會超出 time limit
#         pass

# # my 
# class Solution:
#     def new21Game(self, n: int, k: int, maxPts: int) -> float:
#         # 我把 n 切成 k 份 (每份 >0 <=maxPts)
#         # 沒想法了
#         pass


# given ans Beats 60.17%
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # When the game ends, the point is in [k..k - 1 + maxPts]
        #   P = 1, if n >= k - 1 + maxPts
        #   P = 0, if n < k (note the constraints already have k <= n)
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        ans = 0.0
        dp = [1.0] + [0] * n  # dp[i] := prob to have i points
        windowSum = dp[0]  # P(i - 1) + P(i - 2) + ... + P(i - maxPts)

        for i in range(1, n + 1):
            # The prob to get point i is
            # P(i) = [P(i - 1) + P(i - 2) + ... + P(i - maxPts)] / maxPts
            dp[i] = windowSum / maxPts
            if i < k:
                windowSum += dp[i]
            else:  # The game ends
                ans += dp[i]
            if i - maxPts >= 0:
                windowSum -= dp[i - maxPts]

        return ans

s = Solution()
# 0 <= k <= n <= 10**4
# n : 
# k : 總和到達 k 點就要停
# maxPts : 每次抽牌最大可能的點數
# print(s.new21Game(n = 10, k = 1, maxPts = 10))
# print(s.new21Game(n = 6, k = 1, maxPts = 10))
# print(s.new21Game(n = 21, k = 17, maxPts = 10))
print(s.new21Game(n = 20, k = 3, maxPts = 11))



