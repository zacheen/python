# 2570. Merge Two 2D Arrays by Summing Values
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values

from typing import List
from math import inf
from collections import defaultdict

# my 
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mem = defaultdict(int)
        for i, n in nums1 :
            mem[i] = n
        for i, n in nums2 :
            mem[i] += n
        ans = [[i,s] for i,s in mem.items()]
        ans.sort()
        return ans

s = Solution()
print("ans :",s.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]])) # 



