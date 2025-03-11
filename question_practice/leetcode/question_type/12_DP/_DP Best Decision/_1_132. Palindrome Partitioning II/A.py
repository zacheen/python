# 132. Palindrome Partitioning II
# https://leetcode.com/problems/palindrome-partitioning-ii/description/

from typing import List
import functools

from math import inf
# my 2799ms Beats26.18%
class Solution:
    def minCut(self, s: str) -> int:
        dp = [0]+[inf]*len(s) # dp[i] 當尾巴是 i 最少的組合是
        for now_i in range(1,len(s)+1) :
            for cut_i in range(now_i):
                part = s[cut_i:now_i]
                if part == part[::-1] :
                    if cut_i == 0 :
                        dp[now_i] = 0
                    else :
                        dp[now_i] = min(dp[now_i], dp[cut_i]+1)
        return dp[-1]

# given ans
# concept is the same
# optimized : "isPalindrome[i][j] = s[i] == s[j] and isPalindrome[i + 1][j - 1]"
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # isPalindrome[i][j] := True if s[i..j] is a palindrome
        isPalindrome = [[True] * n for _ in range(n)]
        # dp[i] := the minimum cuts needed for a palindrome partitioning of s[0..i]
        dp = [n] * n

        for l in range(2, n + 1):
            i = 0
            for j in range(l - 1, n):
                isPalindrome[i][j] = s[i] == s[j] and isPalindrome[i + 1][j - 1]
                i += 1

        for i in range(n):
            if isPalindrome[0][i]:
                dp[i] = 0
                continue

            # Try all the possible partitions.
            for j in range(i):
                if isPalindrome[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

s = Solution()
print("ans :",s.minCut("a")) # 0
print("ans :",s.minCut("ab")) # 1
print("ans :",s.minCut("aab")) # 1
print("ans :",s.minCut("aabb")) # 1
print("ans :",s.minCut("aba")) # 0
print("ans :",s.minCut("abc"))




