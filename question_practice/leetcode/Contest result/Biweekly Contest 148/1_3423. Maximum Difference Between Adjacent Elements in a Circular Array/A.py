# 3423. Maximum Difference Between Adjacent Elements in a Circular Array
# 

from typing import List
import functools

# my 0ms Beats100.00%
from itertools import pairwise
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = max(abs(n1-n2) for n1,n2 in pairwise(nums))
        ans = max(ans, abs(nums[-1]-nums[0]))
        return ans

s = Solution()
print("ans :",s.maxAdjacentDistance(nums = [1,2,4])) # 3



