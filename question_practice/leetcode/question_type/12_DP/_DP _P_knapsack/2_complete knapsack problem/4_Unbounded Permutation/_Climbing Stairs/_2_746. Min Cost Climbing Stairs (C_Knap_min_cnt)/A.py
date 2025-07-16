# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List
from math import inf

# using my template C_Knap_min_cnt : 3ms Beats73.40%
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 新增起點 跟 終點
        cost = [0] + cost + [0]
        def C_Knap_min_cnt(nums, target):
            dp = [0]
            for i in range(1,target+1):
                min_c = inf
                for n in nums :
                    if (pre_i:=i-n) >= 0 and (cou:=dp[pre_i]) < min_c:
                        min_c = cou
                dp.append(min_c+cost[i])
            return dp[-1]
        nums = [1,2]
        return C_Knap_min_cnt(nums, len(cost)-1)

# given ans : 3ms Beats73.40% (should be faster)
class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])

s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))



