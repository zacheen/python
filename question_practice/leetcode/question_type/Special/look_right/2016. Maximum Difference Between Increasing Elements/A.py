# 2016. Maximum Difference Between Increasing Elements
# https://leetcode.com/problems/maximum-difference-between-increasing-elements

from typing import List
from math import inf

# my 
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_ans = -1
        min_n = nums[0]
        for n in nums :
            if n > min_n :
                if (new_res := n - min_n) > max_ans :
                    max_ans = new_res
            else :
                min_n = n
        return max_ans

s = Solution()
print("ans :",s.maximumDifference([7,1,5,4])) # 4
print("ans :",s.maximumDifference([9,4,3,2])) # -1
print("ans :",s.maximumDifference([1,5,2,10])) # 9



