# 796. Rotate String
# https://leetcode.com/problems/rotate-string/description/

from typing import List
from math import inf

# my using template : 0ms
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
    def rotateString(self, s: str, goal: str) -> bool:
        pre_l = pre_len(s, goal)
        for i, l in enumerate(pre_l) :
            if i+l == len(s) :
                if s[:i] == goal[l:] :
                    return True
        return False 

# given ans : 0ms
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal+goal    

s = Solution()
print("ans :",s.rotateString(s = "abcde", goal = "cdeab")) # T
print("ans :",s.rotateString(s = "abcde", goal = "abced")) # F



