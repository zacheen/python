# 2466. Count Ways To Build Good Strings
# https://leetcode.com/problems/count-ways-to-build-good-strings/

from typing import List
import functools

# my 2024/12/30 70ms Beats96.36%
import math
MOD = 10**9 + 7
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1]
        for i in range(1, high+1, 1) :
            now_c = 0
            # appending zero
            prev_i = i-zero
            if prev_i >= 0 :
                now_c += dp[prev_i]
            # appending one
            prev_i = i-one
            if prev_i >= 0 :
                now_c += dp[prev_i]
            dp.append(now_c % MOD)
        return sum(dp[low:]) % MOD

# # my v2 Beats 89.76%
# # mem 也 %
# class Solution:
#     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
#         mem = [1]+[0]*(high) # 空字串是一種組合
#         ans = 0
#         for i in range(1, high+1) :
#             zero_comb = 0
#             last_zero = i-zero
#             one_comb = 0
#             last_one = i-one
#             if last_zero >= 0 :
#                 zero_comb = mem[last_zero]
#             if last_one >= 0 :
#                 one_comb = mem[last_one]
            
#             mem[i] = (zero_comb + one_comb) % 1000000007
#             if i >= low :
#                 # ans = (ans + mem[i]) % 1000000007
#                 ans += mem[i]
#                 if ans >= 1000000007 :
#                     ans = ans - 1000000007
#         # print(mem)
#         return ans
    
# given ans gcd optimization
class Solution:
    def countGoodStrings(self, low, high, zero, one) -> int:  # num theory applied dp
        print(low, high, zero, one)
        # this block is optional gcd optimization
        gcd = math.gcd(zero, one)
        zero //= gcd
        one  //= gcd
        high //= gcd
        low = (low-1)//gcd + 1
        print(low, high, zero, one)

        mod = 10**9+7
        dp = [0] * (high+1)
        dp[0] = 1
        for i in range(1, high+1):
            dp[i] = (dp[i-zero]+dp[i-one]) % mod
        return sum(dp[low:]) % mod


# given ans Beats 97.64%
# 更優化我的流程
# 註解的地方是我再優化 
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        kMod = 1_000_000_007
        # ans = 0
        # dp[i] := # of good strings with length i
        dp = [1] + [0] * high

        for i in range(1, high + 1):
            if i >= zero:
                # dp[i] = (dp[i] + dp[i - zero]) % kMod
                dp[i] = dp[i - zero]
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % kMod
            # if i >= low:
            #     ans = (ans + dp[i]) % kMod

        return sum(dp[low:high+1]) % kMod

s = Solution()
print(s.countGoodStrings(low = 3, high = 3, zero = 1, one = 1))
print(s.countGoodStrings(low = 2, high = 3, zero = 1, one = 2))



