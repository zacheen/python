# 2134. Minimum Swaps to Group All 1's Together II
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii

from typing import List
import functools

# # my 682ms Beats73.87%
# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
#         count_1 = sum(n==1 for n in nums)
#         if count_1 == 0 :
#             return 0
#         interval_count_0 = sum(n==0 for n in nums[-count_1:])
#         min_interval_count_0 = interval_count_0
#         # print(nums[-count_1:])
#         # print(interval_count_0)
#         for indx,now_n in enumerate(nums) :
#             if now_n == 0 :
#                 interval_count_0 += 1
#             if nums[indx-count_1] == 0 :
#                 interval_count_0 -= 1
#             # print(interval_count_0)
#             min_interval_count_0 = min(min_interval_count_0, interval_count_0)
#         return min_interval_count_0

# v2 Just revise to efficient grammer
# 645ms Beats95.50%
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count_1 = nums.count(1)
        if count_1 == 0 :
            return 0
        interval_count_0 = nums[-count_1:].count(0)
        min_interval_count_0 = interval_count_0
        # print(nums[-count_1:])
        # print(interval_count_0)
        for indx,now_n in enumerate(nums) :
            if not now_n:
                interval_count_0 += 1
            if not nums[indx-count_1]:
                interval_count_0 -= 1
            # print(interval_count_0)
            min_interval_count_0 = min(min_interval_count_0, interval_count_0)
        return min_interval_count_0
        

# # given ans
# # similar concept but slower
# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
#         n = len(nums)
#         k = nums.count(1)
#         ones = 0  # the number of ones in the window
#         maxOnes = 0  # the maximum number of ones in the window

#         for i in range(n * 2):
#             if i >= k and nums[i % n - k]:  # Magic in Python :)
#                 ones -= 1
#             if nums[i % n]:
#                 ones += 1
#             maxOnes = max(maxOnes, ones)

#         return k - maxOnes

s = Solution()
# print("ans :",s.minSwaps([0,1,0,1,1,0,0]))
# print("ans :",s.minSwaps([0,1,1,1,0,0,1,1,0]))
# print("ans :",s.minSwaps([1,1,0,0,1]))
print("ans :",s.minSwaps([0,0,0]))



