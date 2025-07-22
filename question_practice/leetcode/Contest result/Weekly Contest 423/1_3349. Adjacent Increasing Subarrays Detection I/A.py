# 3349. Adjacent Increasing Subarrays Detection I
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description/

from typing import List
from math import inf
from itertools import pairwise

# my 72ms Beats97.47%
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1 :
            return True
        
        fit_i = [False]*len(nums)
        fit_cnt = 1 # 直接從 1 開始，這樣只要有一個符合長度就為2
        for i, (n1,n2) in enumerate(pairwise(nums)) :
            if n2 > n1 :
                fit_cnt += 1
                if fit_cnt >= k :
                    fit_i[i] = True
                    # 檢查前一個 subarray 有沒有符合
                    if fit_i[i-k] :
                        return True
            else :
                fit_cnt = 1
        # print(fit_i)
        return False
                    

s = Solution()
print("ans :",s.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], k = 3)) # T
print("ans :",s.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], k = 5)) # F
print("ans :",s.hasIncreasingSubarrays([1,-1], 1)) # T

