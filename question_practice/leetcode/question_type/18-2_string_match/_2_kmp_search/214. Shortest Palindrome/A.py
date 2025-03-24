# 214. Shortest Palindrome
# https://leetcode.com/problems/shortest-palindrome/description/

from typing import List
from math import inf

def LCP(arr) :
    len_arr = len(arr)
    z = [0]*len_arr
    z_box_l = z_box_r = 0
    for i in range(1, len_arr):
        same_len = 0
        if i <= z_box_r :
            same_len = min(z_box_r-i+1, z[i-z_box_l])
                # z_box_r-i+1  : 如果 i~z_box_r 全部都一樣，長度會是多少
                # z[i-z_box_l] :  為了排除情況 "aabab"
            # if same_len > 0 : print("fast forward") # 應該要大於1 才會 fast forward
        while i + same_len < len_arr and arr[same_len] == arr[i+same_len]:
            # 這裡順序不能錯
            z_box_l = i
            z_box_r = i + same_len
            same_len += 1
        z[i] = same_len
    return z

# 回傳 pattern 在 arr 中出現的起始位置 (要全部 pattern 符合)
def pre_len(arr, pattern) :
    concat = pattern + "$" + arr  # 使用 "$" 避免 pattern 影響 arr
    Z = LCP(concat)
    return Z[len(pattern) + 1:]

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "" : return s
        pre_l = pre_len(s[::-1],s)
        for i, l in enumerate(pre_l) :
            if len(s)-i-l == 0 :
                return s[:l-1:-1]+s

s = Solution()
print("ans :",s.shortestPalindrome("aacecaaa")) # aaacecaaa
print("ans :",s.shortestPalindrome("abcd")) # dcbabcd
print("ans :",s.shortestPalindrome("ababbbabbaba")) 
                         # ababbabbbababbbabbaba



