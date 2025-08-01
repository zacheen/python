# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
    # should use Kadane's Algorithm

# Kadane's Algorithm template
class Solution:
    def maxSubArray(self, nums):
        max_current = 0
        max_ans = nums[0]
        for n in nums:
            if max_current < 0 : # 前面是負的就歸零
                max_current = n
            else :
                max_current += n 
            if max_current > max_ans:
                max_ans = max_current
        return max_ans

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray([5,4,-1,7,8])) # 23



