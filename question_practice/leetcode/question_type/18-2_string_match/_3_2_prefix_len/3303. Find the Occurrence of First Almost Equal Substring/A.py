# 3303. Find the Occurrence of First Almost Equal Substring
# https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/description/

from typing import List
from math import inf

# my inspire by given ans : 1557ms Beats87.25%
def LCP(arr) :
    len_arr = len(arr)
    z = [0]*len_arr
    z_box_l = z_box_r = 0
    for i in range(1, len_arr):
        same_len = 0
        if i <= z_box_r :
            same_len = min(z_box_r-i, z[i-z_box_l])
                # z_box_r-i    : 如果 i~z_box_r 全部都一樣，長度會是多少
                # z[i-z_box_l] :  為了排除情況 "aabab"
            # if same_len > 0 : print("fast forward") # 應該要大於1 才會 fast forward
                       # 如果arr還有位置   and r_p 這個位置與 prefix(same_len) 相同
        while (r_p:=i+same_len) < len_arr and arr[same_len] == arr[r_p]:
            same_len += 1
        z[i] = same_len
        if r_p > z_box_r : # 目前 r_p 到更遠的位置 > 更新box
            z_box_l = i
            z_box_r = r_p
    return z
class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        f_l = LCP(pattern + s)
        b_l = LCP(pattern[::-1] + s[::-1])

        # Match s[i..i + len(pattern) - 1] with `pattern` from both the prefix and
        # the suffix.
        for i in range(len(s) - len(pattern) + 1):
            if f_l[len(pattern) + i] + b_l[len(s) - i] >= len(pattern) - 1:
                return i
        return -1

s = Solution()
print("ans :",s.minStartingIndex(s = "abcdefg", pattern = "bcdffg")) # 1
print("ans :",s.minStartingIndex(s = "cdefg", pattern = "cdffg")) # 0
print("ans :",s.minStartingIndex(s = "cdefg", pattern = "bdefg")) # 0
print("ans :",s.minStartingIndex(s = "ababbababa", pattern = "bacaba")) # 4
print("ans :",s.minStartingIndex(s = "abcd", pattern = "dba")) # -1
print("ans :",s.minStartingIndex(s = "dde", pattern = "d")) # 0

# special case
print("ans :",s.minStartingIndex(s = "ede", pattern = "d")) # 0
print("ans :",s.minStartingIndex(s = "efeff", pattern = "fe")) # 1
print("ans :",s.minStartingIndex(s = "ffggf", pattern = "gg")) # 1
