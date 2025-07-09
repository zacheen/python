# 3599. Partition Array to Minimize XOR
# https://leetcode.com/problems/partition-array-to-minimize-xor/description/

from typing import List
from math import inf
from functools import cache

# my (recursive version): 7636ms Beats84.16%
class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        @cache
        def dp(now_i, rem_k):
            if rem_k == 0 :
                if now_i == len(nums) :
                    return 0
                else :
                    return inf
            if now_i >= len(nums) :
                return inf
            
            rem_k -= 1
            now_xor = 0
            min_ret = inf
            for next_i in range(now_i, len(nums)-rem_k) :
                now_xor ^= nums[next_i]
                min_ret = min(min_ret, max(dp(next_i+1, rem_k), now_xor))
            return min_ret
        return dp(0, k)

# my (for version) : 5503ms Beats91.83%
    # but optimize takes time
class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        xor_acc = []
        now_xor = 0
        for n in nums :
            now_xor ^= n
            xor_acc.append(now_xor)
        # print(xor_acc)

        dp = xor_acc.copy() # 紀錄從 0~i 分成for組 最好的組合
        len_dp = len(dp)
        # xor_acc = [0]+xor_acc
        for rou in range(1,k): # -1 因為 xor_acc 已經做一次了
            new_dp = [inf]*len_dp
            for i in range(rou, len_dp):
                min_res = inf
                xor_acc_front = xor_acc[i]
                for h, prev in enumerate(dp[rou-1:i], rou-1) :
                    now_xor = xor_acc_front^xor_acc[h] # h~i 不包含 h
                    max_sub = prev if prev > now_xor else now_xor
                    if max_sub < min_res :
                        min_res = max_sub
                new_dp[i] = min_res
            dp = new_dp
        return dp[-1]

s = Solution()
print("ans :",s.minXor(nums = [1,2,3], k = 2)) # 1
print("ans :",s.minXor(nums = [2,3,3,2], k = 3)) # 2
print("ans :",s.minXor(nums = [1,1,2,3,1], k = 2)) # 0



