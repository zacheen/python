# 重新練習
class Solution:
    def maxProduct(self, nums):
        pass

# given ans
class Solution:
    def maxProduct(self, nums):
        if min(nums)>0:
            return reduce(lambda x, y: x*y, nums)
        if not nums:
            return 
        locMin = locMax = gloMax = nums[0]
        for i in range(1,len(nums)): # 不包含第一個數字
            if nums[i]<0:
                temp = locMax
                locMax = max(locMin*nums[i], nums[i]) # 這個是為了處理0 也同時處理了相乘之後有沒有更大
                locMin = min(temp*nums[i], nums[i])
            else:
                locMax = max(locMax*nums[i], nums[i])
                locMin = min(locMin*nums[i], nums[i])
            print(locMax, locMin)
            gloMax=max(gloMax, locMax)
        return gloMax


s = Solution()
# print(s.maxProduct([2,3,0,4]))
print(s.maxProduct([2,3,0,-2,4,-2]))
# print(s.maxProduct([-2]))