# 2294. Partition Array Such That Maximum Difference Is K
# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k

from typing import List
from math import inf

# my 73ms Beats94.02%
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        last_num = nums[0]
        ans_cou = 1
        for n in nums :
            if n-last_num > k :
                ans_cou += 1
                last_num = n
        return ans_cou

s = Solution()
print("ans :",s.partitionArray(nums = [3,6,1,2,5], k = 2)) # 2
print("ans :",s.partitionArray(nums = [1,2,3], k = 1)) # 2
print("ans :",s.partitionArray(nums = [2,2,4,5], k = 0)) # 3



