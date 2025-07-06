# 1155. Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum

from typing import List
from math import inf
MOD = 10**9+7

# optimize using prefix : 0ms
    # 有 coin value = 1, shift 完之後 每次可以拿最多 k-1 個
    # 總共可以拿 n 次
    # 所以可以用 template C_Knap_comb_limit
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if not (n <= target <= n * k):
            return 0  # 无法组成 target

        shift = 1 # shift values from 1~6 to 0~5
        k -= shift
        target -= n*shift
        dp = [1] + [0]*(target) # dp[i] : 總合為 i 有多少種組合
        for i in range(1, n+1):
            max_j = min(i*k, target)  # i 个骰子至多掷出 i*k
            for fut_i in range(1, max_j+1):
                dp[fut_i] += dp[fut_i-1]  # 原地计算 f 的前缀和
            for fut_i in range(max_j, k, -1):
                dp[fut_i] -= dp[fut_i-(k+1)] # dp[j] 是两个前缀和的差
        return dp[-1] % MOD

s = Solution()
print("ans :",s.numRollsToTarget(n = 1, k = 6, target = 3)) # 1
print("ans :",s.numRollsToTarget(n = 2, k = 6, target = 7)) # 6
print("ans :",s.numRollsToTarget(n = 3, k = 6, target = 6)) # 10
print("ans :",s.numRollsToTarget(n = 3, k = 6, target = 10)) # 27
print("ans :",s.numRollsToTarget(n = 30, k = 30, target = 500)) # 222616187



