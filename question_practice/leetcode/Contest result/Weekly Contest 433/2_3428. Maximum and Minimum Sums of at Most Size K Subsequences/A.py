# 3428. Maximum and Minimum Sums of at Most Size K Subsequences
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

from typing import List
import functools

MOD = 10**9+7

# # my Time Limit Exceeded : involve big combination number
# from math import comb
# class Solution:
#     def minMaxSums(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         len_n = len(nums)
#         ans = 0
#         for i,(min_n, max_n) in enumerate(zip(nums, reversed(nums))) :
#             remain_cou = len_n - (i+1)
#             if remain_cou < 0 : break
#             for k_i in range(k) :
#                 cou = comb(remain_cou, k_i)
#                 ans = (ans + cou*(min_n + max_n))%MOD
#         return ans

# ref No.1 how to cal comb : 5609ms Beats100.00%
class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        # prepare for cal comb in faster way
        n = len(nums)
        fact = [1]*(n+1)
        invfact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = (fact[i-1] * i) % MOD
        invfact[n] = pow(fact[n], MOD-2, MOD)
        for i in reversed(range(n)):
            invfact[i] = (invfact[i+1]*(i+1)) % MOD

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return (fact[n]*((invfact[r]*invfact[n-r]) % MOD)) % MOD
        
        nums.sort()
        len_n = len(nums)
        ans = 0
        for i,(min_n, max_n) in enumerate(zip(nums, reversed(nums))) :
            remain_cou = len_n - (i+1)
            if remain_cou < 0 : break
            for k_i in range(k) :
                cou = comb(remain_cou, k_i)
                ans = (ans + cou*(min_n + max_n))%MOD
        return ans

s = Solution()
print("ans :",s.minMaxSums(nums = [1,2,3], k = 2)) # 24
print("ans :",s.minMaxSums(nums = [5,0,6], k = 1)) # 22
print("ans :",s.minMaxSums(nums = [1,1,1], k = 2)) # 12
print("ans :",s.minMaxSums(nums = [0,1,1], k = 3)) # 9



