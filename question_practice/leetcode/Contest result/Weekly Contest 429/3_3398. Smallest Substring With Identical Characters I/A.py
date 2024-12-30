# 3398. Smallest Substring With Identical Characters I
# https://leetcode.com/problems/smallest-substring-with-identical-characters-i/description/

from typing import List
import functools
# my opt 3ms Beats94.03%
class Solution:
    def minLength(self, s: str, k: int) -> int:
        # checking len 1
        len_1_fail_count = 0
        # and count interval
        prev = s[0]
        last_c = 0
        count_list = []
        for i, c in enumerate(s) :
            # checking len 1
            len_1_fail_count += (i&1) ^ int(c)
            # count interval
            if c != prev :
                count_list.append(i-last_c)
                prev = c
                last_c = i
        count_list.append(len(s)-last_c)
        # print("count_list",count_list)
        # print("len_1_fail_count",len_1_fail_count)
        
        # return if len can be 1
        if len_1_fail_count <= k or (len(s)-len_1_fail_count) <= k :
            return 1

        # binary search 判斷哪個數符合條件
        left, right = 2, len(s) # right 通常會超出界線(因為執行的時候不會執行到這個數字) # 但是最後 l 有可能會超出範圍
        while left < right:
            mid = (left + right) // 2
            # mid OK or not
            if sum( n // (mid+1) for n in count_list ) > k: # 條件 (如果 == target 的情況 要是 False)
                # 沒通過 或 數字應該要往大的方向跑(目標沒有在 left 跟 mid 之間)
                left = mid + 1
            else:
                # 通過(包含 == target 的情況)
                right = mid 
        return left


# # 問題是我沒有辦法歸納出 排除1個的情況，我只要計算長的有幾個要 change
# # given ans
# class Solution:
#     def minLength(self, s: str, k: int) -> int:
#         s = [int(x) for x in s]
#         n = len(s)
        
#         # 先處理 0,1 交替的 case 
#         f1 = 0
#         f2 = 0
#         for i, now_s in enumerate(s):
#             if now_s ^ (i & 1): f1 += 1
#             else: f2 += 1
#         if f1 <= k or f2 <= k:
#             return 1
        
#         # 紀錄各自數量
#         cou = []
#         cur = s[0]
#         cnt = 0
#         for v in s:
#             if v == cur:
#                 cnt += 1
#             else:
#                 cou.append(cnt)
#                 cur = v
#                 cnt = 1
#         cou.append(cnt)
        
#         # binary search 判斷哪個數符合條件
#         l = 2
#         r = n
#         while l <= r:
#             m = (l + r) // 2
#             ch_c = 0
#             for x in cou:
#                 ch_c += x // (m + 1)
#             if ch_c > k: l = m + 1
#             else: r = m - 1
#         return max(l, 2)
    
# # my fail
# from itertools import pairwise
# class Solution:
#     def minLength(self, s: str, numOps: int) -> int:
#         def check_n(mid, start_change):
#             prev_n = ""
#             def change_prev_n():
#                 nonlocal prev_n
#                 if prev_n == "0" :
#                     prev_n = "1"
#                 else :
#                     prev_n = "0"
            
#             # print("check_n", mid, start_change)
#             numOps_lim = numOps
#             cou = 0
            
#             if start_change :
#                 cou = mid+1
#                 prev_n = s[0]
#             for indx, n in enumerate(s) :
#                 if n == prev_n :
#                     cou += 1
#                     # print("now cou:", cou)
#                     if cou > mid :
#                         numOps_lim -= 1
#                         # print(mid, indx, prev_n, "change")
#                         if numOps_lim < 0 :
#                             # print(mid, start_change, "False")
#                             return False
#                         cou = 1
#                         next_indx = indx+1
#                         if next_indx < len(s) and s[next_indx] != n:
#                             if mid == 2 : # might no enough space to change
#                                 prev_range = indx-2
#                                 if prev_range >= 0 and s[next_indx] == n :
#                                     change_prev_n()
#                             else :
#                                 pass
#                         else :
#                             change_prev_n()
#                 else :
#                     cou = 1
#                     prev_n = n
#                 # print("sta :",indx, prev_n, cou)
#             # print(mid, start_change, "True")
#             return True
        
#         # print("ret :",check_n(2, False))
        
#         left, right = 1, len(s) # right 通常會超出界線(因為執行的時候不會執行到這個數字) # 但是最後 l 有可能會超出範圍
#         while left < right:
#             mid = (left + right) // 2
#             # mid OK or not
#             if not(check_n(mid, True) or check_n(mid, False)) : # 條件 (如果 == target 的情況 要是 False)
#                 # 沒通過 或 數字應該要往大的方向跑(目標沒有在 left 跟 mid 之間)
#                 left = mid + 1
#             else:
#                 # 通過(包含 == target 的情況)
#                 right = mid 
#         return left

s = Solution()
print("ans :",s.minLength("000001", 1)) # 2
print("ans :",s.minLength("0000",2)) # 1
print("ans :",s.minLength("0101",0)) # 1
# print("ans :",s.minLength("0110",2)) # 1
# print("ans :",s.minLength("01101",2)) # 10101, 1
# print("ans :",s.minLength("01100",2)) # 1
# print("ans :",s.minLength("011000",3)) # 1
# print("ans :",s.minLength("01100100111111110110010010000111001111011000101011",6)) # 2
#                           #01100100110110110110010010010101001101011010101011
#                           #          ^  ^             ^  ^     ^     ^
# print("ans :",s.minLength("1011100",1)) # 2
# print("ans :",s.minLength("1001",1)) # 2
# ??


