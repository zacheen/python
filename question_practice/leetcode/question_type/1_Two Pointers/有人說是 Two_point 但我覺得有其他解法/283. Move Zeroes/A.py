# My Runtime: 172 ms, faster than 88.54% of Python3
class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums)-1, -1, -1) :
            if nums[i] == 0 :
                del(nums[i])
                nums.append(0)

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))

