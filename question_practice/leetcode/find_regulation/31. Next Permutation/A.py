import sys
# my Runtime: 60 ms, faster than 49.24% of Python3
# class Solution:
#     def nextPermutation(self, nums):
#         # Do not return anything, modify nums in-place instead.

#         # corner case
#         if len(nums) <= 1:
#             return
        
#         # 找尋要從哪裡開始處理
#         ro_indx = len(nums)-2
#         while ro_indx >= 0 and nums[ro_indx] >= nums[ro_indx+1] :
#             ro_indx -= 1
#         print(ro_indx)

#         # corner case 這個組合已經是最大的
#         if ro_indx == -1 :
#             nums.sort()
#             return
        
#         # 一開始思考不全 應該是找大於前一位的數字 而不是找最小的數字
#         # 找到比 ro_indx 這個位置 數字更大的數字交換位置
#         bigger = sys.maxsize
#         big_indx = None
#         for ind, num in enumerate(nums[ro_indx+1:]) :
#             if num > nums[ro_indx] and num < bigger :
#                 big_indx = ind+ro_indx+1  # ?? 不知到有沒有比較好的寫法
#                 bigger = num
        
#         # 把目前最小的數字 拿到前面
#         # 此數後面要排序
#         print(ro_indx,big_indx)
#         nums[ro_indx], nums[big_indx] = nums[big_indx], nums[ro_indx]
#         last = sorted(nums[ro_indx+1:])
#         ro_indx = ro_indx+1
#         for i in last :
#             nums[ro_indx] = i
#             ro_indx += 1

# given ans
# 想法是一樣的
# 只是做法優化
# 然後最後其實不用sort 只需要reverse就好 因為有判斷過是遞增
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # from back to front, find the first num < nums[i + 1]
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        # from back to front, find the first num > nums[i], swap it with nums[i]
        if i >= 0:
            for j in range(n - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # reverse nums[i + 1..n - 1]
        reverse(nums, i + 1, len(nums) - 1)

s = Solution()
l = [1,4,3,2]
# l = [4,3,2,1]
# l = [1,2,3,4]
# l = [1,2,4,3]
# l = [1,3,4,2]

# 思考不全 應該是找大於前一位的數字 而不是找最小的數字
# l = [2,3,4,1]
# l = [3,4,5,2,1] # 5 移前 後面 sort

# l = [1,1]
# l = [2,1,1]
# l = [1,2,1,1]

s.nextPermutation(l)
print(l)



