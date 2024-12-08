# 3366. Minimum Array Sum
# https://leetcode.com/problems/minimum-array-sum/description/

from typing import List
import functools

# my 1760ms Beats84.30%
import math
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        @functools.lru_cache(None)
        def dp(i, op1, op2):
            if op1 < 0 or op2 < 0:
                return math.inf
            if i == len(nums) :
                return 0
            now_n = nums[i]
            di2 = math.ceil(now_n/2)
            subk = now_n-k
            # do nothing
            min_ret = now_n + dp(i+1, op1, op2)
            # use op1
            min_ret = min(di2 + dp(i+1, op1-1, op2), min_ret)
            if subk >= 0 :
                # use op2
                min_ret = min(subk + dp(i+1, op1, op2-1), min_ret)
                # use op2 first and op1
                min_ret = min(math.ceil(subk/2) + dp(i+1, op1-1, op2-1), min_ret)
                # use op1 first and op2
                if di2 >= k :
                    min_ret = min((di2-k) + dp(i+1, op1-1, op2-1), min_ret)
            # print("f:",i, op1, op2, min_ret)
            return min_ret
        return dp(0, op1, op2)

# to trace the path
# import math
# class Solution:
#     def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
#         nums.reverse()
#         print(nums)
#         @functools.lru_cache(None)
#         def dp(i, op1, op2):
#             if op1 < 0 or op2 < 0:
#                 return math.inf, []
#             if i == len(nums) :
#                 return 0, []
#             now_n = nums[i]
#             di2 = math.ceil(now_n/2)
#             subk = now_n-k
#             # do nothing
#             ret_val, ret_ll = dp(i+1, op1, op2)
#             min_ret = ret_val + now_n
#             ll = [now_n] + ret_ll
#             # use op1
#             ret_val, ret_ll = dp(i+1, op1-1, op2)
#             cal_val = ret_val + di2
#             if cal_val < min_ret :
#                 ll = [di2] + ret_ll
#                 min_ret = cal_val
#             if subk >= 0 :
#                 # use op2
#                 ret_val, ret_ll = dp(i+1, op1, op2-1)
#                 cal_val = ret_val + subk
#                 if cal_val < min_ret :
#                     ll = [subk] + ret_ll
#                     min_ret = cal_val
#                 # use op2 first and op1
#                 ret_val, ret_ll = dp(i+1, op1-1, op2-1)
#                 cal_val = ret_val + math.ceil(subk/2)
#                 if cal_val < min_ret :
#                     ll = [math.ceil(subk/2)] + ret_ll
#                     min_ret = cal_val
#                 # use op1 first and op2
#                 if di2 >= k :
#                     ret_val, ret_ll = dp(i+1, op1-1, op2-1)
#                     cal_val = ret_val + (di2-k)
#                     if cal_val < min_ret :
#                         ll = [(di2-k)] + ret_ll
#                         min_ret = cal_val
#             # print("f:",i, op1, op2, min_ret)
#             return min_ret, ll
#         min_ret, ll = dp(0, op1, op2)
#         return min_ret, ll, sum(ll)


# my wrong
# from math import ceil
# import bisect
# class Solution:
#     def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
#         nums.sort()
#         theshold = 2*k-2
#         # !!
#         st = bisect.bisect_left(nums, k)
#         en = bisect.bisect_right(nums, theshold)
        
#         ans = 0
#         pass_k = 0
#         # 1 n > theshold
#         print("1:",nums[en:])
#         for n in reversed(nums[en:]) :
#             if op1 > 0 :
#                 n = ceil(n/2)
#                 op1 -= 1
#             if op2 > 0 :
#                 pass_k += 1
#                 op2 -= 1
#             ans += n
#             # print("ans1 :", ans , n)

#         nums_interval = list(reversed(nums[st:en]))
#         # 2 k~n~threshold
#         print("2:",nums_interval)
#         remain = []
#         while nums_interval and op2:
#             remain.append(nums_interval.pop()-k)
#             op2 -= 1
        
#         # 3 remain
#         remain += nums[:st] + nums_interval
#         remain.sort(reverse = True)
#         print("3:",remain)
#         for n in remain :
#             if op1 :
#                 ans += ceil(n/2)
#                 op1 -= 1
#             else :
#                 ans += n

#         # print("pass_k :",pass_k)
#         return ans - pass_k*k

# given ans

s = Solution()
# print("ans :",s.minArraySum(nums = [2,8,3,19,3], k = 3, op1 = 1, op2 = 1)) # 23
# print("ans :",s.minArraySum(nums = [2,4,3], k = 3, op1 = 2, op2 = 1)) # 3
print("ans :",s.minArraySum([1, 3, 5, 7, 9, 12, 12, 12, 13, 15, 15, 15, 16, 17, 19, 20],11,15,4))
# print("ans :",s.minArraySum())


