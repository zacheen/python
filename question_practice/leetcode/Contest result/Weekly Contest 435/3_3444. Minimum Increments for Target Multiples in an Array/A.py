# 3444. Minimum Increments for Target Multiples in an Array
# https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/description/
    # !!只能往上加

from typing import List
import functools

from math import inf,lcm

# my opt : 1182ms Beats100.00%
class Solution(object):
    def minimumIncrements(self, nums, target):
        len_t = len(target)
        for_mask_lim = 1 << len_t
        full_mask = for_mask_lim-1
        mem_gcd = []
        for mask in range(0, for_mask_lim): # 如果要加入空的就從 0 開始
            this_gcd = 1
            for i, tar in enumerate(target):
                if mask & (1 << i):
                    this_gcd = lcm(this_gcd, tar)
            mem_gcd.append(this_gcd)
        
        dp = [0] + [inf]*(full_mask) # each status min cost
        for n in nums :
            new_dp = dp.copy() # 要用新的 dp 以免同一個數字被 target 用兩次
            for mask in range(1, for_mask_lim):
                this_gcd = mem_gcd[mask]
                r = n % this_gcd
                cost = 0 if r==0 else this_gcd-r
                # update dp
                for dp_mask in range(0, for_mask_lim):
                    if dp_mask & mask > 0 :
                        continue
                    new_state = mask|dp_mask
                    new_cost = cost + dp[dp_mask]
                    if new_cost < new_dp[new_state] :
                        new_dp[new_state] = new_cost
            dp = new_dp
        return dp[-1]

# # given ans : 1704ms Beats100.00%
# class Solution(object):
#     def minimumIncrements(self, nums, target):
#         def gcd(a, b):
#             while b:
#                 a, b = b, a % b
#             return a
#         def lcm(a, b):
#             return a * b // gcd(a, b)
        
#         m = len(target)
#         full_mask = (1 << m) - 1
#         lcm_for_mask = []
#         for mask in range(0, full_mask+1):
#             L = 1
#             for i in range(m):
#                 if mask & (1 << i):
#                     L = lcm(L, target[i])
#             lcm_for_mask.append(L)

        
#         dp = [0] + [inf] * full_mask 
#         for x in nums:
#             candidate_options = []
#             for mask in range(1, full_mask+1):
#                 L = lcm_for_mask[mask]
#                 r = x % L
#                 cost = 0 if r == 0 else (L - r)
#                 candidate_options.append((mask, cost))
#             new_dp = dp.copy()
#             for state in range(full_mask+1):
#                 base = dp[state]
#                 if base == inf:
#                     continue
#                 for mask, cost in candidate_options:
#                     new_state = state | mask
#                     cand = base + cost
#                     if cand < new_dp[new_state]:
#                         new_dp[new_state] = cand
#             dp = new_dp
#         return dp[full_mask]



s = Solution()
print("ans :",s.minimumIncrements(nums = [1,2,3], target = [4])) # 1
print("ans :",s.minimumIncrements(nums = [8,4], target = [10,5])) # 2
print("ans :",s.minimumIncrements(nums = [1,30], target = [31,32])) # 32



