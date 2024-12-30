# 3405. Count the Number of Arrays with K Matching Adjacent Elements
# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/description/

from typing import List
import functools
MOD = mod = 10**9+7

# my opt 3209ms Beats100.00%
from math import comb
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # pick numbers and become a list n-k (each item have to differ from the previous one)
            # first one can be any number > m
            # second one have to choose a number that is not first one > (m-1)
            # m(first)*(m-1)**(n-k-1)  # n-k-1 = all - later expand - first one 
        ans = m*pow(m-1,n-k-1, mod=MOD) 
        # putting these number into n space, but the first one have to fit one number first
            # EX: n = 3, m = 2, k = 0 changing to n = 4, m = 2, k = 1 above is the same
            # _ _ _ _ put in 1,2,1 
                # if I put like "1 _ 2 1" than the _ follow the previous one and become 1121 
                # but "_ 1 2 1" _ cannot follow by anything, so is not available
            # that is why comb( (n-1), (n-k-1) )
                # the first space have to fit one number first 1 _ _ _ remain 2,1
            # comb( (n-1), (n-k-1) ) = comb( (n-1), (n-1)-(n-k-1) ) = comb( (n-1), k )
        ans *= (comb(n-1, k) % MOD)
        return ans % (MOD)

# # given ans (to cal faster and prevent result getting too big)
# MOD = mod = 10**9+7
# N=2*10**5+1
# fac = [1]*N  #fac[i] i的阶乘
# ifac = [1]*N #ifac[i] i的阶乘 的逆元
# inv = [0]*N  #inv[i]  i的逆元
# inv[1]=1 
# for i in range(2, N):
#     fac[i] = fac[i-1]*i%mod
#     inv[i] = (mod - mod // i) * inv[mod % i] % mod
#     ifac[i] = ifac[i-1]*inv[i]%mod
# def C(n: int, k: int) -> int:  #不重复组合数，n个不同物品不重复无序的取出k个
#     if n < 0 or k < 0 or n < k:
#         return 0
#     return ((fac[n] * ifac[k]) % MOD * ifac[n - k]) % MOD
# class Solution:
#     def countGoodArrays(self, n: int, m: int, k: int) -> int:
#         res=m*pow(m-1,n-k-1,mod)%mod
#         n,m=k,n-k
#         res*=C(n+m-1,n)
#         return res%mod

# # my fail 
# I thought every number from 1~m have to appear at least one

s = Solution()
# print("ans :",s.countGoodArrays(n = 3, m = 2, k = 1)) # 4
# print("ans :",s.countGoodArrays(n = 4, m = 2, k = 2)) # 6
# print("ans :",s.countGoodArrays(n = 5, m = 2, k = 0)) # 2
print("ans :",s.countGoodArrays(n = 3, m = 2, k = 0)) # 2
print("ans :",s.countGoodArrays(n = 4, m = 2, k = 1)) # 2
print("ans :",s.countGoodArrays(n = 5, m = 2, k = 2)) # 2


# print("ans :",s.countGoodArrays(n = 4, m = 2, k = 1)) # 2




