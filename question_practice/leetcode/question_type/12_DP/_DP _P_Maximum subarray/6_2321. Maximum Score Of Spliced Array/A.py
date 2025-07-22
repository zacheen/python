# 2321. Maximum Score Of Spliced Array
# https://leetcode.com/problems/maximum-score-of-spliced-array/description/

from typing import List
from math import inf

# my 35ms Beats100.00%
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        diff = [n1-n2 for n1,n2 in zip(nums1, nums2)]

        # finding max subarray sum
        max_diff = -inf
        total_pos = 0
        min_diff = inf
        total_neg = 0
        for n in diff :
            # pos
            if total_pos < 0 :
                total_pos = n
            else :
                total_pos += n 
            if total_pos > max_diff:
                max_diff = total_pos

            # neg
            if total_neg > 0 :
                total_neg = n
            else :
                total_neg += n 
            if total_neg < min_diff:
                min_diff = total_neg

        return max(sum(nums2)+max_diff , sum(nums1)-min_diff)

s = Solution()
print("ans :",s.maximumsSplicedArray(nums1 = [60,60,60], nums2 = [10,90,10])) # 210
print("ans :",s.maximumsSplicedArray(nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20])) # 220
print("ans :",s.maximumsSplicedArray(nums1 = [7,11,13], nums2 = [1,1,1])) # 31



