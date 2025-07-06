# 1155. Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum

from typing import List
from math import inf
MOD = 10**9+7

# 最快使用 C_Knap_comb_limit : 0ms
    # 有 coin value = 1, shift 完之後 每次可以拿最多 k-1 個
    # 總共可以拿 n 次

# my 106ms Beats86.31% 
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # 20ms Beats98.22%
        if target < n or target > n * k:
            return 0
        
        dp = [1]+[0]*(target)
        for _ in range(n):
            new_dp = [0]*(target+1)
            for fut_i in range(target, -1, -1):
                # < coin is a single value>
                new_dp[fut_i] = sum(dp[fut_i-num] for num in nums)
                # < available coin is a range> EX: 1~k
                new_dp[fut_i] = sum(dp[max(0,fut_i-k) : fut_i])
                    # (expand)
                    # for num in range(1,min(k, fut_i)+1):
                    #     new_dp[fut_i] += dp[fut_i-num]
            dp = new_dp
        return dp[-1] % MOD

# my 238ms Beats64.43%
MOD = 10**9+7
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [1]+[0]*(target)
        for _ in range(n):
            new_dp = [0]*(target+1)
            for num in range(1,k+1):
                for fut_i in range(target, num-1, -1):
                    # dp[fut_i] = (dp[fut_i]+old_dp[fut_i-num]) % MOD
                    new_dp[fut_i] += dp[fut_i-num]
            dp = new_dp
        return dp[-1] % MOD

s = Solution()
print("ans :",s.numRollsToTarget(n = 1, k = 6, target = 3)) # 1
print("ans :",s.numRollsToTarget(n = 2, k = 6, target = 7)) # 6
print("ans :",s.numRollsToTarget(n = 3, k = 6, target = 6)) # 10
print("ans :",s.numRollsToTarget(n = 3, k = 6, target = 10)) # 27
print("ans :",s.numRollsToTarget(n = 30, k = 30, target = 500)) # 222616187



