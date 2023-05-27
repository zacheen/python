# 1406. Stone Game III
# https://leetcode.com/problems/stone-game-iii/description/

from typing import List
import functools

# my Beats 19.29%
# commit fail once : 有負的分數，所以如果可以全拿也不一定要拿
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        max_i = len(stoneValue) - 1
        sum_i_to_end = stoneValue.copy()
        for i in range(max_i,0,-1):
            sum_i_to_end[i-1] += sum_i_to_end[i]
        # print(sum_i_to_end)

        # i 是此玩家在此位子 最多可以拿到多少分
        @functools.lru_cache(None)
        def max_score(i):
            if i > max_i :
                return 0
            return sum_i_to_end[i] - min(max_score(x) for x in range(i+1,i+4))

        Alice_score = max_score(0)
        score_diff = Alice_score - (sum_i_to_end[0] - Alice_score)# - Bob_Score
        # print(Alice_score, Bob_score)
        if score_diff > 0 :
            return "Alice"
        elif score_diff < 0 :
            return "Bob"
        else :
            return "Tie"

# my v2 改成 for 迴圈版本
# Beats 97.31%
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        max_i = len(stoneValue) - 1
        sum_i_to_end = stoneValue.copy()
        for i in range(max_i,0,-1):
            sum_i_to_end[i-1] += sum_i_to_end[i]
        # print(sum_i_to_end)

        # i 是此玩家在此位子 最多可以拿到多少分
        dp = [0]*(len(stoneValue)+1)
        for i in range(max_i,-1,-1):
            # print(i, sum_i_to_end[i], dp[i+1:min(len(dp), i+4)], dp)
            dp[i] = sum_i_to_end[i] - min(dp[i+1:min(len(dp), i+4)])
        # print(dp)
        Alice_score = dp[0]
        score_diff = Alice_score - (sum_i_to_end[0] - Alice_score)# - Bob_Score
        # print(Alice_score, (sum_i_to_end[0] - Alice_score))
        if score_diff > 0 :
            return "Alice"
        elif score_diff < 0 :
            return "Bob"
        else :
            return "Tie"

# given ans
# 還合併 sum_i_to_end 跟 dp 的 for 迴圈
import math
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] := max "relative score" Alice can make w/ stoneValue[i:]
        dp = [-math.inf] * n + [0]
        # 這裡的 dp 是差距最大的分數
        for i in reversed(range(n)):
            summ = 0
            for j in range(i, i + 3):
                if j == n:
                    break
                summ += stoneValue[j]
                dp[i] = max(dp[i], summ - dp[j + 1])

        score = dp[0]
        if score == 0:
            return 'Tie'
        return 'Alice' if score > 0 else 'Bob'

s = Solution()
print(s.stoneGameIII([1,2,3,7]))
print(s.stoneGameIII([1,2,3,-9]))
print(s.stoneGameIII([1,2,3,6]))
print(s.stoneGameIII([-1,-2,-3])) # 要注意有負的



