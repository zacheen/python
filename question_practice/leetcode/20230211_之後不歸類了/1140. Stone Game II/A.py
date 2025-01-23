# 1140. Stone Game II
# https://leetcode.com/problems/stone-game-ii/

from typing import List
import functools

# my 

# given ans : Beats 52.54%
# my 優化速度 : Beats 67.28%
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # 優化
        # suffix_sums = [0] * (n + 1)
        # suffix_sums[n - 1] = piles[n - 1]
        # for i in range(n - 2, -1, -1):
        #     suffix_sums[i] = suffix_sums[i + 1] + piles[i]
        # my 優化 
        suffixSum = piles.copy()
        for i in range(n - 2, -1, -1): 
            suffixSum[i] += suffixSum[i + 1]
        # suffixSum.append(0) # 其實也根本不會呼叫到最後一個
        # print(suffixSum)

        dp = [[0] * (n + 1) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffixSum[i]
                else:
                    # 優化
                    # for x in range(1, 2 * m + 1):
                        # opponent_score = dp[i + x][max(x, m)]
                        # score = suffixSum[i] - opponent_score
                        # dp[i][m] = max(dp[i][m], score)
                    ## my 優化 v1
                    # dp[i][m] = max(suffixSum[i] - dp[i + x][max(x, m)] for x in range(1, 2 * m + 1))
                    ## my 優化 v2
                    dp[i][m] = suffixSum[i] - min(dp[i + x][max(x, m)] for x in range(1, 2 * m + 1))

        return dp[0][1]

# given ans v2 Beats 83.41%
# 我再優化 Beats 97.70%
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # dp = [[0]*n for _ in range(n)]
        suffixSum = piles.copy()
        for i in range(n - 2, -1, -1): 
            suffixSum[i] += suffixSum[i + 1]
        print(suffixSum)

        # i 代表目前取到第幾個位置
        # M 是可以取的範圍
        # 回傳值是對此玩家來說，現在的狀況 i,M，取最好的結果最多可以拿到幾個石頭
            # 注意這裡不管是那個玩家都適用 dp() 去計算最好的結果
        @functools.lru_cache(None)
        def dp(i, M) :
            if i + 2*M >= n :
                return suffixSum[i]
            # 從這一格往後 找到 opponent 可以拿到的最小點數
            return suffixSum[i] - min(dp(i + X, max(M, X)) for X in range(1, 2*M + 1))
        
        return dp(0, 1)


s = Solution()
print(s.stoneGameII([2,7,9,4,4]))
print(s.stoneGameII([1,2,3,4,5,100]))



