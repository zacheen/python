# 673. Number of Longest Increasing Subsequence
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description

from typing import List
import functools
from collections import Counter

# my SegTree version 34ms Beats95.76%
class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [[0,1]] * 2 * self.n

    # 更新這個位置最大長度
    def update(self, index, val, comb):
        index += self.n
        if val > self.tree[index][0] :
            self.tree[index]= [val, comb]
        elif val == self.tree[index][0] :
            self.tree[index][1] += comb
        else :
            raise Exception
        while index > 1:
            # update node
            max_len_1, comb_1 = self.tree[index]
            max_len_2, comb_2 = self.tree[index^1]
            if max_len_1 == max_len_2 :
                self.tree[index>>1] = [max_len_1, comb_1 + comb_2]
            elif max_len_1 > max_len_2 :
                self.tree[index>>1] = self.tree[index]
            else :
                self.tree[index>>1] = self.tree[index^1]
            index >>= 1

    # 查詢這個位置以前最大長度, 此長度的組合數
    def query(self, left, right):
        # include
        left += self.n
        right += self.n
        max_len = 1
        max_len_cou = 1
        while left <= right:
            if left & 1 :
                # combine result
                ret_len, cou = self.tree[left]
                if ret_len > max_len :
                    max_len = ret_len
                    max_len_cou = cou
                elif ret_len == max_len :
                    max_len_cou += cou
                left += 1
            if not (right & 1) :
                # combine result
                ret_len, cou = self.tree[right]
                if ret_len > max_len :
                    max_len = ret_len
                    max_len_cou = cou
                elif ret_len == max_len :
                    max_len_cou += cou
                right -= 1
            left >>= 1
            right>>= 1
        return (max_len, max_len_cou)

class Solution:
    def findNumberOfLIS(self, nums):
        rank = { x : i for i, x in enumerate(sorted(set(nums))) } # 各個數字的大小排行
        sg = SegTree(rank)
        for num in nums:
            prev, comb = sg.query(0, rank[num] - 1) # 判斷在這個數字之前 有幾個數字大於他
            sg.update(rank[num], prev + 1, comb) 
        return sg.query(0, len(rank)-1)[1]

# my 43ms Beats96.38%
import bisect
class Solution:
    def findNumberOfLIS(self, nums):
        mem = []
        for n in nums :
            # top left direct append
            if not mem or n > mem[-1][0][0] :
                comb = sum(comb for n, comb in mem[-1]) if mem else 1
                mem.append([])
                mem[-1].append([n, comb])
            else :
                # find the number
                indx_1D = bisect.bisect_left(mem, n, key=lambda x : x[0][0])
                each_mem = mem[indx_1D]

                # find the number position
                indx_2D = bisect.bisect_right(each_mem, -n, key=lambda x : -x[0])
                if indx_2D == len(each_mem) :
                    if indx_1D == 0 :
                        # the first one of the Subsequence
                        mem[indx_1D].append([n, 1])
                    else :
                        # sum the all combination acceptable
                        sum_indx = bisect.bisect_right(mem[indx_1D-1], -n, key=lambda x : -x[0])
                        mem[indx_1D].append([n, sum(comb for n, comb in mem[indx_1D-1][sum_indx:])])
                elif indx_2D < len(each_mem) :
                    # flush the impossible combination
                    mem[indx_1D] = mem[indx_1D][indx_2D:]
                    # if at the end
                    if indx_1D+1 >= len(mem) :
                        mem.append([])
                    # sum the all combination acceptable
                    mem[indx_1D+1].append([n, sum(comb for n, comb in mem[indx_1D])])
            # print("mem",mem)
        return sum(comb for n, comb in mem[-1])

# # given ans : slower, but more simple
# # DP O(n^2) 395ms Beats93.84%
# class Solution:
#     def findNumberOfLIS(self, nums: list[int]) -> int:
#         # length[i] := the length of the LIS ending in nums[i]
#         length = [1] * len(nums)
#         # count[i] := the number of LIS's ending in nums[i]
#         count = [1] * len(nums)
#         # Calculate the `length` and `count` arrays.
#         for i, num in enumerate(nums):
#             for j in range(i):
#                 # 如果可以相接
#                 if nums[j] < num:
#                     after_len = length[j] + 1
#                     # 如果相接後比較長 > 複寫
#                     if length[i] < after_len:
#                         length[i] = after_len
#                         count[i] = count[j]
#                     # 如果一樣長 > 組合相加
#                     elif length[i] == after_len:
#                         count[i] += count[j]

#         # Get the number of LIS.
#         ans = 0
#         maxLength = 0
#         for i, l in enumerate(length):
#             # 如果有更長的結果 覆寫之前較短的結果
#             if l > maxLength:
#                 maxLength = l
#                 ans = count[i]
#             elif l == maxLength:
#                 ans += count[i]
#         return ans

s = Solution()
print("ans :",s.findNumberOfLIS(nums = [1,3,5,4,7])) # 2
print("ans :",s.findNumberOfLIS(nums = [2,2,2,2,2])) # 5
print("ans :",s.findNumberOfLIS(nums = [1,2,3])) # 1
print("ans :",s.findNumberOfLIS(nums = [4,5,6,1,2,3])) # 2
print("ans :",s.findNumberOfLIS(nums = [4,5,6,1,2,3,7])) # 2
print("ans :",s.findNumberOfLIS(nums = [4,6,12,18,14,10,16,20])) # 1
print("ans :",s.findNumberOfLIS(nums = [2,1])) # 2



