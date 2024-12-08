# 1760. Minimum Limit of Balls in a Bag
# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description

from typing import List
import functools

# my v1 579ms Beats74.21%
import math
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, 1000000000
        while left < right:
            mid = (left + right) // 2
            if maxOperations < sum( (n-1)//mid for n in nums) :
                left = mid + 1
            else:
                right = mid 
        return left


# my ver2 453ms Beats99.47%
# same logic, but opt "opt_nums" and "max(nums)"
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        opt_nums = [n-1 for n in nums]
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if maxOperations < sum( n//mid for n in opt_nums) :
                left = mid + 1
            else:
                right = mid 
        return left

# given ans 443ms Beats99.47%
# same logic, but opt the bisect range
import bisect
class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        # Returns the number of operations required to make m penalty.
        def numOperations(m: int) -> int:
            return sum((num - 1) // m for num in nums) <= maxOperations
        return bisect.bisect_left(range(1, max(nums)), True,
            key=lambda m: numOperations(m)) + 1

# combine version 445ms Beats99.47%
import bisect
class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        # Returns the number of operations required to make m penalty.
        opt_nums = [n-1 for n in nums]
        def numOperations(m: int) -> int:
            return sum( num//m for num in opt_nums) <= maxOperations
        return bisect.bisect_left(range(1, max(nums)), True,
            key=lambda m: numOperations(m)) + 1
    
s = Solution()
print("ans :",s.minimumSize(nums = [9], maxOperations = 2)) # 3 - [3,3,3]
print("ans :",s.minimumSize(nums = [2,4,8,2], maxOperations = 4)) # 2
# print("ans :",s.minimumSize())



