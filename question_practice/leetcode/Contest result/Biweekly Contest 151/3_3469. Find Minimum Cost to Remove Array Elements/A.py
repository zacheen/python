# 3469. Find Minimum Cost to Remove Array Elements
# https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/description/

from typing import List
from math import inf
from collections import deque
from functools import cache

# my 1472ms Beats100.00%
class Solution:
    def minCost(self, nums: List[int]) -> int:
        nums = deque([(n,i) for i, n in enumerate(nums)])

        @cache
        def dp(used):
            nonlocal nums
            if len(nums) < 3 :
                return max(n for n, i in nums)
            next_3 = [nums.popleft() for _ in range(3)]
            next_3_ori = next_3[:]
            next_3.sort()
            
            # use bigger two
            nums.appendleft(next_3[0])
            n1_place = 1 << next_3[1][1]
            n2_place = 1 << next_3[2][1]
            used = used - n1_place
            used = used - n2_place
            ret = dp(used) + max(next_3[1][0], next_3[2][0])
            nums.popleft()
            used = used | n1_place
            used = used | n2_place

            # use smaller two
            nums.appendleft(next_3[2])
            n1_place = 1 << next_3[0][1]
            n2_place = 1 << next_3[1][1]
            used = used - n1_place
            used = used - n2_place
            ret = min(dp(used) + max(next_3[0][0], next_3[1][0]), ret)
            nums.popleft()
            used = used | n1_place
            used = used | n2_place

            for item in next_3_ori[::-1] :
                nums.appendleft(item)
            return ret
        return dp((1<<len(nums))-1)
    
# optimized by given ans : 203ms Beats100.00%
class Solution:
    def minCost(self, nums: List[int]) -> int:
        len_n = len(nums)
        end_i = len_n-2

        @cache
        def dp(now_i, remain_n):
            nonlocal nums
            if now_i > end_i :
                return max(nums[now_i:] + [remain_n])
            next_now_i = now_i + 2
            next_3 = [remain_n] + nums[now_i:next_now_i]
            next_3.sort()
            
            # use bigger two
            ret = dp(next_now_i, next_3[0]) + next_3[2]

            # use smaller two
            ret = min(ret, dp(next_now_i, next_3[2]) + next_3[1])

            return ret
        return dp(1, nums[0])

s = Solution()
print("ans :",s.minCost([6,2,8,4])) # 6,8 > 2,4 : 12
print("ans :",s.minCost([2,1,3,3])) # 2,1 > 3,3 : 5
print("ans :",s.minCost([8,7,2,10,18])) # 28



