# 3455. Shortest Matching Substring
# https://leetcode.com/problems/shortest-matching-substring/description/

from typing import List
from math import inf
from bisect import bisect_left, bisect_right

# my using lcp template : 2451ms Beats29.46%
def lcp(arr) :
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
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        p_spl = p.split("*")
        pref_len = [lcp(each_part+s)[len(each_part):] for each_part in p_spl]
        fro_fit, mid_fit, end_fit = [[i for i, each_len in enumerate(each_i) if each_len>=len(ori_p)] if ori_p!="" else range(len(s)+1) for ori_p, each_i in zip(p_spl, pref_len)]

        min_ans = inf
        len_first = len(p_spl[0])
        len_mid = len(p_spl[1])
        for poss_mid in mid_fit :
            fro_i = bisect_right(fro_fit, poss_mid-len_first)-1
            if fro_i < 0 :
                continue
            fro_p = fro_fit[fro_i]

            end_i = bisect_left(end_fit, poss_mid+len_mid)
            if end_i >= len(end_fit) :
                continue
            end_p = end_fit[end_i]

            min_ans = min(min_ans, end_p-fro_p)
        if min_ans == inf :
            return -1
        else :
            return min_ans+len(p_spl[2])


# given ans


s = Solution()
print("ans :",s.shortestMatchingSubstring(s = "abaacbaecebce", p = "ba*c*ce")) # 8
print("ans :",s.shortestMatchingSubstring(s = "baccbaadbc", p = "cc*baa*adb")) # -1
print("ans :",s.shortestMatchingSubstring(s = "a", p = "**")) # 0
print("ans :",s.shortestMatchingSubstring(s = "madlogic", p = "*adlogi*")) # 6
print("ans :",s.shortestMatchingSubstring(s = "jyhpbbpund", p = "bbp*un*")) # 5
print("ans :",s.shortestMatchingSubstring(s = "jyhpbbpund", p = "*un*d")) # 3
print("ans :",s.shortestMatchingSubstring(s = "jyhpbbpun", p = "un**")) # 2



