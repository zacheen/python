# my 時間區間有點大
# Runtime: 92 ms, faster than 82.56% of Python3
# Runtime: 141 ms, faster than 29.89% of Python3
# Runtime: 113 ms, faster than 55.75% of Python3
# 如果 mid 有找到  那先記錄有答案
# 再來縮 l r 的位置
# 當 l r 都是 target 之後
# 再一個一個往外擴張
class Solution:
    def searchRange(self, nums, target):
        l, r = 0, len(nums) - 1
        have_ans = False
        while l <= r:
            mid = (l + r) // 2
            # print(l, mid, r, " : ", nums[l], nums[mid], nums[r])
            if nums[mid] == target :
                # l r 位置往內縮
                have_ans = True
                if nums[l] == nums[r] :
                    break 
                elif nums[r] == nums[mid] :
                    l = mid
                else :
                    r = mid
            # 為了找到 mid == target
            elif nums[mid] < target:
                l = mid + 1 
            else:
                r = mid - 1
        print(l, r)

        if have_ans :
            while l > 0 and nums[l-1] == nums[l] :
                l = l-1
            while r < len(nums)-1 and nums[r+1] == nums[r] :
                r = r+1
            return [l,r]
        else :
            return [-1, -1]

# 第二個想法
# 先找到其中一個 target 的位置
# 再各自左右2分法 找到 l, r
# 看了 given ans 好像沒有必要先找到 某個 target ...

# given ans
# 直接找最左邊的target
# 再找最右邊的target
import bisect
class Solution:
    def searchRange(self, nums, target):
        l = bisect.bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            return -1, -1
        r = bisect.bisect_right(nums, target) - 1
        return l, r

s = Solution()
# print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
# print(s.searchRange(nums = [5,7,7,8,8,10], target = 6))
# print(s.searchRange(nums = [5,7,7,8,8,10], target = 5))
# print(s.searchRange(nums = [5,5,7,8,8,10], target = 5))
# print(s.searchRange(nums = [5,7,7,8,8,10], target = 10))
# print(s.searchRange(nums = [8,8,8,8,8,8], target = 8))
# print(s.searchRange(nums = [0,8,8,8,8,8], target = 8))
# print(s.searchRange(nums = [8,8,8,8,8,10], target = 8))
print(s.searchRange(nums = [0,8,8,8,8,10], target = 8))

# print(s.searchRange(nums = [1,3], target = 1))
# print(s.searchRange(nums = [1,2,3], target = 2))
