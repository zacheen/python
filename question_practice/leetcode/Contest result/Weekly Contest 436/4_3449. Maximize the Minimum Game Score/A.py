# 3449. Maximize the Minimum Game Score
# https://leetcode.com/problems/maximize-the-minimum-game-score/

from typing import List
import math

# given ans (combing with my binary search and optimized): 4735ms Beats100.00%
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def check_valid(low) :
            end_i = len(points)-1
            rem = m
            pre = 0
            for i, p in enumerate(points):
                k = math.ceil(low/p) - pre  # 還需要操作的次數 : 本來要操作的次數 - 為了滿足前一個數要操作的次數
                if i == end_i and k <= 0:  # 最後一個數已經滿足要求
                    break
                if k < 1:
                    k = 1  # 至少要走 1 步
                rem -= k*2-1  # 至少要走 k*2-1 or (k-1)*2+1 才能滿足 k
                if rem < 0:
                    return False
                pre = k-1  # 右邊那個數順帶操作了 k-1 次
            return True
        # print(check_valid(2))
        
        left, right = 0, min(points)*(m+1)//2
        while left + 1 < right:
            mid = (left + right) // 2
            if check_valid(mid):
                left = mid
            else:
                right = mid
        if check_valid(right) : return right
        else : return left

# # my fail : misunderstanding and I don't know how to check moves
# class Solution:
#     def maxScore(self, points: List[int], m: int) -> int:
#         def cal_moves(target) :
#             return sum(math.ceil(target/p) for p in points)
        
#         left, right = 0, 10**9+1
#         while left + 1 < right:
#             mid = (left + right) // 2
#             if cal_moves(mid) <= m:
#                 left = mid
#             else:
#                 right = mid
#         if cal_moves(right) <= m : return right
#         else : return left

s = Solution()
# print("ans :",s.maxScore(points = [2,4], m = 3)) # 4
# print("ans :",s.maxScore(points = [1,2,3], m = 5)) # 2
# print("ans :",s.maxScore(points = [1,8], m = 10)) # 5 (X)8

# # end at front
# print("ans :",s.maxScore(points = [1,1,2], m = 5)) # 2
# # print(check_valid(2))
# # end at end
# print("ans :",s.maxScore(points = [1,1,1], m = 3)) # 2
# # print(check_valid(2))
# # end at mid
print("ans :",s.maxScore(points = [2,1,2], m = 4)) # 2
# print(check_valid(2))



