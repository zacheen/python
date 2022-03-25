# My
# Runtime: 36 ms, faster than 85.55% of Python3
# 不知道有沒有違反題意 ...
# from collections import Counter
# class Solution:
#     def sortColors(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         count = [0,0,0]
#         for n in nums :
#             count[n]+=1

#         indx = 0
#         for i in range(3) :
#             for ii in range(count[i]) :
#                 nums[indx] = i
#                 indx += 1

#         print(nums)

# given ans 這個方法的原理 跟我的計數差不多 而且應該還比較慢 因為要一直覆寫
# class Solution:
#     def sortColors(self, nums):
#         zero = -1
#         one = -1
#         two = -1

#         for num in nums:
#             if num == 0:
#                 two += 1
#                 one += 1
#                 zero += 1
#                 nums[two] = 2
#                 nums[one] = 1
#                 nums[zero] = 0
#             elif num == 1:
#                 two += 1
#                 one += 1
#                 nums[two] = 2
#                 nums[one] = 1
#             else:
#                 two += 1
#                 nums[two] = 2
#             print(zero, one,two)
#         print(nums)

# given ans 三點換位
# 特殊解法 可以用的情況很少
class Solution:
    def sortColors(self, nums):
        l = 0  # next 0 should be put in l
        r = len(nums) - 1  # next 2 should be put in r

        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 1:
                i += 1
            else:
                # we may swap a 0 to index i, but we're still not sure whether
                # this 0 is put in the correct index, so we can't move pointer i
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
        print(nums)

s = Solution()
print(s.sortColors([2,0,2,1,1,0]))

