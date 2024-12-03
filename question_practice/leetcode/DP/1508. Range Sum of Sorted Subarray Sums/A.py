# 1508. Range Sum of Sorted Subarray Sums
# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums

from typing import List
import functools

# my 194ms Beats92.92%
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_array = []
        last_array = []
        for new_n in nums :
            last_array = [l_n+new_n for l_n in last_array] + [new_n]
            sum_array += last_array
        sum_array.sort()
        # print(sum_array)
        return sum(sum_array[left-1:right]) % 1000000007
        # because the numbers bigger than 1000000007 do not include multiple, so doing it at the end is faster 

# v2 611ms Beats14.60%
# import numpy as np
# class Solution:
#     def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
#         sum_array = np.array([], dtype=int)
#         last_array = np.array([], dtype=int)
#         for new_n in nums :
#             last_array = np.append(last_array+new_n, [new_n])
#             sum_array = np.append(sum_array, last_array)
#         sum_array.sort()
#         # print(sum_array)
#         return sum(sum_array[left-1:right]) % 1000000007

# # given ans
# # the same time complexity, but easier
# # Brute Force
# class Solution:
#     def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
#         arr = []
#         for i in range(n):
#             s = 0
#             for j in range(i, n):
#                 s += nums[j]
#                 arr.append(s)
#         arr.sort()
#         mod = 10**9 + 7
#         return sum(arr[left - 1 : right]) % mod

s = Solution()
print("ans :",s.rangeSum())



