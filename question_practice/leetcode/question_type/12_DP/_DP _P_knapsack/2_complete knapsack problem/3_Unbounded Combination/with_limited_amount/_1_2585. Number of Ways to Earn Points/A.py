# 2585. Number of Ways to Earn Points
# https://leetcode.com/problems/number-of-ways-to-earn-points/

from typing import List
from math import inf

# 71ms Beats100.00%
MOD = 10**9+7
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [1] + [0]*target
        s = 0
        for max_lim, coin in types:
            s = min(s+coin*max_lim, target) # 到目前為止最大可能總和
            # 先正常計算所有可能組合數量
            for fut_i in range(coin, s+1):
                dp[fut_i] += dp[fut_i-coin]
            # 再減去超過使用次數c的組合數量
            t = (max_lim+1)*coin
            for fut_i in range(s, t-1, -1):
                dp[fut_i] -= dp[fut_i-t]
        return dp[-1] % MOD

# 683ms Beats99.41%
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp=[1]+[0]*target
        for cou, mar in types:
            new_dp = dp.copy()
            for i in range(0, len(dp)):  # 從小到大
                if dp[i] != 0 :
                    for fut_i in range(i+mar, min(i+(cou*mar)+1 , len(dp)), mar):
                        new_dp[fut_i] += dp[i]
            dp = new_dp
        return dp[target]%(10**9+7)

s = Solution()
print("ans :",s.waysToReachTarget(target = 6, types = [[6,1],[3,2],[2,3]])) # 7
print("ans :",s.waysToReachTarget(target = 5, types = [[50,1],[50,2],[50,5]])) # 4
print("ans :",s.waysToReachTarget(target = 18, types = [[6,1],[3,2],[2,3]])) # 1



