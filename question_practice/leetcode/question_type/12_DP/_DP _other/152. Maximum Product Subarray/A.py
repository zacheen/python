# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/

from typing import List
from math import inf
from functools import reduce

# my 4ms Beats95.63%
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ans = max(nums)
        left_real = False
        right_real = False

        stack = [1]
        for n in nums + [0] :
            if n == 0 :
                if len(stack) == 1 :
                    if left_real :
                        max_ans = max(max_ans, stack[0])
                elif len(stack) == 3 :
                    if left_real :
                        max_ans = max(max_ans, stack[0])
                    if right_real :
                        max_ans = max(max_ans, stack[2])
                else :
                    if stack[2] > 0 :
                        max_ans = max(max_ans, reduce(lambda n1,n2 : n1*n2, stack))
                    else :
                        max_ans = max(max_ans, reduce(lambda n1,n2 : n1*n2, stack[:3]))
                        max_ans = max(max_ans, reduce(lambda n1,n2 : n1*n2, stack[2:]))
                stack = [1]
            elif n < 0 :
                if len(stack) == 5 :
                    stack[2] *= stack.pop()*stack.pop()
                stack.append(n)
                stack.append(1)
                right_real = False
            else :
                if len(stack) == 1 : left_real = True
                stack[-1] *= n
                right_real = True
        return max_ans

# given ans : 3ms Beats98.64%
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        r1 = r2 = -inf
        for i in nums:
            prefix*=i
            r1 = max(r1,prefix)
            if prefix == 0:
                prefix = 1
        for i in nums[::-1]:
            suffix*=i
            r2 = max(r2,suffix)
            if suffix == 0:
                suffix = 1
        return max(r1,r2)
    
# given ans DP : 10ms Beats59.99%
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
            res = max(res, curMax)
        return res

s = Solution()
print("ans :",s.maxProduct([2,3,-2,4])) # 6
print("ans :",s.maxProduct([-2,0,-1])) # 0
print("ans :",s.maxProduct([1,-2,1,-1,1])) # 2
print("ans :",s.maxProduct([1,-2,1,1,1])) # 1
print("ans :",s.maxProduct([-3,-1,-1])) # 3



