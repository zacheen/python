# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# my : 0ms
class Solution:
    def findMin(self, nums) -> int:
        if nums[0] < nums[-1] :
            return nums[0]
        
        # now decrease must be in the middle
            # the number on the left are all larger that the number on the right after decrease
        def bin_search(nums):
            left = 0
            right = len(nums)-1

            while left+1 < right :
                mid = (left+right) >> 1
                if nums[left] > nums[mid] :
                    right = mid
                else :
                    left = mid
            return nums[right]
        return bin_search(nums)

s = Solution()
# print(s.findMin([11,13,15,17]))
# print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([1,2,3,4,5]))
print(s.findMin([5,1,2,3,4]))
print(s.findMin([4,5,1,2,3]))
print(s.findMin([3,4,5,1,2]))
print(s.findMin([2,3,4,5,1]))
