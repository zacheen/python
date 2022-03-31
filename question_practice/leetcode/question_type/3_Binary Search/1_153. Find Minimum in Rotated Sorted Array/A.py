# 因為 最大的跟最小的 一定會連在一起
# corner case 都沒動
# my Runtime: 52 ms, faster than 64.60% of Python3
# class Solution:
#     def findMin(self, nums):
#         # 處理 corner case
#         if nums[0] < nums[-1] :
#             return nums[0]

#         l,r = 0, len(nums)-1
#         while l < r-1 :
#             mid = (l+r)//2
#             # print(l,mid,r)
#             if nums[l] > nums[mid] :
#                 r = mid
#             else :
#                 l = mid
#         return nums[r]

# given ans 
# 為什麼他沒有 corner case ?
# 如果 1~5 的全部可能組合寫出來 就會發現比較 r跟mid 真的沒有corner case
# (O) 覺得奇怪應該要從另一個方向試試看
class Solution:
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1  # 我的程式如果 +1 會有錯  為什麼他不會 ?  因為 binary search 使用的template不一樣

        return nums[l]

# My v2 如果不想要 corner case
# Runtime: 43 ms, faster than 86.00% of Python3
# class Solution:
#     def findMin(self, nums) :
#         l,r = 0, len(nums)-1
#         while l < r-1 :
#             mid = (l+r)//2
#             # print(l,mid,r)
#             if nums[mid] < nums[r] :
#                 r = mid
#             else :
#                 l = mid
        
#         return min(nums[r] , nums[l])

s = Solution()
# print(s.findMin([11,13,15,17]))
# print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([1,2,3,4,5]))
print(s.findMin([5,1,2,3,4]))
print(s.findMin([4,5,1,2,3]))
print(s.findMin([3,4,5,1,2]))
print(s.findMin([2,3,4,5,1]))
