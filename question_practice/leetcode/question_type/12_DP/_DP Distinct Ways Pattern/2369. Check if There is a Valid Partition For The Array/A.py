# 2369. Check if There is a Valid Partition For The Array
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/

from typing import List
from math import inf

# my 77ms Beats95.38%
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [True] + [False]*len(nums)
        for i, n1 in enumerate(nums) :
            if not dp[i] : continue
            if (n2_i := i+1) < len(nums) :
                n2 = nums[n2_i]
                n3 = -inf
                if (n3_i := i+2) < len(nums) :
                    n3 = nums[n3_i]
                if n1 == n2 :
                    dp[i+2] = True
                    if n2 == n3 :
                        dp[i+3] = True
                if (n1+2 == n2+1 == n3) :
                    dp[i+3] = True
        # print(dp)
        return dp[-1]

s = Solution()
print("ans :",s.validPartition([4,4,4,5,6])) # 
print("ans :",s.validPartition([1,1,1,2])) # 



