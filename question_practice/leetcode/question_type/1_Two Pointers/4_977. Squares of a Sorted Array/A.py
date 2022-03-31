# my Runtime: 325 ms, faster than 47.35% of Pytho
# class Solution:
#     def sortedSquares(self, nums):
#         neg_list = []
#         pos_list = []

#         idx = 0
#         while idx < len(nums) and nums[idx] < 0 :
#             neg_list.append(nums[idx]**2)
#             idx += 1

#         neg_list.reverse()
#         # print(neg_list)

#         while idx < len(nums) :
#             pos_list.append(nums[idx]**2)
#             idx += 1

#         # merge two list
#         pos_idx = 0
#         for num in neg_list :
#             # print(pos_list, pos_idx, num, pos_list[pos_idx])
#             while pos_idx < len(pos_list) and num > pos_list[pos_idx] : #當前數字大於list數字 繼續找下一個位置
#                 pos_idx += 1
#             # print(pos_idx, num)
#             pos_list.insert(pos_idx, num)

#         return pos_list

# given ans 
# l r 指到兩頭 看哪一邊比較大 大的就放在list最前面
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        ans = [0] * n

        while n:
            n -= 1
            if abs(nums[l]) > abs(nums[r]):
                ans[n] = nums[l] * nums[l]
                l += 1
            else:
                ans[n] = nums[r] * nums[r]
                r -= 1

        return ans

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))
print(s.sortedSquares([-1]))