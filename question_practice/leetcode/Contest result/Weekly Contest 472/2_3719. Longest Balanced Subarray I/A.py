# 3719. Longest Balanced Subarray I
# https://leetcode.com/problems/longest-balanced-subarray-i/

from typing import List
from math import inf
from collections import defaultdict

# my v2 : 275ms Beats99.32%
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ret = 0
        len_n = len(nums)
        for st in range(len_n) :
            if len_n - st <= ret: break
            now_add_set = set()
            now_even_set = set()
            for i in range(st, len_n) :
                if nums[i]&1 :
                    now_add_set.add(nums[i])
                else :
                    now_even_set.add(nums[i])
                if len(now_add_set) == len(now_even_set) :
                    ret = max(ret, i - st + 1)
        return ret

# my 1357ms Beats85.18%
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ret = 0
        len_n = len(nums)
        for st in range(len_n) :
            now_add_set = set()
            now_even_set = set()
            for i in range(st, len_n) :
                if nums[i]&1 :
                    now_add_set.add(nums[i])
                else :
                    now_even_set.add(nums[i])
                if len(now_add_set) == len(now_even_set) :
                    ret = max(ret, i - st + 1)
        return ret
    
# # my fail : failed on [6,6]
# class Solution:
#     def longestBalanced(self, nums: List[int]) -> int:
#         st_i = defaultdict(lambda : inf)
#         st_i[0] = -1
#         ret = 0
#         cnt_odd = set()
#         cnt_even = set()
#         for i, n in enumerate(nums) :
#             if n&1 :
#                 cnt_odd.add(n)
#             else :
#                 cnt_even.add(n)
            
#             # finding the farest start indx
#             diff = len(cnt_odd) - len(cnt_even)
#             ret = max(i-st_i[diff], ret)

#             st_i[diff] = min(st_i[diff], i)
#         return ret

s = Solution()
print("ans :",s.longestBalanced([2,5,4,3])) # 4
print("ans :",s.longestBalanced([3,2,2,5,4])) # 5
print("ans :",s.longestBalanced([1,2,3,2])) # 3 : [2, 3, 2]
print("ans :",s.longestBalanced([6,6])) # 0

