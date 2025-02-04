# 3432. Count Partitions with Even Sum Difference
# https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/

from typing import List
import functools

# my 
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        s = sum(nums)
        if s%2 == 0 : 
            return len(nums) - 1
        else :
            return 0

s = Solution()
print("ans :",s.countPartitions()) # 



