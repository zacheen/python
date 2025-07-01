# 2902. Count of Sub-Multisets With Bounded Sum
# https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/description/

from typing import List
from math import inf
from collections import Counter

# my 745ms Beats98.18%
MOD = 10**9+7
class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        total = sum(nums)
        if l > total:
            return 0

        r = min(r, total)
        cnt = Counter(nums)
        dp = [1] + [0]*r
        # 排除掉0
        dp[0] += cnt[0]
        del cnt[0]

        s = 0
        for coin, max_lim in cnt.items():
            s = min(s+coin*max_lim, r) # 到目前為止最大可能總和
            # 先正常計算所有可能組合數量
            for fut_i in range(coin, s+1):
                dp[fut_i] += dp[fut_i-coin]
            # 再減去超過使用次數c的組合數量
            t = (max_lim+1)*coin
            for fut_i in range(s, t-1, -1):
                dp[fut_i] -= dp[fut_i-t]
        return sum(dp[l:]) % MOD

# my 745ms Beats100.00%
MOD = 10**9+7
class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        total = sum(nums)
        if l > total:
            return 0

        r = min(r, total)
        cnt = Counter(nums)
        dp = [1] + [0]*r
        # 排除掉0
        dp[0] += cnt[0]
        del cnt[0]

        s = 0
        for coin, max_lim in cnt.items():
            s = min(s+coin*max_lim, r) # 到目前為止最大可能總和
            # 先正常計算所有可能組合數量
            for fut_i in range(coin, s+1):
                dp[fut_i] += dp[fut_i-coin]
            # 再減去超過使用次數c的組合數量
            t = (max_lim+1)*coin
            for fut_i in range(s, t-1, -1):
                dp[fut_i] -= dp[fut_i-t]
        return sum(dp[l:]) % MOD

s = Solution()
print("ans :",s.countSubMultisets(nums = [1,2,2,3], l = 6, r = 6)) # 1
print("ans :",s.countSubMultisets(nums = [2,1,4,2,7], l = 1, r = 5)) # 7
print("ans :",s.countSubMultisets(nums = [1,2,1,3,5,2], l = 3, r = 5)) # 9



