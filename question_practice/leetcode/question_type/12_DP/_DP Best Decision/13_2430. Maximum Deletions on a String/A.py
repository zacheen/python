# 2430. Maximum Deletions on a String
# https://leetcode.com/problems/maximum-deletions-on-a-string/description/

from typing import List
from math import inf
from functools import cache

# given ans : 1072ms Beats83.82%
class Solution:
    def deleteString(self, s: str) -> int:
        dp = [(1, 0)]  # Start with the first valid operation
        for i in range(1, len(s)):  # Iterate through the string
            if s[i] != s[0]: continue  # Skip if the current char doesn't match the first char
            for x, j in reversed(dp):  # Check previous valid operations
                k = 2 * i - j  # Check the length for possible match
                if k <= len(s) and s[j:i] == s[i:k]:  # Valid match
                    dp.append((x + 1, i))  # Store the new operation
                    break
        return dp[-1][0]  # Return the max number of operations

# # my : Time Limit Exceeded
# def lcp(arr) :
#     len_arr = len(arr)
#     z = [0]*len_arr
#     z_box_l = z_box_r = 0
#     for i in range(1, len_arr):
#         same_len = 0
#         if i <= z_box_r :
#             same_len = min(z_box_r-i+1, z[i-z_box_l])
#                 # z_box_r-i+1  : 如果 i~z_box_r 全部都一樣，長度會是多少
#                 # z[i-z_box_l] :  為了排除情況 "aabab"
#             # if same_len > 0 : print("fast forward") # 應該要大於1 才會 fast forward
#         while i + same_len < len_arr and arr[same_len] == arr[i+same_len]:
#             # 這裡順序不能錯
#             z_box_l = i
#             z_box_r = i + same_len
#             same_len += 1
#         z[i] = same_len
#     return z

# class Solution:
#     def deleteString(self, s: str) -> int:
#         len_s = len(s)
#         dp = [0]+[-inf]*(len_s)
#         for st in range(len_s) :
#             new_cou = dp[st]+1
#             pre_cou = lcp(s[st:])
#             for i, cou in enumerate(pre_cou) :
#                 if i != 0 and cou >= i and new_cou > dp[st+i] :
#                     dp[st+i] = new_cou
#         return max(dp)+1

# given ans
# using result from another list to generate new LCP
class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        # lcs[i][j] := the number of the same letters of s[i..n) and s[j..n)
        lcs = [[0] * (n + 1) for _ in range(n + 1)]
        # dp[i] := the maximum number of operations needed to delete s[i..n)
        dp = [1] * n

        for i in range(n-1,-1,-1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    lcs[i][j] = lcs[i + 1][j + 1] + 1
                if lcs[i][j] >= j - i:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[0]

s = Solution()
# print("ans :",s.deleteString("abcabcdabc")) # 2
print("ans :",s.deleteString("aaabaab")) # 4
# print("ans :",s.deleteString("aaaaa")) # 5
# print("ans :",s.deleteString("abaaa")) # 1



