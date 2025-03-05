# 1035. Uncrossed Lines
# https://leetcode.com/problems/uncrossed-lines/description/

# my using lcs template
class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        for i, c1 in enumerate(nums1) :
            for j, c2 in enumerate(nums2) :
                if c1 == c2 :
                    dp[i+1][j+1] = dp[i][j] + 1
                else :
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
  

s = Solution()
print(s.maxUncrossedLines(nums1 = [1,4,2], nums2 = [1,2,4]))
print(s.maxUncrossedLines(nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]))
print(s.maxUncrossedLines(nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]))



