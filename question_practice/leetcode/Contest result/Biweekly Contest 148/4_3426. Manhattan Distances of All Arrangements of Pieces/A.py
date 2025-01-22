# 3426. Manhattan Distances of All Arrangements of Pieces
# https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/description/

from typing import List
import functools

from math import comb
# given ans 1 : 1328ms Beats39.10%
mod = 10**9+7
class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        base = comb(m * n - 2, k - 2) % mod
        res = 0
        for d in range(1, n):
            res += d * (n - d) * m * m
        for d in range(1, m):
            res += d * (m - d) * n * n
        return res * base % mod

# # related to math ...
# # given ans 2 : 149ms Beats90.48%
# mod = 10**9+7
# class Solution:
#     def distanceSum(self, m: int, n: int, k: int) -> int:
#         num = den = 1
#         for i in range(min(k-2,m*n-k)):
#             num *= m*n-2-i
#             den *= i+1
#             num %= mod
#             den %= mod
#         c = (num*pow(den,-1,mod))%mod
#         return (c*((m*m*n*(n+1)*(n-1)+n*n*m*(m+1)*(m-1))//6))%mod

s = Solution()
print("ans :",s.distanceSum(m = 2, n = 2, k = 2)) # 8
print("ans :",s.distanceSum(m = 1, n = 4, k = 3)) # 20



