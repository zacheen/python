# 3659. Partition Array Into K-Distinct Groups
# https://leetcode.com/problems/partition-array-into-k-distinct-groups
    # "distinct"!!

from typing import List
from math import inf
from collections import Counter

# my 
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        if len(nums)%k != 0 :
            return False
        
        groups = len(nums)//k
        for n, cnt in Counter(nums).items():
            if cnt > groups :
                return False
        return True

s = Solution()
print("ans :",s.partitionArray(nums = [1,2,3,4], k = 2)) # T
print("ans :",s.partitionArray(nums = [3,5,2,2], k = 2)) # T
print("ans :",s.partitionArray(nums = [1,5,2,3], k = 3)) # F
print("ans :",s.partitionArray(nums = [1,3,3], k = 3))   # F

