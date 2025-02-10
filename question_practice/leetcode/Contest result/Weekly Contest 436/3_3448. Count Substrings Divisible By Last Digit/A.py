# 3448. Count Substrings Divisible By Last Digit
# https://leetcode.com/problems/count-substrings-divisible-by-last-digit/description/

from typing import List
from math import inf

# my optimized : 5641ms Beats100.00%
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0]*i for i in range(10)] # dp[mod][rem]
        ans = 0
        for c in s :
            now_last = int(c)
            new_dp = [[0]*i for i in range(10)]
            for mod in range(1, 10) :
                # accumulating all possible result
                for pre_rem in range(mod) :
                    new_dp[mod][(pre_rem*10+now_last)%mod] += dp[mod][pre_rem]
                # adding this new result
                new_dp[mod][now_last%mod] += 1
            if now_last : # now_last > 0 
                ans += new_dp[now_last][0]
            dp = new_dp
        return ans

# # given ans : 5952ms Beats100.00%
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         dp = [[0] * i for i in range(10)]
#         s = [int(x) for x in s]
#         ans = 0
#         for c in s:
#             new_dp = [[0] * i for i in range(10)]
#             for i in range(10):
#                 for j in range(i):
#                     new_dp[i][(j * 10 + c) % i] += dp[i][j]
#             for i in range(1, 10):
#                 new_dp[i][c % i] += 1
#             dp = new_dp
#             if c:
#                 ans += dp[c][0]
#         return ans

s = Solution()
print("ans :",s.countSubstrings("212"))
print("ans :",s.countSubstrings("12936")) # 11
print("ans :",s.countSubstrings("5701283")) # 18
print("ans :",s.countSubstrings("1010101010")) # 25



