# my 
# class Solution:
#     def pivotIndex(self, nums):
        
#         left_sum = 0
#         right_sum = sum(nums)-nums[0]
#         if left_sum == right_sum :
#             return 0
        
#         for indx, n in enumerate(nums[:-1]) :
#             left_sum += n
#             right_sum -= nums[indx+1]
#             # print(indx, left_sum, right_sum)
#             if left_sum == right_sum :
#                 return indx+1
            
#         return -1

# my V2
# Runtime: 151 ms, faster than 91.00% of Python3
# class Solution:
#     def pivotIndex(self, nums):
#         b_sum = [0]
#         now_sum = 0
#         for n in reversed(nums[1:]) :
#             now_sum += n
#             b_sum.append(now_sum)
#         b_sum.reverse()
        
#         now_sum = 0
#         for indx, n in enumerate(nums[:-1]) :
#             if b_sum[indx] == now_sum :
#                 return indx
#             now_sum += n
#         if now_sum == b_sum[-1] :
#             return len(nums)-1
#         return -1
        

# given ans Runtime: 148 ms, faster than 95.09% of Python3
# 直接算 (也是有道理...)
class Solution:
    def pivotIndex(self, nums):
        summ = sum(nums)
        prefix = 0

        for i, num in enumerate(nums):
            if prefix == summ - prefix - num:
                return i
            prefix += num

        return -1

s = Solution()
# print(s.pivotIndex([1,1,1,1,1,1,1]))
# print(s.pivotIndex([1,1,1,1,1,1]))
# print(s.pivotIndex([1,7,3,6,5,6]))
print(s.pivotIndex([2,1,-1]))
print(s.pivotIndex([-1,1,2]))



