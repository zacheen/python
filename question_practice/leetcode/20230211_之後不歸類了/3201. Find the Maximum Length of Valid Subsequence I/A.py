# 3201. Find the Maximum Length of Valid Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i

from typing import List
from math import inf

# my 40ms Beats94.57%
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # (sub[0] + sub[1])  == (sub[1] + sub[2]) % 2
        # => sub[0] % 2 == sub[2] % 2
        nums = list(n&1 for n in nums)
        # both odd 
        both_odd = nums.count(1)
        # both even
        both_even = len(nums) - both_odd
        # switch
        last_n = -1
        cnt = 0
        for n in nums :
            if n != last_n :
                cnt += 1
                last_n = n
        return max(cnt, both_odd, both_even)

s = Solution()
print("ans :",s.maximumLength([1,2,3,4])) # 4
print("ans :",s.maximumLength([1,2,1,1,2,1,2])) # 6
print("ans :",s.maximumLength([1,3])) # 2



