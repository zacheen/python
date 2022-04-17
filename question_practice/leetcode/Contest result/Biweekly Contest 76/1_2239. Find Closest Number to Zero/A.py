# my 
# class Solution:
#     def findClosestNumber(self, nums):
#         min_dis = abs(nums[0])
#         this_num = nums[0]
#         for n in nums :
#             if abs(n) < min_dis or (abs(n) == min_dis and n > this_num) :
#                 min_dis = abs(n)
#                 this_num = n
#         return this_num

# my 參考 given ans 的概念再優化
# Runtime: 171 ms, faster than 83.33% of Python3
class Solution:
    def findClosestNumber(self, nums):
        return min(nums, key = lambda x : (abs(x), -x) )

s = Solution()
print(s.findClosestNumber([-4,-2,1,4,8]))
print(s.findClosestNumber([2,1,-1]))
print(s.findClosestNumber([2,-1,1]))



