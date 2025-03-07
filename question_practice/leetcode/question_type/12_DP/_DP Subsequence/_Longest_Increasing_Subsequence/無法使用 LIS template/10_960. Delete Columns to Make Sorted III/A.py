# 960. Delete Columns to Make Sorted III
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/description/

from typing import List
from math import inf
from functools import cache

# 此題無法使用 template LIS_nonstrict
    # ("a","a") 如果後面有 ("b","a"),("a","b") 我們並不知道要用哪一個
# my 255ms Beats9.37%
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ord_a = ord("a")
        len_s = len(strs[0])
        nums = [[] for _ in range(len_s)]
        for s in strs:
            for i,c in enumerate(s) :
                nums[i].append(ord(c) - ord_a)
        
        @cache
        def dp(now_i, last_i) -> int:
            if now_i == len(nums) :
                return 0
            
            # del
            ret = dp(now_i+1, last_i) + 1

            # dont del
            last_n = nums[last_i]
            now_n = nums[now_i]
            if last_i == -1 or all( now >= last for now, last in zip(now_n, last_n)) :
                if (r := dp(now_i+1, now_i)) < ret :
                    ret = r
            return ret

        return dp(0,-1)
    
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

s = Solution()
print("ans :",s.minDeletionSize(["babca","bbazb"])) # 3
print("ans :",s.minDeletionSize(["edcba"])) # 4
print("ans :",s.minDeletionSize(["ghi","def","abc"])) # 0



