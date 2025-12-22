# 1590. Make Sum Divisible by P
# https://leetcode.com/problems/make-sum-divisible-by-p

from typing import List
from math import inf
from itertools import accumulate

# my 
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p
        # print(rem)
        if rem == 0 :
            return 0
        
        mem_mod = {0:-1}
        ans = len(nums)
        # find the interval that %p is rem
        for i, acc in enumerate(accumulate(nums)) :
            now_mod = acc % p
            # diff = (now_mod - rem) % p
            diff = (now_mod - rem)
            if diff < 0 :
                diff += p
            # print(i, acc, now_mod, now_mod - rem, diff)
            # print(mem_mod)
            if diff in mem_mod :
                # print(i, mem_mod[diff])
                ans = min(ans, i - mem_mod[diff])
            mem_mod[now_mod] = i
        if ans == len(nums) :
            return -1
        return ans

s = Solution()
print("ans :",s.minSubarray(nums = [3,1,4,2], p = 6)) # 1
print("ans :",s.minSubarray(nums = [6,3,5,2], p = 9)) # 2
print("ans :",s.minSubarray(nums = [1,2,3], p = 3)) # 0
print("ans :",s.minSubarray(nums = [1,2,3], p = 7)) # -1



