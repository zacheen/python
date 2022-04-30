# Runtime: 268 ms, faster than 69.62% of Python3 
class Solution:
    def productExceptSelf(self, nums):
        count0 = 0
        pos0 = -1
        mul = 1
        
        for idx, eachNum in enumerate(nums) :
            if eachNum == 0 :
                pos0 = idx
                count0 = count0 + 1
                if count0 == 2 :
                    return [0]*len(nums)
            else :
                mul = mul * eachNum
            
        if pos0 != -1 :
            ans = [0]*len(nums)
            ans[pos0] = mul
            return ans
        
        ans = []
        for eachNum in nums :
            ans.append(mul//eachNum)
        return ans

# given ans 比較慢 總共乘三次
# Runtime: 379 ms, faster than 24.26% of Python3
# class Solution:
#     def productExceptSelf(self, nums):
#         n = len(nums)
#         ans = [1] * n

#         # use ans as the prefix product array
#         for i in range(1, n):
#             ans[i] = ans[i - 1] * nums[i - 1]

#         suffix = 1  # suffix product
#         for i, num in reversed(list(enumerate(nums))):
#             ans[i] *= suffix
#             suffix *= num

#         return ans

s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))
print(s.productExceptSelf([1,2,3,4]))