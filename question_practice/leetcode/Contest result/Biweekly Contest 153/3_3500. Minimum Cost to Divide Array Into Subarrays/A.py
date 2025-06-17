# 3500. Minimum Cost to Divide Array Into Subarrays
# https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/description/

from typing import List
from math import inf
from itertools import accumulate

# my inspire by given ans : 3183ms Beats53.73%
    # (nums[0] + nums[1] + ... + nums[r] + k * i) * (cost[l] + cost[l + 1] + ... + cost[r])
    # = (sum(num[0~r]) + k*i) + sum(cost[l~r])
    # = (sum(num[0~r] * sum(cost[l~r])) + (k*i * sum(cost[l~r]))
    # 移除 i : https://youtu.be/wIxXbvmj4Hk?si=S9JbI_rc0pz8K_3D&t=1114
    # = (sum(num[0~r] * sum(cost[l~r])) + sum(cost[l~end])
class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        acc_nums = list(accumulate(nums))
        def sum_nums(end_r) : # include acc_nums[end_r]
            return acc_nums[r]
        
        acc_cost = [0] + list(accumulate(cost))
        def sum_cost(l, r = len(nums)-1) : # include both acc_nums[l], acc_nums[r]
            return acc_cost[r+1] - acc_cost[l]
        
        # DP
        dp = [0] # dp[end_pos] : 到 end_pos 為止最小的 cost
        for r in range(len(nums)): # include nums[r]
            dp.append( min(
                sum_nums(r)*sum_cost(i_sep,r) + k*sum_cost(i_sep) + c_sep
                for i_sep, c_sep in enumerate(dp)
            ))
        return dp[-1]

# given ans : 26ms Beats77.61%
    # 根據公式推論出 best decision
class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        nums_acc = [0] + list(accumulate(nums))
        cost_acc = [0] + list(accumulate(cost))
        sum_cost = cost_acc[n]
        dp = [0]*(n+1)
        hull_m = [0]
        hull_b = [0]
        ptr = 0
        def query(x):
            nonlocal ptr
            while ptr+1 < len(hull_m) and hull_m[ptr+1]*x + hull_b[ptr+1] <= hull_m[ptr]*x + hull_b[ptr]:
                ptr +=1
            return hull_m[ptr]*x+hull_b[ptr]
        def is_bad(m1,b1,m2,b2,m3,b3):
            return (b2-b1)*(m2-m3) >= (b3-b2)*(m1-m2)
        for r in range(1,n+1):
            dp[r] = nums_acc[r]*cost_acc[r]+k*sum_cost+query(nums_acc[r])
            m_new = -cost_acc[r]
            b_new = dp[r]-k*cost_acc[r]
            while len(hull_m) >= 2 and is_bad(hull_m[-2],hull_b[-2],hull_m[-1],hull_b[-1],m_new, b_new):
                hull_m.pop()
                hull_b.pop()
            hull_m.append(m_new)
            hull_b.append(b_new)
        return dp[n]       

s = Solution()
# print("ans :",s.minimumCost(nums = [3,1,4], cost = [4,6,6], k = 1)) # 110
print("ans :",s.minimumCost(nums = [4,8,5,1,14,2,2,12,1], cost = [7,2,8,4,2,2,1,1,2], k = 7)) # 985
