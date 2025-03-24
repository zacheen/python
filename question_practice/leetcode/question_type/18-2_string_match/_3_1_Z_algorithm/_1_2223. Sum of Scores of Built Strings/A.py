# 2223. Sum of Scores of Built Strings
# https://leetcode.com/problems/sum-of-scores-of-built-strings/description/

from typing import List
from math import inf

# my using template
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

class Solution:
    def sumScores(self, s: str) -> int:
        return sum(LCP(s)) + len(s)

s = Solution()
print("ans :",s.sumScores("babab")) # 9
print("ans :",s.sumScores("azbazbzaz")) # 14



