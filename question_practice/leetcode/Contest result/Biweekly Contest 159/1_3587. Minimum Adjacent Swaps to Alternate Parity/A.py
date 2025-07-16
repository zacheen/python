# 3587. Minimum Adjacent Swaps to Alternate Parity
# https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/description/

from typing import List
from math import inf

# my 168ms Beats73.47%
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        odd_ind = list(n&1 for n in nums)
        odd_cnt = sum(odd_ind)
        even_cnt = len(nums) - odd_cnt

        def cal_swap(odd_start):
            exp_i = 0
            ret = 0
            for act_i, is_odd in enumerate(odd_ind) :
                if is_odd == odd_start :
                    ret += abs(exp_i - act_i) 
                    exp_i += 2
            return ret

        if odd_cnt == even_cnt :
            return min(cal_swap(0), cal_swap(1))
        elif odd_cnt == even_cnt+1 :
            # 一定要 odd 開頭 (計算 even 錯位)
            return cal_swap(1)
        elif odd_cnt+1 == even_cnt :
            # 一定要 even 開頭 (計算 odd 錯位)
            return cal_swap(0)
        else :
            return -1

s = Solution()
print("ans :",s.minSwaps([2,4,6,5,7])) # 3
print("ans :",s.minSwaps([2,4,5,7])) # 1
print("ans :",s.minSwaps([1,2,3])) # 0
print("ans :",s.minSwaps([4,5,6,8])) # -1
print("ans :",s.minSwaps([6,5,3])) # 1



