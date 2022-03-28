class Solution:
    def minDeletion(self, nums):
        count = 0
        del_num = 0
        for indx in range(len(nums)-1) :
            if (indx-del_num) % 2 == 0 :
                if nums[indx] == nums[indx + 1] :
                    del_num += 1
          
        if (len(nums) - del_num) % 2 == 0 :
            return del_num
        else :
            return del_num + 1

# given ans 
# 這裡的 l 不只紀錄上一個是什麼 又當作需不需要判斷的 Flag
# class Solution:
#     def minDeletion(self, nums):
#         ans = 0
#         l = None
#         for i in nums:
#             if l is None:
#                 l = i
#             elif l != i:
#                 l = None
#                 ans += 2
#         return len(nums)-ans


# given ans 
# 跳著走 -> 就不用判斷 if (indx-del_num) % 2 == 0 :
# class Solution:
#     def minDeletion(self, nums):
#         to_ret = 0
#         i = 0
#         while i < len(nums) - 1 :
#             if nums[i] == nums[i+1] :
#                 to_ret += 1
#                 i += 1
#                 continue
#             i += 2
            
#         if not to_ret % 2 == len(nums) % 2 :
#             to_ret += 1
#         return to_ret

s = Solution()
print(s.minDeletion(nums = [1,1,2,2,3,3]))

