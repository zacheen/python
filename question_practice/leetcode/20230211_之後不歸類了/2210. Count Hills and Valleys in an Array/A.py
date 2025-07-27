# 2210. Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array

from typing import List
from math import inf
from itertools import pairwise

# my 0ms
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        def get_dir(n1, n2) :
            # dir_f : 1 - increase, 0 - dec
            if n2 > n1 :
                return 1
            else :
                return  0
        
        ans_cnt = 0
        last_dir = None
        for n1, n2 in pairwise(nums) :
            if n1 == n2 : continue
            new_dir = get_dir(n1, n2)
            if last_dir == None :
                last_dir = new_dir
                continue
            if new_dir != last_dir :
                last_dir = new_dir
                ans_cnt += 1
        return ans_cnt

s = Solution()
print("ans :",s.countHillValley(nums = [2,4,1,1,6,5])) # 
print("ans :",s.countHillValley(nums = [6,6,5,5,4,1])) # 
print("ans :",s.countHillValley(nums = [6,6,6,5,6,6,6])) # 



