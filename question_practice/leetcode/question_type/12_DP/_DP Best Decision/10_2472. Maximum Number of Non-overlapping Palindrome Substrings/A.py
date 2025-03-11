# 2472. Maximum Number of Non-overlapping Palindrome Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/

from typing import List
from math import inf

# my 688ms Beats45.99%
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        len_s = len(s)
        dp = [0]+[-1]*(len_s)
        for st_i, fir_c in enumerate(s) :
            for end_i in range(st_i+k, len_s+1) :
                if dp[end_i] >= dp[st_i] :
                    break
                if fir_c == s[end_i-1] :
                    now_s = s[st_i:end_i]
                    if now_s == now_s[::-1] :
                        dp[end_i] = max(dp[end_i], dp[st_i]+1)
                        break
            dp[st_i+1] = max(dp[st_i], dp[st_i+1])
        return dp[-1]

# given ans : 39ms # special algorithm
class Solution:
    def maxPalindromes(self, S: str, k: int) -> int:
        N, ans, start = len(S), 0, 0
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            while left >= start and right < N and S[left] == S[right]:
                if right + 1 - left >= k: 
                    ans += 1
                    start = right + 1
                    break
                left -= 1
                right += 1
        return ans

s = Solution()
print("ans :",s.maxPalindromes("abaccdbbd", 3)) # 2 aba, dbbd
print("ans :",s.maxPalindromes("adbcda", 2)) # 0
print("ans :",s.maxPalindromes("abaab", 3)) # 1, aba



