# 300. https://leetcode.com/problems/longest-increasing-subsequence/

import math
# my Runtime: 3470 ms, faster than 62.73% of Python3
# class Solution:
#     def lengthOfLIS(self, nums):
#         nums = [-math.inf]+nums
#         length = [0]*len(nums)
        
#         for i in range(1, len(nums)):
#             max_len = 0
#             for ii in range(i,-1,-1):  
#                 if nums[ii] < nums[i] :
#                     max_len = max(max_len, length[ii]+1)
#             length[i] = max_len
        
#         print(length)
#         return max(length) 

# given ans
# 概念一樣 但優化了
# 不知道是不是因為 每次都要算 dp[i] 的位置所以比較慢
# Runtime: 3823 ms, faster than 59.98% of Python3 
# class Solution:
#     def lengthOfLIS(self, nums):
#         if not nums:
#             return 0

#         # dp[i] := LIS ending at nums[i]
#         dp = [1] * len(nums)  
#         # max_len = 1 去掉了
#         # 也不用 -math.inf
#         # 而且只要 dp[i] = max(dp[i], dp[j] + 1) 就好 更快

#         for i in range(1, len(nums)):
#             for j in range(i):  # 上面原本是想說 找到第一個比現在小的數字就要停 但最後想想不對
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)


# given ans 竟然有人用 binary search 做 (O) 好猛喔...
# Runtime: 65 ms, faster than 98.80% of Python3   3470ms變成65ms 誇張...
# 其實就是每次加入新的數字的時候都能夠快速地找到 這個數字加入之後最長的位置
# tail[i] 是紀錄 i+1 這個長度  最小的數字是多少  
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums):
        # tail[i] := the minimum tail of all increasing subseqs having length i + 1
        # it's easy to see that tail must be an increasing array
        tail = []

        for num in nums:
            if not tail or num > tail[-1]:
                tail.append(num)
            else:
                tail[bisect_left(tail, num)] = num
            print(tail)

        return len(tail)

s = Solution()
# print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
# print(s.lengthOfLIS([0,1,0,3,2,3]))
# print(s.lengthOfLIS([7,7,7,7,7,7,7]))
# print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6,8,9]))
# print(s.lengthOfLIS([1,3,6,7,9,2,10,5,6,8,9]))
# print(s.lengthOfLIS([1,3,5,7,3,5,]))

