# 2430. Maximum Deletions on a String
# https://leetcode.com/problems/maximum-deletions-on-a-string/description/

from typing import List
from math import inf
from functools import cache

# # my : Time Limit Exceeded
# def LCP(arr) :
#     len_arr = len(arr)
#     z = [0]*len_arr
#     z_box_l = z_box_r = 0
#     for i in range(1, len_arr):
#         same_len = 0
#         if i <= z_box_r :
#             same_len = min(z_box_r-i, z[i-z_box_l])
#                 # z_box_r-i    : 如果 i~z_box_r 全部都一樣，長度會是多少
#                 # z[i-z_box_l] :  為了排除情況 "aabab"
#             # if same_len > 0 : print("fast forward") # 應該要大於1 才會 fast forward
#                        # 如果arr還有位置   and r_p 這個位置與 prefix(same_len) 相同
#         while (r_p:=i+same_len) < len_arr and arr[same_len] == arr[r_p]:
#             same_len += 1
#         z[i] = same_len
#         if r_p > z_box_r : # 目前 r_p 到更遠的位置 > 更新box
#             z_box_l = i
#             z_box_r = r_p
#     return z
# class Solution:
#     def deleteString(self, s: str) -> int:
#         dp = [-inf]*len(s)
#         dp[0] = 0
#         for i in range(len(s)) :
#             pref = LCP(s[i:])
#             new_max_op = dp[i] + 1
#             for st, each_pre in enumerate(pref) :
#                 if st == 0 :
#                     continue
#                 if each_pre >= st : # 可以刪除
#                     dp[i+st] = new_max_op
#         return max(dp) +1 # +1 加上全部刪除

# given ans : 6754ms Beats41.30%
# 使用 dp 一次做出全部的 lcp
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

# given ans : 1074ms Beats95.65%
# 再優化，只剩 DP : 根據前面可以到達的位置 繼續向後推論哪個位置可以到達
    # 且只判斷前面可以到達的位置 "if s[i] != s[0]:"
class Solution:
    def deleteString(self, s: str) -> int:
        dp = [(1, 0)]  # Start with the first valid operation [op_cou, pos]
        for back_st in range(1, len(s)):  # Iterate through the string
            # 每個可以刪除的字串開頭一定是 s[0]
            if s[back_st] != s[0]: continue  # Skip if the current char doesn't match the first char
            for op_cou, front_st in reversed(dp):  # Check previous valid operations
                back_en = 2 * back_st - front_st  # Check the length for possible match
                if back_en <= len(s) and s[front_st:back_st] == s[back_st:back_en]:  # Valid match
                    dp.append((op_cou + 1, back_st))  # Store the new operation
                    break # 為什麼可以 break? 因為愈後面的 op_cou 愈大，所以只要有一個符合即可 break
        return dp[-1][0]  # Return the max number of operations

s = Solution()
print("ans :",s.deleteString("abcabcdabc")) # 2
print("ans :",s.deleteString("aaabaab")) # 4, a > aab > a > all
print("ans :",s.deleteString("aaaa")) # 4
print("ans :",s.deleteString("abaaa")) # 1



