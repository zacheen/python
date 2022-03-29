# My Runtime: 51 ms, faster than 68.41% of Python3
# class Solution:
#     def search(self, nums, target):
#         l,r = 0, len(nums)-1

#         while l < r :
#             mid = (l+r)//2
#             # print(l,mid,r, nums[l], nums[mid], nums[r], target)
#             if nums[mid] == target :
#                 return mid
            
#             # 當某個位置 右>左 時 代表這個區間是有順序的 -> 可以判斷target是否在此區間 
#             if nums[mid] >= nums[l] :
#                 if nums[mid] >= target and target >= nums[l] :
#                     # print("in l")
#                     r = mid  
#                 else :
#                     # print("out l")
#                     l = mid + 1
#             else :
#                 if nums[r] >= target and target >= nums[mid] :
#                     # print("in r")
#                     l = mid 
#                 else :
#                     # print("our r")
#                     r = mid - 1 

#         if l != len(nums) and nums[l] == target:
#             return l
#         return -1

# given ans
# 邏輯是一樣的 只是套的是 template 1  整體好看很多
class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:  # nums[l..m] are sorted
                if nums[l] <= target < nums[m]:
                    # 其實可以 "r = mid + 1" 因為前面已經判斷過 mid 不是答案 
                    r = m - 1
                else:
                    l = m + 1
            else:  # nums[m..n - 1] are sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1



s = Solution()
# print(s.search(nums = [4,5,6,7,0,1,2], target = 0))
# print(s.search(nums = [4,5,6,7,0,1,2], target = 3))
# print(s.search(nums = [1], target = 0))
# print(s.search(nums = [1], target = 1))

# for i in range(5) :
#     print(s.search(nums = [0,1,2,3,4], target = i))
# for i in range(5) :
#     print(s.search(nums = [2,3,4,0,1], target = i))

# print(s.search(nums = [0,1,2,3,4], target = 4))
