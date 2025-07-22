# 3350. Adjacent Increasing Subarrays Detection II
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description/

from typing import List
from math import inf
from itertools import pairwise
from bisect import bisect_left

# my v1 : 1586ms Beats23.08%
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        fit_i = [1]*len(nums)
        fit_cnt = 1 # 直接從 1 開始，這樣只要有一個符合長度就為2
        for i, (n1,n2) in enumerate(pairwise(nums),1) :
            if n2 > n1 :
                fit_cnt += 1
            else :
                fit_cnt = 1
            fit_i[i] = fit_cnt
        # print(fit_i)
        
        def check(k):
            for l1, l2 in zip(fit_i, fit_i[k:]) :
                if l1 >= k and l2 >= k :
                    return True
            return False

        return bisect_left(range(len(nums)//2+1), True, key= lambda x : not check(x))-1

# given ans 1281ms Beats95.19%
    # 因為一定要相鄰 > 其實只要比較
        # 1. 兩個相鄰的 最長符合subarray 其中 較短的長度
        # 2. 最長符合subarray長度 // 2 (因為這是兩個符合的 subarray 組合起來)
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 1
        length = 1
        longest = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                length += 1
            else:
                prev = length
                length = 1
            if length > longest and prev >= length:
                longest = length
            if length // 2 > longest:
                longest = length // 2
        return longest

s = Solution()
print("ans :",s.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1])) # 3
print("ans :",s.maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7])) # 2
print("ans :",s.maxIncreasingSubarrays([1,-1])) # 1
print("ans :",s.maxIncreasingSubarrays([2,5,7,8,9,-1,10,2,3,4,3,1])) # 1

