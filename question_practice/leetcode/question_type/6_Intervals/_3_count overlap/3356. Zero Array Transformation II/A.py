# 3356. Zero Array Transformation II 
# https://leetcode.com/problems/zero-array-transformation-ii/description/

from typing import List
import functools

# # my v1 Time Limit Exceeded
# class Solution:
#     def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
#         zero_count = nums.count(0)
#         if zero_count == len(nums) :
#             return 0
#         for indx_q, (sta, en, dec) in enumerate(queries):
#             for i in range(sta, en+1) :
#                 if nums[i] > 0 :
#                     nums[i] -= dec
#                     if nums[i] <= 0 :
#                         zero_count += 1
#                         if zero_count == len(nums) :
#                             return indx_q + 1
#         return -1

# my v2 95ms Beats99.10%
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        interval = [0]*(len(nums) + 1)
        indx_q = -1
        last_int = 0
        for indx_n, n in enumerate(nums):
            while last_int + interval[indx_n] < n :
                # 使用新的 queue
                indx_q += 1
                if indx_q == len(queries) :
                    return -1
                sta, en, dec = queries[indx_q]
                if indx_n > sta: # indx_n 在 sta~en 中間
                    if (en+1) >= indx_n :
                        # print("rev:", indx_n, sta, en, dec)
                        interval[indx_n] += dec
                        interval[en+1] -= dec
                else :
                    # print("ori:", indx_n, sta, en, dec)
                    interval[sta] += dec
                    interval[en+1] -= dec
            last_int += interval[indx_n]
            # print("last_int:",last_int)
        return indx_q+1

# given ans
# further optimized
class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        line = [0] * (len(nums) + 1)
        decrement = 0
        k = 0
        for i, num in enumerate(nums):
            while decrement + line[i] < num:
                # opt 1 : don't have to +1 when return 
                if k == len(queries):
                    return -1
                l, r, val = queries[k]
                k += 1
                # opt 2 use max(l, i)
                if r >= i:
                    line[max(l, i)] += val
                    line[r + 1] -= val
            decrement += line[i]
        return k
    
s = Solution()
# print("ans :",s.minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]))
# print("ans :",s.minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]))
# print("ans :",s.minZeroArray(nums = [0], queries = [[0,0,2]]))
# print("ans :",s.minZeroArray(nums = [8,4], queries = [[0,1,5],[1,1,5],[1,1,3],[1,1,4],[0,0,3],[1,1,4],[0,1,2],[1,1,3],[1,1,1]]))
print("ans :",s.minZeroArray(nums = [4,8,0], queries = [[0,1,5],[1,2,5]]))
# print("ans :",s.minZeroArray(nums = [1,0,6], queries = [[1,2,1],[0,0,4],[1,1,5],[0,0,5],[1,2,4],[0,2,2],[2,2,4],[1,2,2],[1,2,4],[0,1,3]]))



