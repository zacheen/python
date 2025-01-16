# 2425. Bitwise XOR of All Pairings
# https://leetcode.com/problems/bitwise-xor-of-all-pairings/description

from typing import List
import functools

# my 
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums1) %2 :
            ans ^= functools.reduce(lambda n1,n2 : n1^n2, nums2)
        if len(nums2) %2 :
            ans ^= functools.reduce(lambda n1,n2 : n1^n2, nums1)
        return ans

# given ans
# same

s = Solution()
print("ans :",s.xorAllNums(nums1 = [1,2], nums2 = [3,4])) # 0



