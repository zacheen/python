# 1458. Max Dot Product of Two Subsequences
# https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/

from typing import List
from math import inf

# my 143ms Beats89.40%
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # 1 finding longest common subsequence length
        dp = [[-inf]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        for i, c1 in enumerate(nums1) :
            for j, c2 in enumerate(nums2) :
                dp[i+1][j+1] = max((dp[i][j] if dp[i][j] > 0 else 0)+c1*c2, dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]

# optimized by given ans : using 1D array : 114ms Beats94.70%
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # 1 finding longest common subsequence length
        dp = [-inf]*(len(nums2)+1)
        for i, c1 in enumerate(nums1) :
            new_dp = [-inf]
            for j, c2 in enumerate(nums2) :
                new_dp.append( max( (dp[j] if dp[j] > 0 else 0) + c1*c2, dp[j+1], new_dp[j]) )
            dp = new_dp
        return dp[-1]

# optimized by given ans : avoid special condition :  106ms Beats98.68%
    # normally any item can be skiped
    # but special case is the list cannot be empty
        # in this case is because every multiple result is negative, so is smaller than zero causing us don't take it
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # 1 finding longest common subsequence length
        dp = [0]*(len(nums2)+1)
        for i, c1 in enumerate(nums1) :
            new_dp = [0]
            for j, c2 in enumerate(nums2) :
                new_dp.append( max(dp[j]+c1*c2, dp[j+1], new_dp[j]) )
            dp = new_dp
        if dp[-1] != 0 :
            return dp[-1]

        # 代表某個 List 都是負的 另一個 List 都是正的
        if nums1[0] <= 0 :
            # 代表nums1都是負的 或 包含0
            return max(nums1)*min(nums2)
        else :
            return min(nums1)*max(nums2)

s = Solution()
print("ans :",s.maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6])) # 18
print("ans :",s.maxDotProduct(nums1 = [3,-2], nums2 = [2,-6,7])) # 21
print("ans :",s.maxDotProduct(nums1 = [-1,-1], nums2 = [1,1])) # -1
print("ans :",s.maxDotProduct(nums1 = [-5,-1,-2], nums2 = [3,3,5,5])) # -3



