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
s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))
print(s.productExceptSelf([1,2,3,4]))