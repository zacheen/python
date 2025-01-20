# 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/description/

# given ans
# 邏輯 不只 hash 還拆成兩半
from collections import Counter
class Solution:
    def fourSumCount(self, A, B, C, D):
        count = Counter(a + b for a in A for b in B)
        return sum(count[-c - d] for c in C for d in D)
    
# my practice again : 339ms Beats61.02%
from itertools import product
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        cou = Counter( -n1-n2 for n1,n2 in product(nums1,nums2))
        return sum(cou[n3+n4] for n3,n4 in product(nums3,nums4))

s = Solution()
print(s.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))
print(s.fourSumCount([0],[0],[0],[0]))

