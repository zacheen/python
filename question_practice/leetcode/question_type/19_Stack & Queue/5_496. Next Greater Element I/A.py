# my Runtime: 54 ms, faster than 81.34% of Python3 
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        corr = {}
        for n in nums2 :
            while stack and stack[-1] < n :
                corr[stack.pop()] = n
            stack.append(n)
            
        return [corr.get(n, -1) for n in nums1]

# given ans 完全一樣

s = Solution()
print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))



