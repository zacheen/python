# my 0ms Beats100.00%
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        corr = {}
        for n in nums2 :
            while stack and stack[-1] < n :
                corr[stack.pop()] = n
            stack.append(n)
        return [corr.get(n, -1) for n in nums1]

# my v2 0ms Beats100.00%
# same concept, but using defaultdict
from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans_rem = defaultdict(lambda : -1)
        stack = []
        for n in nums2 :
            while stack and n > stack[-1] :
                ans_rem[stack.pop()] = n
            stack.append(n)
        return [ ans_rem[n] for n in nums1 ]

# given ans same

s = Solution()
print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))



