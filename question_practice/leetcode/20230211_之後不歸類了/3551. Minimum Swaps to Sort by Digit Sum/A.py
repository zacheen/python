# 3551. Minimum Swaps to Sort by Digit Sum
# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/

from typing import List
from math import inf
from collections import defaultdict
from sortedcontainers import SortedList

# given ans template : 909ms Beats99.15%
# minimum swaps to make the list ordered
def min_swaps(nums, key):
    n = len(nums)
    # order[i] : 位置 i 應該要換到哪個新位置
    order = sorted(range(n), key = lambda i: key(nums[i]))
    swaps = 0
    for current_idx, target_idx in enumerate(order):
        while current_idx != target_idx:
            order[target_idx], target_idx = target_idx, order[target_idx]
            swaps += 1
    return swaps

class Solution:
    def minSwaps(self, nums):
        def cal_val(n) :
            ret = 0
            while n :
                ret += n%10
                n //= 10
            return ret
        return min_swaps(nums, lambda x: (cal_val(x), x))

# my v2 optimized : 1629ms Beats45.22%
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def cal_val(n) :
            ret = 0
            while n :
                ret += n%10
                n //= 10
            return ret
        target = sorted(nums, key = lambda x : (cal_val(x), x))
        
        num2i = defaultdict(set)
        for i,n in enumerate(nums):
            num2i[n].add(i)
        
        ans = 0
        for i, (n , t) in enumerate(zip(nums, target)) :
            if n != t :
                ans += 1
                # swap (but actually only have to change later part)
                swap_i = num2i[t].pop()
                # update
                nums[swap_i] = n
                num2i[n].add(swap_i)
            # remove n from num2i
            num2i[n].remove(i)
        return ans

# # my v1
# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
#         def cal_val(n) :
#             ret = 0
#             while n :
#                 ret += n%10
#                 n //= 10
#             return ret
#         target = sorted(nums, key = lambda x : (cal_val(x), x))
#         print(target)
        
#         num2i = defaultdict(SortedList)
#         for i,n in enumerate(nums):
#             num2i[n].add(i)
        
#         ans = 0
#         for i, (n , t) in enumerate(zip(nums, target)) :
#             if n != t :
#                 ans += 1
#                 # swap (but actually only have to change later part)
#                 avapos = num2i[t]
#                 ret_i = avapos.bisect_left(i)
#                 if ret_i >= len(avapos) :
#                     return -1
#                 swap_i = avapos[ret_i]
#                 # update
#                 nums[swap_i] = n
#                 avapos.remove(swap_i)
#                 num2i[n].add(swap_i)
#         return ans

s = Solution()
# print("ans :",s.minSwaps([37,100])) # 1 [100, 37]
# print("ans :",s.minSwaps([22,14,33,7])) # 0 same
# print("ans :",s.minSwaps([18,43,34,16])) # 2 [16, 34, 43, 18]
# print("ans :",s.minSwaps([625468152,191921893,821181574])) # 2
print("ans :",s.minSwaps([20,30,10])) # 2



