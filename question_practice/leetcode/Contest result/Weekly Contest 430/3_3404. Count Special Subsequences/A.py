# 3404. Count Special Subsequences
# https://leetcode.com/problems/count-special-subsequences/description/

from typing import List
import functools

# # my fail, because I didn't notice # the gap n1,n2,n3,n4 >= 2

# given ans 2298ms Beats100.00%
from math import gcd
from collections import Counter
class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        # the gap n1,n2,n3,n4 >= 2
        # n1*n3 = n2*n4 > n4:n3 = n1:n2
        # 約分 reduction
        def mk(x, y) :
            g = gcd(x, y)
            return (x//g, y//g)
        
        mp = Counter()
        ans = 0
        n = len(nums)
        for n3_i, n3 in enumerate(nums) :
            # add new n1:n2
            if n3_i < 4 : # make sure there is enough space for n1
                continue
            n2_i = n3_i-2
            for n1 in nums[:(n2_i-2)+1] :
                mp[mk(n1, nums[n2_i])] += 1
            
            # find n4:n3 previous appears before
            for n4 in nums[n3_i+2: n] :
                s = mk(n4, n3)
                ans += mp[s]
        return ans

s = Solution()
# print("ans :",s.numberOfSubsequences(nums = [1,2,1,2])) # 0
# print("ans :",s.numberOfSubsequences(nums = [1,2,2,1])) # 0
print("ans :",s.numberOfSubsequences(nums = [1,2,3,4,3,6,1])) # 1
# print("ans :",s.numberOfSubsequences(nums = [3,4,3,4,3,4,3,4])) # 3
# print("ans :",s.numberOfSubsequences(nums = [3,4,3,4,3,4,3,4])) # 



