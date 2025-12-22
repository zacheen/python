# 1354. Construct Target Array With Multiple Sums
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/description/

from typing import List
from math import inf
from heapq import heappop, heappush, heapify

# optimized by given ans : 0ms Beats100.00%
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        now_sum = sum(target)
        target = list(-t for t in target if t != 1)
        heapify(target)

        while target :
            # the trick is the largest number must be the last change number
            largest = -heappop(target)
            rem_sum = now_sum - largest
            if rem_sum == 1 :
                return True
            if rem_sum == 0 or largest <= rem_sum :
                return False
            prev_num = largest % rem_sum
            if prev_num == 0 :
                return False
            now_sum = rem_sum + prev_num
            if prev_num != 1 :
                heappush(target, -prev_num)
            # print(target, now_sum)
        return True

# # my : 9ms Beats58.65%
# class Solution:
#     def isPossible(self, target: List[int]) -> bool:
#         now_sum = sum(target)
#         target = list(-t for t in target if t != 1)
#         heapify(target)

#         while target :
#             # the trick is the largest number must be the last change number
#             largest = -heappop(target)
#             rem_sum = now_sum - largest
#             if rem_sum == 0 :
#                 return False
#             if rem_sum != 1 :
#                 if largest > rem_sum :
#                     prev_num = largest % rem_sum
#                 else :
#                     return False
#                 now_sum = rem_sum + prev_num
#                 if prev_num != 1 :
#                     heappush(target, -prev_num)
#             else :
#                 now_sum += 1
#             # print(target, now_sum)
#         return True
        

s = Solution()
print("ans :",s.isPossible([9,3,5])) # T
print("ans :",s.isPossible([1,1,1,2])) # F
print("ans :",s.isPossible([8,5])) # T



