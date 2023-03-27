# # my Beats 100%
# class Solution(object):
#     def zeroFilledSubarray(self, nums):
#         ans = 0
#         zero_count = 0
#         for n in nums :
#             if n == 0 :
#                 zero_count += 1
#             else :
#                 ans += ((zero_count*(zero_count+1))//2)
#                 zero_count = 0
#         ans += ((zero_count*(zero_count+1))//2)
#         return ans

# # given ans
# class Solution:
#     def zeroFilledSubarray(self, nums):
#         ans = 0
#         indexBeforeZero = -1

#         for i, num in enumerate(nums):
#             if num:
#                 indexBeforeZero = i
#             else:
#                 ans += i - indexBeforeZero

#         return ans
    
# 看 given ans 再優化 Beats 100%
# 同樣項目排列組合種類
# ((N+1)*N)/2 = 1+2+3 -> 所以可以每遇到一個就加上現在累計的數字
class Solution(object):
    def zeroFilledSubarray(self, nums):
        ans = 0
        zero_count = 0
        for n in nums :
            if n :
                zero_count = 0
            else :
                zero_count += 1
                ans += zero_count
        return ans
    
s = Solution()
print(s.zeroFilledSubarray(nums = [1,3,0,0,2,0,0,4]))
print(s.zeroFilledSubarray(nums = [0,0,0,2,0,0]))



