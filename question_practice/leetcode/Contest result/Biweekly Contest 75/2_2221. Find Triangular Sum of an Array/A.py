# my 
class Solution:
    def triangularSum(self, nums):
        while len(nums) != 1 :
            new_list = []
            for i in range(len(nums)-1) :
                new_list.append((nums[i]+nums[i+1])%10)
            nums = new_list
        return nums[0]

# 看 given ans 優化
# 但比較不直觀
# class Solution:
#     def triangularSum(self, nums):
#         for j in range(len(nums)-2, -1, -1):
#             for i in range(j+1) :
#                 # 因為其實第一格不會再用到 所以可以直接覆寫
#                 nums[i] = (nums[i]+nums[i+1])%10
#         return nums[0]

s = Solution()
print(s.triangularSum(nums = [1,2,3,4,5]))
print(s.triangularSum(nums = [5]))


