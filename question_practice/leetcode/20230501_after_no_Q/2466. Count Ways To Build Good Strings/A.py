# 2466. Count Ways To Build Good Strings
# https://leetcode.com/problems/count-ways-to-build-good-strings/

from typing import List
import functools

# # my v1 Beats 7.9%
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
            
#             mem[i] = zero_comb + one_comb
#             if i >= low :
#                 ans = (ans + mem[i]) % 1000000007
#         # print(mem)
#         return ans

# my v2 Beats 89.76%
# mem 也 %
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mem = [1]+[0]*(high) # 空字串是一種組合
        ans = 0
        for i in range(1, high+1) :
            zero_comb = 0
            last_zero = i-zero
            one_comb = 0
            last_one = i-one
            if last_zero >= 0 :
                zero_comb = mem[last_zero]
            if last_one >= 0 :
                one_comb = mem[last_one]
            
            mem[i] = (zero_comb + one_comb) % 1000000007
            if i >= low :
                # ans = (ans + mem[i]) % 1000000007
                ans += mem[i]
                if ans >= 1000000007 :
                    ans = ans - 1000000007
        # print(mem)
        return ans

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



