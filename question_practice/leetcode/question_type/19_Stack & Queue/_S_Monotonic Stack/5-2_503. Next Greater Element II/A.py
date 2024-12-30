# my 
class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        ans = [-1]*len(nums)
        for indx, n in enumerate(nums + nums) :
            while stack and stack[-1][0] < n :
                ans[stack.pop()[1]] = n
            if indx < len(nums) :
                stack.append((n, indx))
        return ans

# given ans 概念一樣

s = Solution()
print(s.nextGreaterElements([1,2,1]))
print(s.nextGreaterElements([1,2,3,4,3]))



