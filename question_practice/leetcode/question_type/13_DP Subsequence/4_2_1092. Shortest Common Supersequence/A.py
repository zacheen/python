# 1092. Shortest Common Supersequence 
# https://leetcode.com/problems/shortest-common-supersequence

from typing import List
from math import inf

# my optimized by given ans : 338ms Beats98.83%
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # 1 finding longest common subsequence length
        dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
        for i, c1 in enumerate(str1) :
            for j, c2 in enumerate(str2) :
                if c1 == c2 :
                    dp[i+1][j+1] = dp[i][j] + 1
                else :
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        # print( dp[len(str1)][len(str2)] )
        
        # 2 
        lcs = []
        si1, si2 = len(str1), len(str2)
        while si1 > 0 and si2 > 0:
            if str1[si1-1] == str2[si2-1]:
                lcs.append(str1[si1-1])
                si1 -= 1
                si2 -= 1
            elif dp[si1-1][si2] > dp[si1][si2-1]:
                si1 -= 1
            else:
                si2 -= 1
        lcs = "".join(reversed(lcs))
        # print(lcs)

        # combine the ans
        si1 = 0
        si2 = 0
        ans = []
        for com_c in lcs :
            while (t:=str1[si1]) != com_c :
                ans.append(t)
                si1 += 1
            while (t:=str2[si2]) != com_c :
                ans.append(t)
                si2 += 1
            ans.append(com_c)
            si1 += 1
            si2 += 1
        return "".join(ans) + str1[si1:] + str2[si2:]

# # my Memory Limit Exceeded 
# class Solution:
#     def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
#         # 1 finding longest common subsequence 
#         dp = [[None]*(len(str2)+1) for _ in range(len(str1)+1)]
#         for i, c1 in enumerate(str1) :
#             for j, c2 in enumerate(str2) :
#                 if c1 == c2 :
#                     if dp[i][j] == None :
#                         dp[i+1][j+1] = [c1]
#                     else :
#                         dp[i+1][j+1] = dp[i][j] + [c1]
#                 else :
#                     if dp[i][j+1] == None :
#                         if dp[i+1][j] == None :
#                             continue
#                         dp[i+1][j+1] = dp[i+1][j]
#                     elif dp[i+1][j] == None or len(dp[i][j+1]) > len(dp[i+1][j]) :
#                         dp[i+1][j+1] = dp[i][j+1]
#                     else :
#                         dp[i+1][j+1] = dp[i+1][j]
#         com_sub = dp[len(str1)][len(str2)]

#         si1 = 0
#         si2 = 0
#         ans = []
#         for com_c in com_sub :
#             while (t:=str1[si1]) != com_c :
#                 ans.append(t)
#                 si1 += 1
#             while (t:=str2[si2]) != com_c :
#                 ans.append(t)
#                 si2 += 1
#             ans.append(com_c)
#             si1 += 1
#             si2 += 1
#         return "".join(ans) + str1[si1:] + str2[si2:]


s = Solution()
print("ans :",s.shortestCommonSupersequence(str1 = "abac", str2 = "cab")) # 
# print("ans :",s.shortestCommonSupersequence()) # 



