# my Runtime: 543 ms, faster than 73.12% of Python3
# class Solution:
#     def canJump(self, nums):
#         able = [False]*len(nums)
#         able[0] = True
#         bound = len(nums)-1
#         for indx, n in enumerate(nums) :
#             if able[indx] :
#                 # 判斷有沒有到底
#                 next_pos = indx+n
#                 if next_pos >= bound :
#                     return True
#                 # 把可以到達的位置設成able
#                 for i in range(next_pos, indx, -1) :
#                     if able[i] :
#                         break
#                     able[i] = True
        
#         # print(able)
#         return False

# given ans
# 直接紀錄可以到達的位置 
class Solution:
    def canJump(self, nums):
        i = 0
        reach = 0

        while i < len(nums) and i <= reach:
            reach = max(reach, i + nums[i])
            i += 1

        return i == len(nums)

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
print(s.canJump([2,5,0,0]))
print(s.canJump([0]))
