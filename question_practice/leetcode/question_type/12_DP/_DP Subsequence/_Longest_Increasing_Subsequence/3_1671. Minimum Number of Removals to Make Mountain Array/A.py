# 1671. Minimum Number of Removals to Make Mountain Array
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/

from typing import List
from math import inf
from bisect import bisect_left

# my : 623ms Beats74.67%
def LIS(nums):
    stack = [inf]
    for n in nums :
        if n > stack[-1] :
            stack.append(n)
        else :
            stack[bisect_left(stack,n)] = n
    return len(stack)

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        max_ans = 0
        for i in range(1, len(nums)-1) :
            if nums[i] >= nums[i-1] and nums[i] >= nums[i+1] :
                l = LIS(nums[:i+1])
                if l <= 1 :
                    continue
                r = LIS(nums[:i-1:-1])
                if r <= 1 :
                    continue
                if (new_ans := l + r) > max_ans :
                    max_ans = new_ans
        max_ans -= 1 # 減掉中間重複計算
        return len(nums) - (max_ans)

# optimized by given ans : 19ms Beats87.73%
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        len_n = len(nums)
        sup = []
        stack = [inf]
        for n in nums[::-1] :
            if n > stack[-1] :
                stack.append(n)
            else :
                stack[bisect_left(stack,n)] = n
            sup.append(len(stack))
        sup = sup[::-1]
        
        min_delete = len_n
        stack = [inf]
        for i, n in enumerate(nums) :
            if n > stack[-1] :
                stack.append(n)
            else :
                stack[bisect_left(stack,n)] = n
            if sup[i] >= 2 and len(stack) >= 2 :
                min_delete = min(min_delete, len_n-sup[i]-len(stack)+1)
        return min_delete


            



        

s = Solution()
# print("ans :",s.minimumMountainRemovals([1,3,1])) # 0
print("ans :",s.minimumMountainRemovals([2,1,1,5,6,2,3,1])) # 3
# print("ans :",s.minimumMountainRemovals([1,2,4,3,4,2,1])) # 1
# print("ans :",s.minimumMountainRemovals([100,92,89,77,74,66,64,66,64])) # 6



