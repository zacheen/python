# 1639. Number of Ways to Form a Target String Given a Dictionary
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description

from typing import List
import functools

from collections import Counter

# my 1655ms Beats35.92%
MOD = 10**9 + 7
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # count the number of each index, each word 
        # c[indx][word]
        c = [Counter() for _ in range(len(words[0]))]
        for each_w in words :
            for i, w in enumerate(each_w) :
                c[i][w] += 1
        
        fit_tar = Counter()
        fit_tar[-1] = 1
        for i in range(len(words[0])):
            for t_i in range(len(target)-1,-1,-1) :
                fit_tar[t_i] = (fit_tar[t_i] + (fit_tar[t_i-1]*c[i][target[t_i]])%MOD ) % MOD
        return fit_tar[len(target)-1] % MOD

# # my time limit exceed (but easier to understand)
# MOD = 10**9 + 7
# class Solution:
#     def numWays(self, words: List[str], target: str) -> int:
#         fit_tar = Counter()
#         fit_tar[-1] = 1
#         for i in range(len(words[0])):
#             new_fit_tar = fit_tar.copy()
#             for each_w in words :
#                 for t_i in range(len(target)-1,-1,-1) :
#                     if each_w[i] == target[t_i] :
#                         new_fit_tar[t_i] = (new_fit_tar[t_i] + fit_tar[t_i-1]) % MOD
#             fit_tar = new_fit_tar
#         return fit_tar[len(target)-1] % MOD

# given ans 929ms Beats73.24%
# optimize my solution 
class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        kMod = 1_000_000_007
        # dp[i] := the number of ways to form the first i characters of `target`
        dp = [0] * (len(target) + 1)
        dp[0] = 1

        for j in range(len(words[0])):
            # 1. only count index j, each word
            count = Counter(word[j] for word in words)
            # 2. using target[i - 1] to prevent dp[-1]
            for i in range(len(target), 0, -1):
                dp[i] += dp[i - 1] * count[target[i - 1]]
                dp[i] %= kMod

        return dp[len(target)]

s = Solution()
print("ans :",s.numWays(words = ["baab"], target = "bab")) # 2
print("ans :",s.numWays(words = ["acca","bbbb","caca"], target = "aba")) # 6
print("ans :",s.numWays(words = ["abba","baab"], target = "bab")) # 4
print("ans :",s.numWays(words = ["bb","bb"], target = "bb")) # 4




