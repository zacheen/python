# 2518. Number of Great Partitions
# https://leetcode.com/problems/number-of-great-partitions

from typing import List
from math import inf

# my using template knapsack_01_comb v1 : 47ms Beats100.00%
MOD = 10**9+7
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < k*2: return 0
        # 一定要先排除不可能的狀況
        # 因為後面有 (sum(dp))*2
            # 如果沒有排除 代表有可能 sum1 < k 且 sum2 < k
            # 但*2時 其實sum2 < k已經計算過一次了，所以會重複計算
        
        k -= 1
        dp = [1]+[0]*(k)
        for num in nums:
            for fut_i in range(k, num-1, -1):
                dp[fut_i] += dp[fut_i-num]

        # 全部的可能組合數 - 其中一邊的和少於 k (因為有兩邊所以*2)
        all_comb = pow(2, len(nums), MOD)
        invalid = sum(dp)*2
        return (all_comb-invalid) % MOD


s = Solution()
# print("ans :",s.countPartitions(nums = [1,2,3,4], k = 4)) # 
print("ans :",s.countPartitions([96,40,22,98,9,97,45,22,79,57,95,62], 505)) # 
# print("ans :",s.countPartitions()) # 



