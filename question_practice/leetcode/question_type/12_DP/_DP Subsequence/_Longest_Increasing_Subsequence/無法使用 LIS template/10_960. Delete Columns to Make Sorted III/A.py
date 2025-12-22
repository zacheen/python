# 960. Delete Columns to Make Sorted III
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description/

from typing import List
from math import inf
from functools import cache
    
# my 149ms Beats28.42%
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # ord_a = ord("a")
        len_s = len(strs[0])
        nums = []
        for i in range(len_s) :
            nums.append([st[i] for st in strs])
        
        # dp[i] := 若我取用 i，我最多可以取用幾個
        dp = [1]*len(nums) # 我一定可以取用一個，就是自己
        for n_i, num in enumerate(nums):
            for past_i, past_num in enumerate(nums[:n_i]) :
                if all( now_n >= past_n for now_n, past_n in zip(num, past_num) ):
                    # can take
                    dp[n_i] = max(dp[n_i], dp[past_i]+1)
        return len_s - max(dp)
    
# my dp version
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = []
        len_s = len(strs[0])
        for col_i in range(len_s) :
            cols.append(list(s[col_i] for s in strs))
        
        @cache
        def dp(now_col):
            # dont take this col
            max_ret = 1
            for pre_col in range(now_col) :
                if all(this_c >= pre_c for this_c, pre_c in zip(cols[now_col], cols[pre_col])) :
                    # print("avai", now_col, pre_col)
                    max_ret = max(max_ret, dp(pre_col)+1) 
            return max_ret
        # print("max", dp(len_s-1))
        return len_s - max( dp(i) for i in range(len_s) )



s = Solution()
print("ans :",s.minDeletionSize(["babca","bbazb"])) # 3
print("ans :",s.minDeletionSize(["edcba"])) # 4
print("ans :",s.minDeletionSize(["ghi","def","abc"])) # 0



