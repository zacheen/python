# 3290. Maximum Multiplication Score
# https://leetcode.com/problems/maximum-multiplication-score/description/

from typing import List
from math import inf

# my : 576ms Beats78.26%
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [0]*(len(b)+1)
        for i, c1 in enumerate(a) :
            new_dp = [-inf] # 這裡加 -inf 是因為不能跳過任何項目
            for j, c2 in enumerate(b) :
                new_dp.append( max(dp[j]+c1*c2, new_dp[j]) )
            dp = new_dp
        return dp[-1]


# given ans : concept more like knapsack_01
class Solution:
    def maxScore(self, a: list[int], b: list[int]) -> int:
        # dp[i] := the maximum score of a[0..i]
        dp = [-inf] * 4
        for num in b:
            for i in reversed(range(4)):
                # Skip `num` or pair a[i] with `num`.
                dp[i] = max(dp[i], (dp[i - 1] if i > 0 else 0) + a[i] * num)
        return dp[3]

s = Solution()
print("ans :",s.maxScore(a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7])) # 26
print("ans :",s.maxScore(a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4])) # -1

