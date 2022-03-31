# my Runtime: 52 ms, faster than 94.20% of Python3
class Solution:
    def findMin(self, nums) :
        # 處理 corner case
        l,r = 0, len(nums)-1
        while l < r-1 :
            mid = (l+r)//2
            # print(l,mid,r)
            if nums[mid] == nums[r] : # 為了避免 [4,5,5,5,5] 這種情況
                r -= 1
            elif nums[mid] < nums[r] :
                r = mid
            else :
                l = mid
        
        return min(nums[l], nums[r])

s = Solution()
# print(s.findMin([11,13,15,17]))
# print(s.findMin([4,5,6,7,0,1,2]))

# print(s.findMin([1,2,3,4,5]))
# print(s.findMin([5,1,2,3,4]))
# print(s.findMin([4,5,1,2,3]))
# print(s.findMin([3,4,5,1,2]))
# print(s.findMin([2,3,4,5,1]))

# print(s.findMin([1,2,3,4,5,5]))
# print(s.findMin([5,1,2,3,4,5]))
# print(s.findMin([1,1,2,3,4,5]))
# print(s.findMin([1,2,3,4,5,1]))

# print(s.findMin([3,3,4,5,1,2]))
# print(s.findMin([3,4,5,1,2,3]))
# print(s.findMin([2,3,4,5,1,2]))
# print(s.findMin([3,4,5,1,2,2]))
# print(s.findMin([3,4,5,1,1,2]))

# print(s.findMin([4,5,5,5,5]))
# print(s.findMin([5,4,5,5,5]))
# print(s.findMin([5,5,4,5,5]))
# print(s.findMin([5,5,5,4,5]))
# print(s.findMin([5,5,5,5,4]))
