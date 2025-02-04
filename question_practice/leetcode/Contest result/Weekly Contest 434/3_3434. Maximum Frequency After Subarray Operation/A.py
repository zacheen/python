# 3434. Maximum Frequency After Subarray Operation
# https://leetcode.com/problems/maximum-frequency-after-subarray-operation/description/

from typing import List
import functools
from math import inf

# my opt 911ms Beats82.50%
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cou = [0]*51
        max_diff = 0
        for n in nums :
            cou[n] += 1
            if n == k :
                for i in range(1,51):
                    cou[i] = max(0, cou[i]-1)
            max_diff = max( max_diff, max(cou) - cou[k])
        return max_diff + nums.count(k)

# from collections import Counter
# # my fail : hidden test case : max_diff of different number might vary at different range
# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         total_k = nums.count(k)
#         # actually, I can add zero
#         # if total_k == len(nums) : # every item is k
#         #     return len(nums) - 1
        
#         cou = Counter()
#         cou[k] = 0
#         max_diff = 0
#         l = 0
#         for indx, r_n in enumerate(nums):
#             cou[r_n] += 1
#             while cou[k]>0 and cou.most_common(1)[0][1] <= cou[k] :
#                 cou[nums[l]] -= 1
#                 l += 1
#             max_diff = max(max_diff, cou.most_common(1)[0][1] - cou[k])
#         print(total_k, max_diff)
#         return total_k + max_diff

# given ans 6352ms Beats100.00%
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(1, 51) :
            cur = 0
            for x in nums :
                cur = max(0, cur +(x == i) -(x == k)) # i 跟 k 差幾個
                res = max(res, cur)
        # print("sum :", res , nums.count(k))
        return res + nums.count(k)

# given ans 2 : state machine DP
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ans = 0
        for target in set(nums):
            f0, f1, f2 = 0, -inf, -inf
            for x in nums:
                f2 = max(f2, f1) + (x == k)
                f1 = max(f1, f0) + (x == target)
                f0 += (x == k)
                ans = max(ans, f1, f2)
        return ans
    
# given ans 3 : state machine DP optimized : 105ms Beats99.08%
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        f0 = f2 = 0
        f1 = [0] * 51
        for x in nums:
            if x == k:
                f2 += 1
                f0 += 1
            else:
                f1[x] = max(f1[x], f0) + 1
                f2 = max(f2, f1[x])
        return f2

s = Solution()
# print("ans :",s.maxFrequency(nums = [1,2,3,4,5,6], k = 1)) # 2
# print("ans :",s.maxFrequency([10,2,3,4,5,5,4,3,2,2], k = 10)) # 4
# print("ans :",s.maxFrequency([2,3,4,5,5,4,3,2,2,10], k = 10)) # 4
# print("ans :",s.maxFrequency([10,2,3,4,5,5,4,3,2,2,10], k = 10)) # 5
# print("ans :",s.maxFrequency([10,2,3,5,4,2,2,10,10], k = 2))
# print("ans :",s.maxFrequency([2,2,10,2,3,4,5,5,4,3,2,2], k = 10)) # 5
# print("ans :",s.maxFrequency([2,10,2,3,4,5,5,4,3,2,2], k = 10)) # 4
# print("ans :",s.maxFrequency([3,10,2,3,3,2,2], k = 10)) # 4
# print("ans :",s.maxFrequency([2,3,3,3,3], k = 3)) # 5
# print("ans :",s.maxFrequency([3,3,3,3,2], k = 3)) # 5
# print("ans :",s.maxFrequency([3,3,2,3,3], k = 3)) # 5
# print("ans :",s.maxFrequency([3,3,2,3,3,2,3,3], k = 3)) # 7
print("ans :",s.maxFrequency(
[37, 20, 28, 37, 28, 28, 37, 28, 37, 37, 28, 37, 20, 37, 37, 20, 20, 37, 20, 20, 20, 20, 37, 37, 20, 28, 37, 20, 20, 20, 28, 28, 20, 20, 37, 37, 28, 37, 37]
, k = 28)) # 19
print("ans :",s.maxFrequency(
[1,1,1,2,10,10,2,2,2,2]
, k = 10)) # [1,1,1,2,10,10,10,10,10,10] : 6

