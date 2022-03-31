# my Runtime: 632 ms, faster than 87.39% of Python3
# class Solution:
#     def longestOnes(self, nums, k):
#         l = 0
#         remain_flip = k  # 看 given ans 其實可以用 k 就好了
#         max_len = 0
#         for r, r_num in enumerate(nums) :
#             # 我好像都沒有找到可以共用的判斷 習慣自己多創建一個變數去紀錄判斷 就會搞得很複雜
#             if r_num == 0 :
#                 remain_flip -= 1
#                 if remain_flip < 0:
#                     while True :
#                         if nums[l] == 0 :
#                             remain_flip += 1
#                             l += 1
#                             break
#                         l += 1
#                 else :
#                     max_len = max(max_len, r-l+1)
#             else :
#                 # print(l,r)
#                 max_len = max(max_len, r-l+1)
#         return max_len

# given ans
class Solution:
    def longestOnes(self, nums, k):
        ans = 0

        l = 0
        for r, a in enumerate(nums):
            if a == 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            
            # 我做了 這麼多的判斷 好像也沒有省到幾次 計算max
            ans = max(ans, r - l + 1)

        return ans


s = Solution()
# print(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
# print(s.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
# print(s.longestOnes(nums = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1], k = 3))
print(s.longestOnes(nums = [1,1,1,1,1,0,0,1,1,0,0,1,1,1,1], k = 3))
