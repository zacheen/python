# Maximum Subarray Sum – Kadane’s Algorithm
# classic
    # 53. Maximum Subarray
    # https://leetcode.com/problems/maximum-subarray/

# classic kadane_algorithm
def maxSubArray(nums):
    max_current = max_global = nums[0]
    for n in nums[1:]:
        max_current = max(n, max_current + n) # 前面是負的就歸零
        if max_current > max_global:
            max_global = max_current
    return max_global

# 較快
def maxSubArray(nums):
    max_current = 0
    max_global = nums[0]
    for n in nums:
        if max_current < 0 : # 前面是負的就歸零
            max_current = n
        else :
            max_current += n 
        if max_current > max_global:
            max_global = max_current
    return max_global

# 較好理解
def maxSubArray(self, nums):
        now_sum = 0
        maxSubArray = nums[-1]
        for n in nums :
            now_sum += n
            maxSubArray = max(maxSubArray, now_sum)
            now_sum = max(0, now_sum) # 前面是負的就歸零
        return maxSubArray

print( maxSubArray([2, 3, -8, 7, -1, 2, 3]) ) # [7, -1, 2, 3] > 11
print( maxSubArray([2, 3, -8, 2, -1, 2, 3]) ) # [2, -1, 2, 3] > 6
print( maxSubArray([-2, -4]) )
print( maxSubArray([-4, -2]) )
print( maxSubArray([5, 4, 1, 7, 8]) )